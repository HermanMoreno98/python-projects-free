import geopandas as gpd
import folium
import webbrowser

# Mapa
mymap = folium.Map(
    location=[-11.005714, -76.108739],
    zoom_start=8,
    tiles="OpenStreetMap"
)

ruta_shape = "./Data/Comunidades Campesinas Minagri geogpsperu juansuyo/Comunidades Campesinas Minagri geogpsperu juansuyo.shp"

# Cargando shapefile
comunidades=gpd.read_file(ruta_shape)

print("Tipo de dato")
print(type(comunidades))

print("Columnas del shape")
print(comunidades.columns)

print("Geoseries")
print(type(comunidades.geometry))

geoPath = comunidades.geometry.to_json()
poligonos = folium.features.GeoJson(geoPath)
mymap.add_child(poligonos)

# Añadir controles
mymap.add_child(folium.map.LayerControl())
# Guardar
mymap.save("Mapas/shape-comunidades.html")
# Abrir en el navegador
webbrowser.open("Mapas/shape-comunidades.html")

