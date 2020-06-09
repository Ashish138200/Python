import pandas as p
#(✷‿✷)
df1 = p.DataFrame([[2,4,6],[10,20,30]])
#print(df1)
'''
Rows-   0   1   2
Indexes    
0       2   4   6
1       10  20  30
'''
#You can have your own columns & index names

df2 = p.DataFrame([[2,4,6],[10,20,30]],columns=['Price','Age','Values'],index=['First','Second']) #using list
#print(df2)

df3 = p.DataFrame([{"Name":'John','Surname':'K'},{"Name":'Jack','Surname':'Z'}]) #Using dictionaries
#print(df3)

#----------------------------------------Data Analysis------------------------------------------------------------------
#print(type(df1))

#print(dir(df1))

#print(df1.mean()) #mean of all the columns

#print(df1.mean().mean()) # mean of whole dataFrame at once

#print(df2.Price.mean())