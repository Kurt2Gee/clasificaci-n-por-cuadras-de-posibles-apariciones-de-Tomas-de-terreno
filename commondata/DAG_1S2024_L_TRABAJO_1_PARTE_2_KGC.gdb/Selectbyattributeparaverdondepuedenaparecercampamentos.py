
import arcpy              


def script_tool(fcIn, dirOut, nameOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)   
    dirOut = arcpy.GetParameterAsText(1) 
    nameOut= arcpy.GetParameterAsText(2)  


    script_tool(fcIn, dirOut, nameOut)



    arcpy.SetParameterAsText(2, "Result")

aprx = arcpy.mp.ArcGISProject("CURRENT")



aprxMap = aprx.listMaps()[0]




aprxMap.addDataFromPath(fcIn)



content = []



content.append(aprxMap.listLayers()[0].name)


where_clause = "Posibles = '1'"

fcOut = f"{dirOut}\\{nameOut}"



arcpy.conversion.ExportFeatures(fcIn, fcOut, where_clause)



aprxMap.addDataFromPath(fcOut)