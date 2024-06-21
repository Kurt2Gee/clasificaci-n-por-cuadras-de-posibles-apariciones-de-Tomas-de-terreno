import arcpy


def script_tool(fcIn, clip_features, dirOut, nameOut):
 
    """Script code goes below"""


fcIn = arcpy.GetParameterAsText(0) #grupo_socioeconomico por manzana
clip_features= arcpy.GetParameterAsText(1)
dirOut = arcpy.GetParameterAsText(2) #directorio
nameOut = arcpy.GetParameterAsText(3) #nombre de clip

script_tool(fcIn,clip_features, dirOut, nameOut, )
arcpy.SetParameterAsText(3, "Result")

#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")

#Definir salida
fcOut = f"{dirOut}\\{nameOut}"


#Contenidos activos en el proyecto
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn)
aprxMap.addDataFromPath(clip_features)
content = []
n = len(aprxMap.listLayers())
for i in list(range(0,n)):
    content.append(aprxMap.listLayers()[i].name)

script_tool(fcIn,clip_features, dirOut, nameOut, )
arcpy.SetParameterAsText(3, "Result")

arcpy.analysis.PairwiseClip(content[1], content[0], fcOut)

aprxMap.addDataFromPath(fcOut)