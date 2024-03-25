import pandas as pd

##3.1
foot_ball = pd.read_csv("football.csv")

##3.2
print(foot_ball.tail(7))

##3.3.1
print(foot_ball[['Nationality', 'Club']].head())

##3.3.2
print(foot_ball.iloc[9])

##3.3.3
print(foot_ball.loc[100:110, ['Goals', 'Appearances']])

# #3.3.5
foot_ball['Goals per Appearance'] = foot_ball['Goals'] / foot_ball['Appearances']


print(foot_ball.head())


arsenal_players = foot_ball[foot_ball['Club'] == 'Arsenal']
print(arsenal_players)


# Filter players who have scored more than 5 goals
high_scorers = foot_ball[foot_ball['Goals'] > 5]
print(high_scorers)
