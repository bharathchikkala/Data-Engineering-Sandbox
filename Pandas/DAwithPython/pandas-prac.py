import pandas as pd

data = [1,2,3,4,5]
series = pd.Series(data)
print(series)

# creating series from dict
dict = {
    'bharath' : 20,
    'hafy' : 13,
    'tataya' : 18
}
dict_series = pd.Series(dict)
print(dict_series)

dict_data = {
    'a' : [1,2,3,4],
    'b' : [4,5,6,7],
    'c' : [7,8,9,0]
}

df1 = pd.DataFrame(dict_data)
print(df1)
print(df1['a'])
