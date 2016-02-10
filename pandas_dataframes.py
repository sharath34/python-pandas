import pandas as pd
import datetime
"""
dt = datetime.datetime(2013,12,1)
end = datetime.datetime(2013,12,8)
step = datetime.timedelta(days=1)
dates = []

while dt < end :
    dates.append(dt.strftime('%m-%d'))
    dt += step

print dates

d = {'Date' : dates , 'Mumbai': [12,10,33,43,23,21,66] ,
     'Paris': [22,6,44,53,24,11,54] , 'Tokyo': [24,56,78,65,44,31,14]}
print d

df = pd.DataFrame(d)
print df
print df.Mumbai

df = df.set_index('Date')
print df

titanic = pd.read_csv('data/titanic.csv')

# print titanic.head()

# print titanic.Sex.value_counts()

"""

medals = pd.read_csv('data/olympicmedals.csv')

# print medals.City.value_counts()

# print medals.head()

x = medals.NOC.value_counts()

print x