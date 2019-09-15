# dashboard-project-airline
Prueba técnica para trabajo en aerolinea, exigen que no se use tableau ni similares. Se hará con **plotly** y **dash**. 

## instructions

In this Technical Test we are looking for something simple that shows your skills. 

You will find the following instructions:

**Goal**: Visualize a data set on an attractive and interactive dashboard that allows users to explore data in an easy manner and to find the most important insights extracted from data.

**Tech stack**: Up to the candidate

**Deadline**: the results should be delivered within 1 week from receiving the exercise.

**Dataset description**: The file contains a list of scheduled flights between the 24th July 2017 and 30th July 2017. Meaning of the columns:

* Id - a unique identifier of a flight
* Date - a scheduled date of departure
* Dep - IATA code of a departure airport
* Dep_time - UTC scheduled time of departure
* Dep_local_time – scheduled time of departure in the airport local timezone
* Arr - IATA code of an arrival airport
* Arr_time - UTC scheduled time of arrival
* Arr_local_time – scheduled time of arrival in the airport local timezone
* BaseIataCode - base of an aircraft serving the flight
* LOF_ID - line of flight identifier, line of flight is a daily route of an aircraft



## requirements

Para ejecutar el proyecto hay que instalar las dependencias que se encuentran en el fichero `requirements.txt`. Por ejemplo con pip: 

```
$ pip3 install -r requirements.txt
```


## additional data from IATA database

Para enriquecer el dataset con las longitudes y latitudes de los aeropuertos se consume el siguiente recurso. Más adelante se podrían emplear para visualizaciones geográficas con `folium` en mejorar futuras. 

https://www.partow.net/miscellaneous/airportdatabase/

## Files
 
* app.py: despliega el dashboard
* assets/style.css: hoja de estilo
* graphics.py: contiene 4 ejemplos de plots interactivos que se podrían incluir en un dashboard real
* requirements.txt: contiene las dependencias de python para este proyecto que se pueden instalar en un entorno virtual. 
* pipe.py: creación del dataframe con los datos
* input: contiene los datasets empleados. 
* test.ipynb: contine los test de enriquecimiento y consumo de datasets

## Start app

Para iniciar la visualización ejecutar el siguiente comando, previamente instaladas las dependencias. 

```
$ python3 app.py
```

La consola nos mostrará una URL local a la que acceder para abrir la visualización en el navegador

```
Running on http://127.0.0.1:8050/
```

## Next Steps

1. Incluir `callbacks` para mejorar la interactividad
2. Uso de visualización geoespacial para hacer uso de la base de datos importada o una API. 
3. Incluir branding de la empresa. 


