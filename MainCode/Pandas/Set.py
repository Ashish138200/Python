import pandas as p
#(✷‿✷)
#df = p.read_csv('supermarkets-commas.txt',header=None)
df = p.read_csv('supermarkets-commas.txt')
#df.columns = ['ID','Address','City','Zip','Country','Name','Employees'] #add columns header
#print(df)
#----------------------------To extract a particular value from the table-----------------------------------------------
#df1 = df.set_index("ID",inplace=True)
#df.set_index("ID",inplace=True)
df.set_index("Name",inplace=True,drop=False)
print(df)