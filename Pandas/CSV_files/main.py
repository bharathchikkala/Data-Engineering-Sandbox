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

#well for less data and all its fine to use csv inbuilt library what about we have to check thousands of columns and rows so pandas entered the chat,lets work on it!
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

#understanding the dataframes and series in pandas
print(data.to_dict())

temp_list = data["temp"].to_list()
print(temp_list)

#figuring out average of temp
print(data["temp"].mean())

print(data["temp"].max())

#Get data in columns
print(data["condition"])
print(data.condition)

#Get data in rows
print(data[data["day"] == "Monday"])
#also we can write
print(data[data.day == "Tuesday"])
print(data[data.day == "Wednesday"])

print(data.temp.max())
print(data[data.day == "Friday"])

#getting the day which recorded more temperature on the week
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


#creating dataframe from scratch

some_dict = {
    "students_id" : ["519","520","521"],
    "marks" : [19,20,20]
}
new_dataframe = pandas.DataFrame(some_dict)
print(new_dataframe)

# created dataframe to csv

new_dataframe.to_csv("DataFrame.csv")
