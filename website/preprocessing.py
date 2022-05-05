import numpy as np
import sqlite3
import pandas as pd
from sklearn.preprocessing import StandardScaler

def onehot_encode(df, column):
    dummies = pd.get_dummies(df[column], prefix=column)
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column, axis=1)
    return df

def preprocess_input(player):
    
    connection = sqlite3.connect(r"C:\Users\Igor\Documents\GitHub\Portfolio\website\static\data\database.sqlite")
    players = pd.read_sql_query("SELECT * FROM Player", connection)
    stats = pd.read_sql_query("SELECT * FROM Player_Attributes", connection)
    
    players = players.drop(['id', 'player_fifa_api_id'], axis=1)
    stats = stats.drop(['id', 'player_fifa_api_id', 'date'], axis=1)

    players['birthday'] = pd.to_datetime(players['birthday'])
    players['birth_year'] = players['birthday'].apply(lambda x: x.year)
    players['birth_month'] = players['birthday'].apply(lambda x: x.month)
    players['birth_day'] = players['birthday'].apply(lambda x: x.day)
    players = players.drop('birthday', axis=1)

    categoricals = stats.groupby(by='player_api_id', as_index=False)[['player_api_id', 'preferred_foot', 'attacking_work_rate', 'defensive_work_rate']].head(1)

    for column in ['attacking_work_rate', 'defensive_work_rate']:
        categoricals[column] = categoricals[column].apply(lambda x: np.NaN if x not in ['low', 'medium', 'high'] else x)
        categoricals[column] = categoricals[column].fillna(categoricals[column].mode()[0])

    stats = stats.groupby(by='player_api_id').mean()
    stats = stats.merge(categoricals, on='player_api_id')
    
    for column in stats.loc[:, stats.isna().sum() > 0].columns:
        stats[column] = stats[column].fillna(stats[column].mean())

    df = players.merge(stats, on='player_api_id')
    df = df.drop('player_api_id', axis=1)

    index_wanted = df.loc[df['player_name'] == player].index
    df = df.drop('player_name', axis=1)

    df['preferred_foot'] = df['preferred_foot'].replace({'left': 0, 'right': 1})

    for column in ['attacking_work_rate', 'defensive_work_rate']:
        df = onehot_encode(df, column=column)

    df = df.drop('overall_rating', axis=1)

    scaler = StandardScaler()
    scaler.fit(df)
    df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)
    df_final = df.iloc[index_wanted].values.reshape(1, -1)
  
    x = pd.DataFrame(df_final, columns=df.columns)

    return x

# print(preprocess_input('Cristiano Ronaldo'))
