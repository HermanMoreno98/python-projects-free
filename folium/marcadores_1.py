import pandas as pd
import folium
import webbrowser
#from folium.plugins import MarkerCluster

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
popups = puntos["categoria"].tolist()


feature_group = folium.FeatureGroup(name="Estaciones")

# Para manejar n colecciones a la vez
for lat, lon, tag in zip(latitudes,longitudes, popups):
    fLat = float(lat)
    fLon = float(lon)
    if tag=="Primero":
        folium.Marker(location=[fLat,fLon],
                      popup=tag,
                      icon=folium.Icon(color="blue",
                                       icon="cloud")).add_to(feature_group)
    elif tag=="Segundo":
        folium.Marker(location=[fLat,fLon],
                      popup=tag,
                      icon=folium.Icon(color="red",
                                       icon="info-sign")).add_to(feature_group)    
    else:
        folium.Marker(location=[fLat,fLon],
                      popup=tag,
                      icon=folium.Icon(color="purple",
                                       icon="road")).add_to(feature_group)

mymap.add_child(feature_group)

# Añadir controles
mymap.add_child(folium.map.LayerControl())
# Guardar
mymap.save("Mapas/marcadores_1.html")
# Abrir en el navegador
webbrowser.open("Mapas/marcadores_1.html")


