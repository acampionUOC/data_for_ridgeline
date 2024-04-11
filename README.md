# data_for_ridgeline project
## Descripción
Este proyecto permite generar el conjunto de datos para generar la visualización en formato Ridgeline propuesta como solución a la PEC2 de la asignatura Visualización de Datos correspondiente al plan de estudios del Máster de Ciencia de Datos en la Universitat Oberta de Catalunya.
<br><br>
El proyecto contiene los siguientes ficheros:
- dataset\temp_BNC_aeropuerto_1954_2024.csv: se trata de un fichero generado por el autor del repositorio a partir de la captura manual en la web https://datosclima.es/Aemethistorico/Meteostation.php para el resultado de una consulta de las temperaturas en el aeropuerto de Barcelona entre 1-01-1954 y 1-01-2024.
<br>
<br>
- dataset\output_temp_BCN.xlsx: fichero de salida generado al ejecutar main.py con los datos para el Ridgeline plot en formato requerido por la visualización generada en Tableau Public. Se ha utilizado como plantilla la solución diseñada por Ken Flerlage disponible en https://www.flerlagetwins.com/2018/05/joy-plot.html.
<br>
<br>
- main.py: código principal para generar el dataset de salida output_temp_BCN.xlsx

<br>

La visualización resultante generada en Tableau Public se puede encontrar en el siguiente link:
https://public.tableau.com/app/profile/alvaro.campion/viz/Barcelonamintemperaturelast80years/Dashboard

## Autores
El autor del proyecto es:
- Alvaro Campion Mezquiriz (acampion@uoc.edu)

## Instalación
Clonar el repositorio para su instalación <br>

'''
git clone https://github.com/acampionUOC/data_for_ridgeline.git
'''

# Ejecución
La ejecución del código se puede hacer mediante la siguiente expresión:
<br>
'''
python main.py
'''
<br>
