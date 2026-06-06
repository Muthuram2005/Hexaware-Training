# File Handling
# 1
import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2
import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

# 3
import csv
count = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        count += 1
print("Total Players :",count)

# Player Analytics
# 4
import csv
name = ""
highest_runs = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs = int(row[4])
        if runs > highest_runs:
            highest_runs = runs
            name = row[1]
print("Highest Runs Scorer : ",name)
print(highest_runs)

# 5
import csv
name = ""
lowest_runs = 999999
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs = int(row[4])
        if runs < lowest_runs:
            lowest_runs = runs
            name = row[1]
print("Lowest Runs Scorer : ",name)
print(lowest_runs)

# 6
import csv
runs = 0
count = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs += int(row[4])
        count += 1
print("Average Runs : ",(runs/count))

# 7
import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[4]) > 600:
            print(row[1],":",row[4])

# 8
import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if int(row[4]) < 500:
            print(row[1],":",row[4])

# Team Analytics
# 9
import csv
teams = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        teams[team] = teams.get(team, 0) + 1
print("Players by Team :",teams)

# 10
import csv
teams_runs = {}
runs = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        teams_runs[team] = teams_runs.get(team, 0) + runs
print("Total Runs by Team :",teams_runs)

# 11
import csv
teams_runs = {}
runs = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        teams_runs[team] = teams_runs.get(team, 0) + runs
highest_team = max(teams_runs, key = teams_runs.get)
print("Team with Highest Runs:",highest_team)
print("Runs :",teams_runs[highest_team])

# 12
import csv
teams_runs = {}
runs = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        teams_runs[team] = teams_runs.get(team, 0) + runs
lowest_team = min(teams_runs, key = teams_runs.get)
print("Team with Highest Runs:",lowest_team)
print("Runs :",teams_runs[lowest_team])

# Boundary Analysis
# 13
import csv
name = ""
most_fours = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        fours = int(row[5])
        if fours > most_fours:
            most_fours = fours
            name = row[1]
print("Player with most fours:",name)
print("No. of fours:",most_fours)

# 14
import csv
name = ""
most_sixes = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        sixes = int(row[6])
        if sixes > most_sixes:
            most_sixes = sixes
            name = row[1]
print("Player with most sixes:",name)
print("No. of sixes:",most_sixes)

# 15
import csv
total = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += int(row[5])
print("Total Fours in Tournament :",total)

# 16
import csv
total = 0
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += int(row[6])
print("Total Sixes in Tournament :",total)

# Lists, Sets and Dictionaries
# 17
import csv
names = []
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        names.append(row[1])
names.sort()
print("Sorted Players :",names)

# 18
import csv
teams = set()
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        teams.add(row[2])
print("Unique Teams:",teams)

# 19
import csv
team_runs = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        team = row[2]
        runs = int(row[4])
        team_runs[team] = team_runs.get(team, 0) + runs
print("Dictionary ( team : total_runs ):",team_runs)

# 20
import csv
player_runs = {}
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        player = row[1]
        runs = int(row[4])
        player_runs[player] = player_runs.get(player, 0) + runs
print("Dictionary ( player_name : runs ):",player_runs)

# Functions
# 21
import csv
def find_top_scorer():
    name = ""
    highest_runs = 0
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            runs = int(row[4])
            if runs > highest_runs:
                highest_runs = runs
                name = row[1]
    print("Top Scorer :",name)
    print("Scorer :",highest_runs)
find_top_scorer()

# 22
import csv
def calculate_average_runs():
    total = 0
    count = 0
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += int(row[4])
            count += 1
    print("Average Runs :",total / count)
calculate_average_runs()

# 23
import csv
def find_best_team():
    team_runs = {}
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            team = row[2]
            runs = int(row[4])
            team_runs[team] = team_runs.get(team, 0) + runs
    highest_team = max(team_runs, key=team_runs.get)
    print("Best Team :",highest_team)
    print("Total Runs by Team:",team_runs[highest_team])
find_best_team()

# 24
import csv
def find_total_boundaries():
    total = 0
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += int(row[5]) + int(row[6])
    print("Total Boundaries :",total)
find_total_boundaries()

