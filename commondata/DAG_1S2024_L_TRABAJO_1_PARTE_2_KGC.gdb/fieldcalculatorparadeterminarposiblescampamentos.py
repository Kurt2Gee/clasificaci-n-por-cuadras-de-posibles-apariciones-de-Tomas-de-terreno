import arcpy


def script_tool(fcIn, field):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)
    field = arcpy.GetParameterAsText(1)

    script_tool(fcIn, field)
    arcpy.SetParameterAsText(1, "Result")


    #-----------------------------------------

 
expression = "indice(!Hacinamiento!, !GSE!)"
expression_type = "PYTHON3"
code_block = """
def indice(x, y):
    if x == "Desconocido" and y == 0:
        return 1
    elif x == "Hacinamiento Leve" and y == 3:
        return 1
    elif x == "Hacinamiento Medio" and y == 5:
        return 1
    elif x == "Hacinamiento Leve" and y == 4:
        return 1
    elif x == "Hacinamiento Leve" and y == 5:
        return 1
    else:
        return 0
"""

#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")

aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn)
content = []
content.append(aprxMap.listLayers()[0].name)
#Entorno
#Definir entorno





# Now call CalculateField with all parameters correctly
arcpy.management.CalculateField(fcIn, field, expression, expression_type, code_block)