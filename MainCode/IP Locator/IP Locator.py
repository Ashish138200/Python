import requests
import folium
res = requests.get('https://ipinfo.io/')
data = res.json()
l = list(data.values())
print("Your IP is: ",l[0])
print("City: ",l[1])
print("State: ",l[2])
print("Country: ",l[3])
print("Your Service Provider: ",l[5])
location = data['loc'].split(',')
lat = float(location[0])
log = float(location[1])
fg = folium.FeatureGroup('my map')
fg.add_child(folium.GeoJson(data=(open('india_states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[lat,log],popup="This is my location"))

map = folium.Map(location=[lat,log],zoom_start=7)

map.add_child(fg)
map.save("mylocation.html")