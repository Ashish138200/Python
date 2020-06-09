import pandas as p
#(✷‿✷)
#csv = Character Seperated Values
df1 = p.read_csv('supermarkets.csv')
#print(df1)
df2 = p.read_json('supermarkets.json')
#print(df2)
df3 = p.read_excel('supermarkets.xlsx',sheet_name=0)
#print(df3)
df4 = p.read_csv('supermarkets-commas.txt') #default value of sep(seperator) is comma
#print(df4)
df5 = p.read_csv('supermarkets-semi-colons.txt',sep=';')
#print(df5)