import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def colorProducer(elev):
    if elev < 2000:
        return "green"
    elif elev > 2000 and elev < 3000:
        return "orange"
    else:
        return "red"

html = """<h4>Volcano Information:</h4>
height = %s m
<p>More Info at: </p>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""
map = folium.Map(location=[39, -99], zoom_start=6, tiles="Stamen Terrain")
# fg = FeatureGroup
fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html = html % (str(el), name, name), width = 200, height = 200)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 10, popup = folium.Popup(iframe), fill_color = colorProducer(el), fill = True, fill_opacity = 0.7, color = "grey"))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding='UTF-8-sig').read(),style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")