from geopy.geocoders import Nominatim
import pandas as p

nom = Nominatim()
#k = nom.geocode("3995 23rd St, San Francisco, CA 94114")
#print(k.latitude)
df = p.read_csv('supermarkets.csv')
df["Address"]=df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]
df["Coordinates"] = df["Address"].apply(nom.geocode)
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude)
#print(df.Coordinates[0])
print(df)

