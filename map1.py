import folium
import pandas 

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

fg = folium.FeatureGroup(name="My Map")

def dynamic_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

for lt, ln, ele in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], 
        popup=str(ele), 
        fill=True, 
        color=dynamic_color(ele), 
        fill_color=dynamic_color(ele),
        opacity=1.0,
        fill_opacity=1.0
    ))



map.add_child(fg)

map.save("Map1.html")