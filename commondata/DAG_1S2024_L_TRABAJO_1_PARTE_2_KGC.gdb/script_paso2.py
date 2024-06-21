
import arcpy               # Importa el módulo arcpy necesario para las herramientas de geoprocesamiento de ArcGIS.


def script_tool(fcIn, dirOut, nameOut):
    """Script code goes below"""

    return

 # Obtener los parámetros de entrada desde la interfaz de ArcGIS.
if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)   # Clase de entidad de entrada.
    dirOut = arcpy.GetParameterAsText(1) ## Directorio donde se guardará el archivo de salida.
    nameOut= arcpy.GetParameterAsText(2)  # Nombre del archivo de salida.

     # Llamar a la función principal script_tool con los parámetros obtenidos.

    script_tool(fcIn, dirOut, nameOut)


     # Establecer un parámetro de salida (en este caso, "Result" es un marcador de posición).

    arcpy.SetParameterAsText(2, "Result")

  #Entorno
#    # Definir el proyecto actual de ArcGIS.
aprx = arcpy.mp.ArcGISProject("CURRENT")


    # Obtener el primer mapa del proyecto actual.


aprxMap = aprx.listMaps()[0]



    # Añadir la clase de entidad de entrada al mapa para su visualización

aprxMap.addDataFromPath(fcIn)


 # Inicializar una lista para almacenar los nombres de las capas.

content = []


# Añadir el nombre de la primera capa del mapa a la lista de contenido.

content.append(aprxMap.listLayers()[0].name)


# Definir la ruta completa para el archivo de salida combinando el directorio de salida y el nombre del archivo.

fcOut = f"{dirOut}\{nameOut}"

# Realizar la exportación de características usando una consulta 'where_clause' para seleccionar solo los registros donde "Posibles = 1".


arcpy.conversion.ExportFeatures(fcIn, fcOut, where_clause="Posibles = 1")


# Añadir el resultado exportado al mapa actual para que el usuario pueda visualizarlo.

aprxMap.addDataFromPath(fcOut)

