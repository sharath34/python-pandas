import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mlb = pd.read_csv('data/mlbsalaries.csv')

# print mlb.Team.value_counts()

# print mlb.Position.value_counts()

yr2010 =  mlb[mlb.Year == 2010]

yr2010 = yr2010.set_index('Player')
"""
 print yr2010.head()

 print yr2010.sort_index().head()

# sort the column names
print yr2010.sort_index(axis= 1).head()

# sort on salary column
print yr2010.Salary.sort_values(ascending=False).head()
print yr2010.Salary.sort_values(ascending=False).head()

# sort on column salary and get the dataframe
srt_yr2010 = yr2010.sort_index(ascending=False, by = ['Salary'])

print srt_yr2010.head(20)

# Sorting by two columns
srt_yr2010 = yr2010.sort_index(ascending=[False,True],
                               by = ['Salary','Team'])

print srt_yr2010.head(20)
#plot

top10 = yr2010.Salary.sort_values(ascending=False).head(10)

#print type(top10)

plt.figure()
top10.plot(label ='Salaries')
plt.xticks(rotation = 'vertical')
plt.legend()
plt.show()

"""
top10 = yr2010.Salary.sort_values(ascending=False).head(10)

print top10

player = top10.index
name = top10
y_pos = np.arange(len(name))
plt.barh(y_pos,name,align='center', alpha=0.4)
plt.yticks(y_pos,name)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')
plt.show()