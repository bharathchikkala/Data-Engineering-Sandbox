'''
just playing around with the dataset of ipl first 47 matches below we have seen like total sixes, batters,
particular batter runs or sixes he scored and all

In the end we can add it to dataframe if we want by just using (.DataFrame) method from pandas.
'''


import pandas

data = pandas.read_csv("ipl_2026_deliveries.csv")

'''
#total sixes in 47 matches(match 12 was not accurately there in kaggle dataset,untill we learn web scraping we have to
use this kaggle datasets
'''
total_sixes = len(data[data["batsman_runs"] == 6])
print(total_sixes)

#particular from dataset sixes he hit,and his runs sum and his runs to list and all
abhishek_sharma = data[data["batter"] == "Abhishek Sharma"]
# print(abhishek_sharma)
sixes = abhishek_sharma[abhishek_sharma["batsman_runs"] == 6]
print(len(sixes))
runs = abhishek_sharma["batsman_runs"]
print(len(runs))
print(runs.tolist())
print(runs.sum())



#Match numbers from dataset
matches = data.match_no
all_matches = matches.drop_duplicates()
list_matches = all_matches.tolist()
print(list_matches)

#Teams that are present in dataset
teams = data.batting_team
what_teams = teams.drop_duplicates()
print(what_teams.tolist())


#balls kohli faced and sixes he hit
kohli = data[data["batter"] == "Virat Kohli"]
print(len(kohli))
travis_sixes = len(kohli[kohli["batsman_runs"] == 6])
print(travis_sixes)


#total batters who are in strike(faced even 1 ball in first 47 matches)
total_batters = data.batter
unique_batters = total_batters.drop_duplicates()
list_batters = unique_batters.tolist()
# print(list_batters)
for batter in unique_batters:
    print(batter)
