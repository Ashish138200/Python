import pandas as p
#(✷‿✷)
df = p.read_csv('supermarkets-commas.txt')
df.set_index("Address",inplace=True,drop=False)
k = df.loc["735 Dolores St":"332 Hill St","Country":"ID"]
c= df.loc[:,"Country"]
#print(c)

#------------------------------------------------Indexing---------------------------------------------------------------
i = df.iloc[1:3,1:3]
print(i)