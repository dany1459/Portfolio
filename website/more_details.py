import sqlite3
import pandas as pd

def get_more_details(player):
    sqlcommand = "SELECT A1.player_name player_name, birthday, height, weight, overall_rating, preferred_foot FROM Player A1 INNER JOIN Player_Attributes A2 ON A1.player_api_id = A2.player_api_id WHERE A2.date LIKE '2015%'"
    connection = sqlite3.connect(r"C:\Users\Igor\Documents\GitHub\Portfolio\website\static\data\database.sqlite")
    players = pd.read_sql_query(sqlcommand, connection)

    players['birthday'] = pd.to_datetime(players['birthday'])
    players['birth_year'] = players['birthday'].apply(lambda x: x.year)
    players = players.drop('birthday', axis=1)

    index_wanted = players.loc[players['player_name'] == player].index
    players = players.drop(['player_name'], axis=1)
    players['weight'] = players['weight'].apply(lambda x: x/2.2)
    df_final = players.iloc[index_wanted[0]].values.reshape(1, -1)
    x = pd.DataFrame(df_final, columns=players.columns)
    return x

# print(get_more_details('Cristiano Ronaldo'))
