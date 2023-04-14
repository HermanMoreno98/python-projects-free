import pandas as pd
import folium
import webbrowser
from folium.plugins import MarkerCluster

mymap = folium.Map(
    location=[-6.477905555555556, -76.37866],
    zoom_start=5,
    titles="OpenStreetMap"
)

url_file = "./Data/datalogger_yx.csv"
puntos = pd.read_csv(url_file)
puntos.rename(columns={
    "y":"latitud",
    "x":"longitud"
},inplace=True)
puntos = puntos[["latitud","longitud","station"]]

def recode(x):
    if x < 10:
        return "Primero"
    elif x >= 10 and x <=20:
        return "Segundo"
    else:
        return "Tercero"

puntos["categoria"] = puntos["station"].apply(recode)

latitudes = puntos["latitud"].tolist()
longitudes = puntos["longitud"].tolist()
popups = puntos["station"].tolist()

locations = []

# Para manejar n colecciones a la vez
for lat, lon in zip(latitudes,longitudes):
    fLat = float(lat)
    fLon = float(lon)
    locations.append([lat,lon])
    
# Creacion objecto espacial
feature_group = folium.FeatureGroup(name="Estaciones")
marcadores = MarkerCluster(locations=locations, popups=popups)
marcadores.add_to(feature_group)

mymap.add_child(feature_group)
# Añadir controles
mymap.add_child(folium.map.LayerControl())
# Guardar
mymap.save("Mapas/marcadores.html")
# Abrir en el navegador
webbrowser.open("Mapas/marcadores.html")


