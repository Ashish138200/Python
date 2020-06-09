import pandas as p
#(✷‿✷)
df = p.read_csv('supermarkets-commas.txt')
#------------------------------------Deleting---------------------------------------------------------------------------
df = df.drop("City",1)
#df.drop(df.columns[0:3],0) #for deleting column
df.drop(df.index[0:3],0) # for deleting index
df.columns #for getting columns
#print(df)

#------------------------------------------Adding columns---------------------------------------------------------------
#df["Continent"]=["Asia","North America","South America","Europe","Antartica","Africa"]
df["Continent"]=df.shape[0]*["North America"]
#print(df.shape[0])

#-------------------------------------------Modifying-------------------------------------------------------------------
df["Continent"] = df["Country"]+","+"North America"
#print(df)
df_T = df.T
print(df_T)