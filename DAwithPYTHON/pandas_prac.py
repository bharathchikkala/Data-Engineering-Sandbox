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


df = pd.read_csv('data.csv')
print(df.head(2))
print(df.tail(2))

print(dict_data)
print(dict_data['a'][0])

print(df1)
print(df1.loc[0,'a'])
print(df1.loc[0,'b'])
print(df1.loc[0,'c'])
print(df1.iloc[3,1])

# data manipulation with dataframe

df1['m'] = [19,20,21,13]
print(df1)

print(df1.loc[1,'m'])
print(df1.iloc[1,3])

df1.drop('c',axis=1, inplace=True)
print(df1)
