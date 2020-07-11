#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:36:09 2020

@author: jm
"""

#%% required libraries
import geopandas as gpd
import matplotlib.pyplot as plt


#%% read data
df = gpd.read_file("data/proyectos-mineros-ubicacin-aproximada-/proyectos-mineros-ubicacin-aproximada--shp.shp", encoding = 'utf-8')
pais = gpd.read_file("data/gadm36_ARG_shp/gadm36_ARG_1.shp", encoding = 'utf-8') 


#%% explore data
df.info()
df.ESTADO.value_counts()
df.MINERAL_PR.value_counts()


#%% change too long values in 'ESTADO'
df.loc[df.ESTADO == "Exploración avanzada", 'ESTADO'] = 'Exp avanzada'
df.loc[df.ESTADO == "Evaluación económica previa", 'ESTADO'] = 'Ev econ previa'
df.loc[df.ESTADO == "Proceso de Cierre", 'ESTADO'] = 'Proc cierre'

   
#%% group and summarize data
nr_estado = df.groupby('ESTADO')['ESTADO'].count().sort_values(ascending = False)
nr_mineral = df.groupby('MINERAL_PR')['MINERAL_PR'].count().sort_values(ascending = False)

#%% bar plot
# figure and axis
fig, ax = plt.subplots(1, 2, sharey = True)

# MINERAL_PR
nr_mineral.plot(kind = 'bar', rot = '45', ax = ax[0])
ax[0].set_xlabel("Mineral")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title('Grafico de barras por \n tipo de mineral')
ax[0].set_axisbelow(True)
ax[0].grid(color = 'gray', linestyle = 'dashed')

# ESTADO
nr_estado.plot(kind = 'bar', ax = ax[1])
ax[1].set_xlabel("Estado del yacimiento")
ax[1].set_title('Grafico de barras por \n estado del yacimiento')
ax[1].set_axisbelow(True)
ax[1].grid(color = 'gray', linestyle = 'dashed')
plt.show()


#%% subsets of the data by mineral
carbon = df[df['MINERAL_PR'] == 'Carbón']
cobre = df[df['MINERAL_PR'] == 'Cobre']
hierro = df[df['MINERAL_PR'] == 'Hierro']
litio = df[df['MINERAL_PR'] == 'Litio']
oro = df[df['MINERAL_PR'] == 'Oro']
plata = df[df['MINERAL_PR'] == 'Plata']
plomo = df[df['MINERAL_PR'] == 'Plomo']
potasio = df[df['MINERAL_PR'] == 'Potasio']
uranio = df[df['MINERAL_PR'] == 'Uranio']

# mapa completo
# definir un mapa base con limites interprovinciales
ax = pais.plot(figsize = (10, 10), color = 'none', edgecolor = 'black')

# definir los nombres de los ejes y el titulo
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.title('Proyectos mineros en Argentina')

# agregar los proyectos mineros segun tipo de mineral
carbon.plot(color = 'black', ax = ax, label = 'Carbón')
cobre.plot(color = 'brown', ax = ax, label = 'Cobre')
hierro.plot(color = 'red', ax = ax, label = 'Hierro')
litio.plot(color = 'blue', ax = ax, label = 'Litio')
oro.plot(color = 'gold', ax = ax, label = 'Oro')
plata.plot(color = 'grey', ax = ax, label = 'Plata')
plomo.plot(color = 'darkslategrey', ax = ax, label = 'Plomo')
potasio.plot(color = 'green', ax = ax, label = 'Potasio')
uranio.plot(color = 'lawngreen', ax = ax, label = 'Uranio')

# agregar leyenda
ax.legend(loc = 'lower right')
