import pandas as pd
import numpy as np
"""
s1 = pd.Series([33,232,232,21,44,55,66,6,66,66,6,])
print s1

s = type(s1)
print s

s2 = s1.values
print s2

s3 = type(s1.values)
print s3

s4 = s1.index
print s4
"""
# data1 = [33,232,232,21,44,55,66,]
# index1 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' ]
#
# d = pd.Series(data1,index1)
#
#
# d.name = 'Daily Temp'
# d.index.name = 'Days'
#
# print d

dict = {'Mon' : 10, 'Tue' : 20 , 'Wed' : 22 , 'Thu' : 44 ,
         'Fri' : 54 , 'Sat' : 98 , 'Sun' : 32}
dict1 = pd.Series(dict)
print dict1

b1 = np.log(dict1)
print b1