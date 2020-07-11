#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:36:09 2020

@author: jm
"""

#%% required libraries
import geopandas as gpd
import matplotlib.pyplot as plt

import folium
#from osgeo import gdal,ogr
#from folium import Choropleth, Circle, Marker
#from folium.plugins import HeatMap, MarkerCluster


#%% read data
df = gpd.read_file("data/proyectos-mineros-ubicacin-aproximada-/proyectos-mineros-ubicacin-aproximada--shp.shp", encoding = 'utf-8')
pais = gpd.read_file("data/gadm36_ARG_shp/gadm36_ARG_1.shp", encoding = 'utf-8') 

type(df)
print(df.crs)
print(pais.crs) # check coordinate reference system (CRS)
pais.crs

#%% explore data
df.shape
df.head()
df.columns
df.geometry.head()
df.info()

df.TIPO_YACIM.value_counts()
df[['TIPO_YACIM']]
df.ESTADO.value_counts()
df.MINERAL_PR.value_counts()
df.EMPRESA.value_counts()

centroid = df[['geometry']].centroid
type(centroid)
    
for index, row in df.iterrows():
    print(row['NOMBRE'], "-", row['EMPRESA'])


#%% cambiar algunos valores en la variable 'ESTADO'
df.loc[df.ESTADO == "Exploración avanzada", 'ESTADO'] = 'Exp avanzada'
df.loc[df.ESTADO == "Evaluación económica previa", 'ESTADO'] = 'Ev econ previa'
df.loc[df.ESTADO == "Proceso de Cierre", 'ESTADO'] = 'Proc cierre'


#%% first plot
df.plot(column = 'MINERAL_PR', legend = True)


#%% some groups by mineral
df.iloc[75, 4] = 'Carbon'
carbon = df[df['MINERAL_PR'] == 'Carbon']
cobre = df[df['MINERAL_PR'] == 'Cobre']
hierro = df[df['MINERAL_PR'] == 'Hierro']
litio = df[df['MINERAL_PR'] == 'Litio']
oro = df[df['MINERAL_PR'] == 'Oro']
plata = df[df['MINERAL_PR'] == 'Plata']
plomo = df[df['MINERAL_PR'] == 'Plomo']
potasio = df[df['MINERAL_PR'] == 'Potasio']
uranio = df[df['MINERAL_PR'] == 'Uranio']

#otros = df[~df['MINERAL_PR'].isin(['Oro', 'Plata', 'Uranio'])]



#%% some groups by estado
exp_avanzada = df[df['ESTADO'] == 'Exp avanzada']
ev_econ_previa = df[df['ESTADO'] == 'Ev econ previa']
produccion = df[df['ESTADO'] == 'Producción']
factibilidad = df[df['ESTADO'] == 'Factibilidad']
prefactibilidad = df[df['ESTADO'] == 'Prefactibilidad']
mantenimiento = df[df['ESTADO'] == 'Mantenimiento']
construccion = df[df['ESTADO'] == 'Construcción']
proc_cierre = df[df['ESTADO'] == 'Proc cierre']
reingenieria = df[df['ESTADO'] == 'Reingeniería']




#%% complete map
# define a base map with province boundaries
ax = pais.plot(figsize = (10, 10), color = 'none', edgecolor = 'black')

# set axis labels and title
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title('Proyectos mineros en Argentina')
              
# add proyectos mineros
oro.plot(color = 'gold', ax = ax, label = 'Oro')
plata.plot(color = 'grey', ax = ax, label = 'Plata')
uranio.plot(color = 'lightgreen', ax = ax, label = 'Uranio')
plt.legend(loc = 'lower right')



#%% complete map 2
# define a base map with province boundaries
ax = pais.plot(figsize = (10, 10), color = 'none', edgecolor = 'black')

# set axis labels and title
ax.set_xlabel("Longitud")
ax.set_ylabel("Latitud")
ax.set_title('Proyectos mineros en Argentina')

# add proyectos mineros
carbon.plot(color = 'black', ax = ax, label = 'Carbon')
cobre.plot(color = 'brown', ax = ax, label = 'Cobre')
hierro.plot(color = 'red', ax = ax, label = 'Hierro')
litio.plot(color = 'blue', ax = ax, label = 'Litio')
oro.plot(color = 'gold', ax = ax, label = 'Oro')
plata.plot(color = 'grey', ax = ax, label = 'Plata')
plomo.plot(color = 'darkslategrey', ax = ax, label = 'Plomo')
potasio.plot(color = 'green', ax = ax, label = 'Potasio')
uranio.plot(color = 'lawngreen', ax = ax, label = 'Uranio')

# add legend
plt.legend(loc = 'lower right')


#%% complete map 3
# define a base map with province boundaries
fig, ax = plt.subplots(1, 2, sharey = True)
#ax[0] = pais.plot(color = 'none', edgecolor = 'black', figsize = (10, 10))
pais.plot(color = 'none', edgecolor = 'black', ax = ax[0], figsize = (3, 10))

# set axis labels and title
ax[0].set_xlabel("Longitud")
ax[0].set_ylabel("Latitud")
ax[0].set_title('Proyectos mineros en Argentina')

# MINERAL
# add proyectos mineros
carbon.plot(color = 'black', ax = ax[0], label = 'Carbón', markersize = 5)
cobre.plot(color = 'brown', ax = ax[0], label = 'Cobre', markersize = 5)
hierro.plot(color = 'red', ax = ax[0], label = 'Hierro', markersize = 5)
litio.plot(color = 'blue', ax = ax[0], label = 'Litio', markersize = 5)
oro.plot(color = 'gold', ax = ax[0], label = 'Oro', markersize = 5)
plata.plot(color = 'grey', ax = ax[0], label = 'Plata', markersize = 5)
plomo.plot(color = 'darkslategrey', ax = ax[0], label = 'Plomo', markersize = 5)
potasio.plot(color = 'green', ax = ax[0], label = 'Potasio', markersize = 5)
uranio.plot(color = 'lawngreen', ax = ax[0], label = 'Uranio', markersize = 5)

# add legend
ax[0].legend(loc = 'lower right', title = 'Mineral')

# ESTADO
# define a base map with province boundaries
#ax[1] = pais.plot(color = 'none', edgecolor = 'black', figsize = (10, 10))
pais.plot(color = 'none', edgecolor = 'black', ax = ax[1], figsize = (3, 10))

# set axis labels and title
ax[1].set_xlabel("Longitud")

# add estado
exp_avanzada.plot(color = 'black', ax = ax[1], label = 'Exp avanzada', markersize = 5)
ev_econ_previa.plot(color = 'brown', ax = ax[1], label = 'Ev econ previa', markersize = 5)
produccion.plot(color = 'red', ax = ax[1], label = 'Produccion', markersize = 5)
factibilidad.plot(color = 'blue', ax = ax[1], label = 'Factibilidad', markersize = 5)
prefactibilidad.plot(color = 'gold', ax = ax[1], label = 'Prefactibilidad', markersize = 5)
mantenimiento.plot(color = 'grey', ax = ax[1], label = 'Mantenimiento', markersize = 5)
construccion.plot(color = 'darkslategrey', ax = ax[1], label = 'Construccion', markersize = 5)
proc_cierre.plot(color = 'green', ax = ax[1], label = 'Proc cierre', markersize = 5)
reingenieria.plot(color = 'lawngreen', ax = ax[1], label = 'Reingenieria', markersize = 5)

# add legend
ax[1].legend(loc = 'lower right', title = 'Estado')


#%% interactive map
# create base map
m_1 = folium.Map(location = [-36.287771, -64.406169], tiles = 'openstreetmap', zoom_start = 4)

# add an additional tile layer
folium.TileLayer('openstreetmap').add_to(m_1)
folium.TileLayer('Stamen Terrain').add_to(m_1)
folium.TileLayer('stamentoner').add_to(m_1)

#folium.GeoJson(oro.geometry).add_to(m_1)

# other mapping code (e.g. lines, markers etc.)
folium.LayerControl().add_to(m_1)

# save the map
m_1.save("map.html")



#%% pandas geoseries 
type(pais['geometry'])

pais['geometry'].area
pais_3857 = pais.to_crs(epsg = 3857)
pais_3857['geometry'].area

# define a variable for m^2 to km^2
sqm_to_sqkm = 10**6

# get area in kilometers squared
pais_area_km = pais_3857.geometry.area / sqm_to_sqkm




