"""
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
"""


import requests
import json


def goals_in_half_season(half, year, team, competition):
    total_pages = 1
    page = 1
    data = ""
    goals = 0

    url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team{half}={team}&page={page}"
    data = requests.get(url)
    json_data = json.loads(data.content)
    sub_goals = [int(i[f'team{half}goals']) for i in json_data['data']]
    goals += sum(sub_goals)

    total_pages = int(json_data['total_pages'])
    if total_pages > 1:
        for i in range(2, total_pages+1):
            url = f"https://jsonmock.hackerrank.com/api/football_matches?competition={competition}&year={year}&team{half}={team}&page={i}"
            data = requests.get(url)
            json_data = json.loads(data.content)
            sub_goals = [int(i[f'team{half}goals']) for i in json_data['data']]
            goals += sum(sub_goals)

    return goals


def getTotalGoals(team, year,competition):
    return goals_in_half_season(1, year, team, competition)+goals_in_half_season(2, year, team, competition)


def getWinnerTotalGoals(competition, year):
    url = f"https://jsonmock.hackerrank.com/api/football_competitions?name={competition}&year={year}"
    data = requests.get(url)
    json_data = json.loads(data.content)
    obj_data = json_data['data']
    winner = obj_data[0]
    team = winner['winner']
    return getTotalGoals(team, year, competition)


# print(getWinnerTotalGoals("English Premier League", 2014))
