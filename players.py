team_list=[
    ["Virat","Rohit","Ganguly"],
    ["james","righ","sam"],
    ["kai","hun","joo"]

]
print(team_list)
print(team_list[0][1])
team_list[0][1] = "dinesh"
print(team_list)

for indi_team in team_list:
    print(f"team:{indi_team}")
    for team_player in indi_team:
        print(team_player)
        if(team_player == "dinesh"):
            print("captain")