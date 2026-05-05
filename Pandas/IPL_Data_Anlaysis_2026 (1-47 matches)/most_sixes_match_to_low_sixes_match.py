import pandas


# Load the CSV file
data = pandas.read_csv("ipl_2026_deliveries.csv")
match_no = data.match_no.unique()

# Count sixes per match
sixes_per_match = (
    data[data['batsman_runs'] == 6]   # filter only sixes
    .groupby('match_no')
    .size()                       # count sixes per match
    .reset_index(name='total_sixes')
    .sort_values(by='total_sixes', ascending=False)  # sort high → low
    .reset_index(drop=True)       # reset index after sorting
    )

data_dict = {
    # "Match" : ["Match_number", "Total_sixes_in_match"],
    "result" : [match_no, sixes_per_match]
}
final_data = pandas.DataFrame(data_dict)
final_data.to_csv("most_to_low_sixes_match.csv")
