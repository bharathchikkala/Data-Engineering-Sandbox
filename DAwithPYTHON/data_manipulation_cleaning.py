import pandas as pd

df = pd.read_csv('data.csv')
print(df)

print(df.isnull().any())

# knowing total nulls in each one
total_nulls = df.isnull().sum()
print(total_nulls)

# print(df.fillna(0))

# print(df)

df['Sales_fill_NA'] = df['Sales'].fillna(df['Sales'].mean())
# if need to change sales column then df['sales'] inplace of df['Sales-fill_NA']

# print(df)

# print(df)
# print(df.dtypes)

# rename columns
df = df.rename(columns={'Date':'Sales_date'})
print(df.head())

df['New_Value'] = df['Value'].fillna(df['Value'].mean()).astype(int)
print(df.head())


df['Change_Rates'] = df['Value'].fillna(df['Value'].mean()).apply(lambda x:x*2).astype(int)
print(df.head())

# grouping
grouped_mean = df.groupby('Product')['Value'].mean()
print(grouped_mean)

# group sum
group_sum = df.groupby(['Product','Region'])['Value'].sum()
print(group_sum)

# aggregate multiple functions
grouped_agg = df.groupby('Region')['Value'].agg(['mean', 'sum', 'count'])
print(grouped_agg)


# merging and joining
df1 = pd.DataFrame(
    {
        'Key' : ['A','B','C','D'],
        'Value' : [1,2,3,4],
    }
)

df2 = pd.DataFrame(
    {
        'Key' : ['A','B','Z','M'],
        'Value' : [19,20,2,1],
    }
)
print(df1)
print(df2)

# merging on key
print(pd.merge(df1,df2,on='Key',how='right'))
print(pd.merge(df1,df2,on='Key',how='outer'))

print(df1.info())
print(df1.describe())
