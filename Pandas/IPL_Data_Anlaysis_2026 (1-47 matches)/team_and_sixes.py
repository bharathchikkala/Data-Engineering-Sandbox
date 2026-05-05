
import pandas


# Load the CSV file
data = pandas.read_csv("ipl_2026_deliveries.csv")


# Filter for match number 20
match_number = 20
match_data = data[data['match_no'] == match_number]


# Get unique batters and bowlers
batters = sorted(match_data['batter'].unique())
bowlers = sorted(match_data['bowler'].unique())
# Count total sixes in the match
total_sixes = (match_data['batsman_runs'] == 6).sum()


data_dict = {
    "Match_info": ["Match No: ", "Batters: ", "Bowlers: ", "Total Sixes: "],
    "Match_data": [match_number , batters, bowlers, total_sixes]
}

main_data = pandas.DataFrame(data_dict)
main_data.to_csv("team_and_sixes.csv")
