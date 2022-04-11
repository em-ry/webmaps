import folium
import pandas

data = pandas.read_csv("download.txt")
cases = list(data["cases"])
deaths = list(data["deaths"])
date = list(data["dateRep"])
con_and_ter = list(data["countriesAndTerritories"])

country = pandas.read_csv("country.csv")
lat = list(country["latitude"])
lon = list(country["longitude"])
name = list(country["name"])
print(len(name))
print(len(set(con_and_ter)))


map = folium.Map(location= [23.424,53.847], zoom_start=6, tiles= "Stamen Terrain")
marker = folium.FeatureGroup(name= "covid")

#for lt, ln, name in  zip(lat, lon, name):
 #       marker.add_child(folium.Marker(location= [lt, ln], popup= name, icon= folium.Icon(color= "red")))
        
    

map.add_child(marker)
map.save("covid19.html")