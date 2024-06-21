
import arcpy


def script_tool(fcIn, clip_features, dirOut, nameOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)  # Clase de entidad de entrada, ejemplo: grupo_socioeconomico por manzana.
    clip_features= arcpy.GetParameterAsText(1) ## Capa de recorte, ejemplo: campamentos.
    dirOut = arcpy.GetParameterAsText(2) ## Directorio de salida donde se guardará el archivo de resultado.
    nameOut = arcpy.GetParameterAsText(3) ## Nombre del archivo de salida después del recorte.

    

    script_tool(fcIn,clip_features, dirOut, nameOut, )
    arcpy.SetParameterAsText(3, "Result")



# ---------------------------------------------------


# Esta sección del código realiza operaciones específicas en el proyecto de ArcGIS.
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")

#Contenidos activos en el proyecto
# Obtener el primer mapa del proyecto actual.

aprxMap = aprx.listMaps()[0]

# Añadir las capas de entrada al mapa actual para visualizarlas.

aprxMap.addDataFromPath(fcIn)   # Añadir la clase de entidad de entrada.
aprxMap.addDataFromPath(clip_features)   # Añadir la capa de recorte.
content = []                  # Inicializar una lista para almacenar los nombres de las capas en el mapa.


n = len(aprxMap.listLayers())# Obtener y listar todas las capas actuales en el mapa.
for i in list(range(0,n)):
    content.append(aprxMap.listLayers()[i].name)

# Definir la ruta completa del archivo de salida combinando el directorio y el nombre de salida.


fcOut = f"{dirOut}\{nameOut}"



# Realizar la operación de recorte (clip) utilizando arcpy.analysis.PairwiseClip.
# Recorta 'fcIn' usando 'clip_features' y guarda el resultado en 'fcOut'.


arcpy.analysis.PairwiseClip(fcIn, clip_features, fcOut)



# Añadir el resultado del recorte al mapa actual para su visualización.

aprxMap.addDataFromPath(fcOut)
