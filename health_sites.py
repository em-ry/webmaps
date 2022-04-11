from turtle import fillcolor
import folium
import pandas

data = pandas.read_csv("files/nigeria.csv")

data = data.dropna(subset=["X"])
data = data.dropna(subset=["Y"])
data["speciality"].fillna("UNKNOWN",inplace=True)
data["addr_street"].fillna("UNKNOWN",inplace=True)

name = list(data["name"])
lat = list(data["X"])
lon = list(data["Y"])
specs = list(data["speciality"])
comp = list(data["completeness"])
add = list(data["addr_street"])


html="""<h4>Site Details</h4>
<strong>Name:</strong> %s <br>
<strong>Completeness:</strong> %s <br>
<strong>Speciality:</strong> %s <br>
<strong>Street:</strong> %s
"""

def color_maker(rank:int)->str:
    if rank > 19:
        return "red"
    elif 12 <= rank <= 19:
        return "blue"
    else:
        return "yellow" 

fea = folium.FeatureGroup(name="health sites")
map= folium.Map(location=(9.0820,8.6753),tiles="Stamen Terrain", zoom_start=7)


for nm, cm, sp, st, lt, ln in zip(name, comp, specs, add, lat, lon):
    iframe = folium.IFrame(html=html % (nm,cm,sp,st), width=200, height=150)
    fea.add_child(folium.CircleMarker(location=(lt,ln), popup=folium.Popup(iframe), 
    fill_color= color_maker(cm), radius= 6, color = "grey", fill_opacity= 1))

map.add_child(fea)
map.add_child(folium.LayerControl())
map.save("health_sites.html")