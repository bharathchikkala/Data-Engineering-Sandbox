#getting data from weather_data.csv 
with open("weather_data.csv") as csvfile:
    file = csvfile.readlines()
    print(file)

#byusing csv inbuilt library getting temp data into list
import csv

with open("weather_data.csv") as csvfile:
    data = csv.reader(csvfile)
    temperatures = []
    for row_temp in data:
        if row_temp[1] != "temp":
            temperatures.append(int(row_temp[1]))
    print(temperatures)
