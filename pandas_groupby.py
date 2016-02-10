import pandas as pd

df = pd.read_csv('data/mlbsalaries.csv')

# print df.describe()

df2 = df.loc[1:20,['Year','Salary']].sort_values(by = 'Salary',ascending=False)
#df3 = df2.groupby('Year')
df2.plot(kind='bar')