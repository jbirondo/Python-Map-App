import folium
import pandas 

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

fg = folium.FeatureGroup(name="My Map")

for lt, ln, ele in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=ele, icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")