import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """<h4>Volcano Information:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
height:%s m"""

def color_maker(elevation:float)->str:
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "blue"
    else:
        return "red"

map = folium.Map(location=[73,-100],zoom_start=3, tiles="Stamen Terrain")
figv = folium.FeatureGroup(name="Volcanoes")#for marker layer
figp = folium.FeatureGroup(name="Population")#for population layer

for lt, ln, el, name in zip(lat,lon, elev, name):
    #the folium.IFrame allows me to pass more info to the popup
    iframe = folium.IFrame(html = html % (name,name,el), width = 200, height= 100)
    figv.add_child(folium.CircleMarker(location=[lt,ln],radius= 6, popup=folium.Popup(iframe), fill_color=color_maker(el),color = "grey",fill_opacity=1))
    #I diffrentiate the volcanoes based on their elev heights with diff colors by making a func that returns a color to the icon plugin. 

#this adds another layer to the map called 'polygons' which can be used to represent populations of countries by colors.
# we put this in a seperate featuregroup for better layer control
figp.add_child(folium.GeoJson(data = open("world.json","r", encoding="utf-8-sig").read(),
#the new folium doesn't accept files anymore(produced by open()), but strings which the .read() method does
 style_function= lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 
 else "orange" if 10000000 <= x["properties"]["POP2005"] <20000000 else "red"} ))


# add_child is used to add any property to the map object or featuregroup.
map.add_child(figp)
map.add_child(figv)

# so after the featuregroup has been loaded unto the map object, a special method called LayerControl can be attached to the map object.
# this allows a user to manipulate the layers such that certain layers can be switched on/off.
map.add_child(folium.LayerControl())


map.save("population_layer.html")