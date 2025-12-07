players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
number_players = len(players)
one_team = number_players // 2
team_a = players[:one_team]
team_b = players[one_team:]
print(team_a)
print(team_b)
