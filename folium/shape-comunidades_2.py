import geopandas as gpd
import folium
import webbrowser
from folium.plugins import MarkerCluster
from folium.plugins import Search

ruta_shape = "./Data/Comunidades Campesinas Minagri geogpsperu juansuyo/Comunidades Campesinas Minagri geogpsperu juansuyo.shp"

# Cargando shapefile
comunidades=gpd.read_file(ruta_shape)

comunidades.to_file("comunidades.geojson", driver="GeoJSON")
comunidadesGeoJson = gpd.read_file("comunidades.geojson", driver="GeoJSON")

mymap = folium.Map(
    location=[-11.005714, -76.108739],
    zoom_start=5,
    tiles="OpenStreetMap"
)

geoPath = comunidades.geometry.to_json()
points = folium.features.GeoJson(geoPath)
#mymap.add_child(points)

comunidadesFolium = folium.GeoJson(
    comunidadesGeoJson,
    name="Comunidades"
).add_to(mymap)

comunidadsearch = Search(
    layer=comunidadesFolium,
    geom_type="Polygon",
    placeholder="Buscar comunidad",
    collapsed=False,
    search_label="nom_comuni"
).add_to(mymap)

popups, locations = [], []

def SetLocations(comunidad):
    
    coordenada_x = comunidad[1].geometry.centroid.x
    coordenada_y = comunidad[1].geometry.centroid.y
    return [coordenada_y,coordenada_x]

def SetPopups(comunidad):
    nombreComunidad = str(comunidad[1].nom_comuni)
    nombreComunidad = nombreComunidad.replace("'"," ")
    nombreComunidad = nombreComunidad.replace("`"," ")
    return nombreComunidad

popups = list(map(SetPopups, comunidades.iterrows()))

locations = list(map(SetLocations, comunidades.iterrows()))

feature_group = folium.FeatureGroup(name="Comunidades campesinas")
MarkerCluster(locations=locations, popups=popups).add_to(feature_group)
mymap.add_child(feature_group)

mymap.add_child(folium.map.LayerControl())

mymap.save("Mapas/shape-comunidades_2.html")