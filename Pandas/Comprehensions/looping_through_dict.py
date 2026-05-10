new_dict = {
    "students" : ["raja","akka","bharath"],
    "score" : [80,95,99]
}
#looping through dictionaries
for (key,value) in new_dict.items():
    print(key)

import pandas
students_dataframe = pandas.DataFrame(new_dict)
print(students_dataframe)


for (index, row) in students_dataframe.iterrows():
    print(index)
    print(row)
    print(row.students)
    print(row.score)
    if row.score >= 80:
        print(row.students)
