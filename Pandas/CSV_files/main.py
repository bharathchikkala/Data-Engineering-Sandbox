#getting data from weather_data.csv 
with open("weather_data.csv") as csvfile:
    file = csvfile.readlines()
    print(file)
