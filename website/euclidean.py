import math
import sqlite3
import pandas as pd

def get_data(sql_command):
	con = sqlite3.connect(r"C:\Users\Igor\Documents\GitHub\Portfolio\website\static\data\database.sqlite")
	data = pd.read_sql(sql_command, con)
	con.close()
	return data

sqlcommand = "SELECT  A1.player_name NAME, height, weight, overall_rating, potential, preferred_foot, attacking_work_rate, defensive_work_rate, crossing, finishing, heading_accuracy, short_passing, volleys, dribbling, curve, free_kick_accuracy, long_passing, ball_control, acceleration, sprint_speed, agility, reactions, balance, shot_power, jumping, stamina, strength, long_shots, aggression, interceptions, positioning, vision, penalties, marking, standing_tackle, sliding_tackle, gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes FROM Player A1 INNER JOIN Player_Attributes A2 ON A1.player_api_id = A2.player_api_id WHERE A2.date LIKE '2015%'"
data = get_data(sqlcommand)
data = data.dropna()
unique = data["NAME"].unique()

dic = {}
for name in unique:
	row = data[data["NAME"]==name].iloc[[0]]
	name = row.iloc[0]["NAME"]
	height = row.iloc[0]["height"]
	weight = row.iloc[0]["weight"]
	overall_rating = row.iloc[0]["overall_rating"]
	potential = row.iloc[0]["potential"]
	crossing = row.iloc[0]["crossing"]
	finishing = row.iloc[0]["finishing"]
	heading_accuracy = row.iloc[0]["heading_accuracy"]
	short_passing = row.iloc[0]["short_passing"]
	volleys = row.iloc[0]["volleys"]
	dribbling = row.iloc[0]["dribbling"]
	curve = row.iloc[0]["curve"]
	free_kick_accuracy = row.iloc[0]["free_kick_accuracy"]
	long_passing = row.iloc[0]["long_passing"]
	ball_control = row.iloc[0]["ball_control"]
	acceleration = row.iloc[0]["acceleration"]
	sprint_speed = row.iloc[0]["sprint_speed"]
	agility = row.iloc[0]["agility"]
	reactions = row.iloc[0]["reactions"]
	balance = row.iloc[0]["balance"]
	shot_power = row.iloc[0]["shot_power"]
	jumping = row.iloc[0]["jumping"]
	stamina = row.iloc[0]["stamina"]
	strength = row.iloc[0]["strength"]
	long_shots = row.iloc[0]["long_shots"]
	aggression = row.iloc[0]["aggression"]
	interceptions = row.iloc[0]["interceptions"]
	positioning = row.iloc[0]["positioning"]
	vision = row.iloc[0]["vision"]
	penalties = row.iloc[0]["penalties"]
	marking = row.iloc[0]["marking"]
	standing_tackle = row.iloc[0]["standing_tackle"]
	sliding_tackle = row.iloc[0]["sliding_tackle"]
	gk_diving = row.iloc[0]["gk_diving"]
	gk_handling = row.iloc[0]["gk_handling"]
	gk_kicking = row.iloc[0]["gk_kicking"]
	gk_positioning = row.iloc[0]["gk_positioning"]
	gk_reflexes = row.iloc[0]["gk_reflexes"]
	vector = (height, weight, overall_rating,
              potential, crossing, finishing, heading_accuracy, short_passing, volleys,
              dribbling, curve, free_kick_accuracy, long_passing, ball_control,
              acceleration, sprint_speed, agility, reactions, balance, shot_power,
              jumping, stamina, strength, long_shots, aggression, interceptions,
              positioning, vision, penalties, marking, standing_tackle, sliding_tackle,
              gk_diving, gk_handling, gk_kicking, gk_positioning, gk_reflexes)

	dic[name] = vector

def euclidean_distance(vector1, vector2):
    return math.sqrt(sum((vector1[i] - vector2[i]) ** 2 for i in range(len(vector1))))

def euc_dist(asked_player):
	vector_player1 = list(dic[asked_player])
	similars = {}
	for player in dic:
		if player != asked_player:
			vector_player2 = list(dic[player])
			distance = euclidean_distance(vector_player1, vector_player2)
			similars[player] = distance
		else:
			pass
	similars_names = sorted(similars, key=similars.get, reverse=False)
	result = []
	cont = 0
	for similar in similars_names:
		if cont > 9:
			break
		result.append((similar))
		cont += 1 
	return result
    
similars = euc_dist("Cristiano Ronaldo")
# print(similars)