# Exception Handling
# 25
import csv
try:
    with open("players.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("players.csv File Not Found")

# 26
import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            runs = int(row[4])
            print(row[1], runs)
        except ValueError:
            print("Invalid Run Value")

# 27
import csv
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        try:
            matches = int(row[3])
            print(row[1], matches)
        except ValueError:
            print("Invalid Match Count")

# NumPy
# 28
import csv
import numpy as np
runs = []
with open("players.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        runs.append(int(row[4]))
runs_array = np.array(runs)
print("Total Runs :", np.sum(runs_array))
print("Average Runs :", np.mean(runs_array))
print("Maximum Runs :", np.max(runs_array))
print("Minimum Runs :", np.min(runs_array))
print("Standard Deviation :", np.std(runs_array))
print("Median :", np.median(runs_array))

# Pandas
# 29
import pandas as pd
df = pd.read_csv("players.csv")
print(df)

#30
import pandas as pd
df = pd.read_csv("players.csv")
print(df.sort_values("runs", ascending=False).head())

# 31
import pandas as pd
df = pd.read_csv("players.csv")
print(df.sort_values("runs", ascending=False))

# 32
import pandas as pd
df = pd.read_csv("players.csv")
print(df.groupby("team")["runs"].sum())

# 33
import pandas as pd
df = pd.read_csv("players.csv")
print(df.groupby("team")["runs"].mean())

# 34
import pandas as pd
df = pd.read_csv("players.csv")
print(df[df["runs"] > 600])

# 35
import pandas as pd
df = pd.read_csv("players.csv")
team_runs = df.groupby("team")["runs"].sum()
print("Top Team :",team_runs.idxmax())
print("Runs :",team_runs.max())

# Report Generation
import csv
total_players = 0
total_runs = 0
highest_name = ""
highest_runs = 0
lowest_name = ""
lowest_runs = 999999
team_runs = {}
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        runs = int(row["runs"])
        total_players += 1
        total_runs += runs
        if runs > highest_runs:
            highest_runs = runs
            highest_name = row["player_name"]
        if runs < lowest_runs:
            lowest_runs = runs
            lowest_name = row["player_name"]
        team = row["team"]
        team_runs[team] = team_runs.get(team, 0) + runs
average_runs = total_runs / total_players
with open("cricket_report.txt", "w") as file:
    file.write("Total Players : " + str(total_players) + "\n")
    file.write("Total Runs : " + str(total_runs) + "\n")
    file.write("Average Runs : " + str(average_runs) + "\n")
    file.write("Highest Scorer : " + highest_name + "\n")
    file.write("Lowest Scorer : " + lowest_name + "\n")
    file.write("\nTeam Wise Runs\n")
    for team, runs in team_runs.items():
        file.write(team + " : " + str(runs) + "\n")
print("Report Generated Successfully")

# 36
import csv
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    with open("top_players.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["player_id", "player_name", "team", "matches", "runs", "fours", "sixes"])
        for row in reader:
            if int(row["runs"]) > 600:
                writer.writerow([row["player_id"], row["player_name"], row["team"], row["matches"], row["runs"], row["fours"], row["sixes"]])
print("top_players.csv was created successfully")

# 37
import csv
team_runs = {}
team_count = {}
with open("players.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        team = row["team"]
        runs = int(row["runs"])
        team_runs[team] = team_runs.get(team, 0) + runs
        team_count[team] = team_count.get(team, 0) + 1
with open("team_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Team", "Total Runs", "Average Runs", "Player Count"])
    for team in team_runs:
        writer.writerow([team, team_runs[team], team_runs[team] / team_count[team], team_count[team]])
print("team_summary.csv was created successfully")

# 38
import csv
players = []
try:
    with open("players.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["runs"] = int(row["runs"])
            row["fours"] = int(row["fours"])
            row["sixes"] = int(row["sixes"])
            players.append(row)
except FileNotFoundError:
    print("players.csv File Not Found")
    exit()

def player_analysis():
    highest = players[0]
    lowest = players[0]
    total_runs = 0
    for player in players:
        total_runs += player["runs"]
        if player["runs"] > highest["runs"]:
            highest = player
        if player["runs"] < lowest["runs"]:
            lowest = player
    average = total_runs / len(players)
    print("\nPLAYER ANALYSIS")
    print("Highest Scorer :", highest["player_name"], "-", highest["runs"])
    print("Lowest Scorer :", lowest["player_name"], "-", lowest["runs"])
    print("Average Runs :", average)

def team_analysis():
    team_runs = {}
    for player in players:
        team = player["team"]
        if team not in team_runs:
            team_runs[team] = 0
        team_runs[team] += player["runs"]
    print("\nTEAM ANALYSIS")
    for team, runs in team_runs.items():
        print(team, ":", runs)
    highest_team = max(team_runs, key=team_runs.get)
    print("\nBest Team :", highest_team)
    print("Total Runs :", team_runs[highest_team])

def boundary_analysis():
    most_fours = players[0]
    most_sixes = players[0]
    total_fours = 0
    total_sixes = 0
    for player in players:
        total_fours += player["fours"]
        total_sixes += player["sixes"]
        if player["fours"] > most_fours["fours"]:
            most_fours = player
        if player["sixes"] > most_sixes["sixes"]:
            most_sixes = player
    print("\nBOUNDARY ANALYSIS")
    print("Most Fours :", most_fours["player_name"], "-", most_fours["fours"])
    print("Most Sixes :", most_sixes["player_name"], "-", most_sixes["sixes"])
    print("Total Fours :", total_fours)
    print("Total Sixes :", total_sixes)

def export_report():
    total_players = len(players)
    total_runs = 0
    highest = players[0]
    lowest = players[0]
    team_runs = {}
    for player in players:
        total_runs += player["runs"]
        if player["runs"] > highest["runs"]:
            highest = player
        if player["runs"] < lowest["runs"]:
            lowest = player
        team = player["team"]
        if team not in team_runs:
            team_runs[team] = 0
        team_runs[team] += player["runs"]
    average_runs = total_runs / total_players
    with open("cricket_report.txt", "w") as file:
        file.write("CRICKET ANALYTICS REPORT\n\n")
        file.write("Total Players : " + str(total_players) + "\n")
        file.write("Total Runs : " + str(total_runs) + "\n")
        file.write("Average Runs : " + str(average_runs) + "\n")
        file.write("Highest Scorer : " + highest["player_name"] + "\n")
        file.write("Lowest Scorer : " + lowest["player_name"] + "\n")
        file.write("\nTEAM WISE RUNS\n")
        for team, runs in team_runs.items():
            file.write(team + " : " + str(runs) + "\n")
    print("cricket_report.txt Generated Successfully")

while True:
    print("\n===== SMART CRICKET ANALYTICS SYSTEM =====")
    print("1. Player Analysis")
    print("2. Team Analysis")
    print("3. Boundary Analysis")
    print("4. Export Reports")
    print("5. Exit")
    choice = input("Enter Choice : ")
    if choice == "1":
        player_analysis()
    elif choice == "2":
        team_analysis()
    elif choice == "3":
        boundary_analysis()
    elif choice == "4":
        export_report()
    elif choice == "5":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
