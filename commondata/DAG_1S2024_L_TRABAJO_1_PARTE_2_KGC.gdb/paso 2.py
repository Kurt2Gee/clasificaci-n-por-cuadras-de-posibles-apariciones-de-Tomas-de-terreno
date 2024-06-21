import arcpy

 # """Función principal del script que realiza la operación de cálculo del campo."""
def script_tool(fcIn, field):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)   # Obtener los parámetros de entrada desde la interfaz de ArcGIS. \\  fcIn: Clase de entidad (feature class) de entrada.
    field = arcpy.GetParameterAsText(1) # field -- Nombre del campo donde se almacenará el resultado del cálculo.
    

    script_tool(fcIn, field)                  # Llamar a la función principal script_tool con los parámetros obtenidos.
    arcpy.SetParameterAsText(1, "Result")     # Establecer el parámetro de salida. En este caso, solo se utiliza para completar el script.


    #-----------------------------------------

 
expression = "indice(!Hacinamiento!, !GSE!)"          # Expresión que llama a la función 'indice' pasando los valores de 'Hacinamiento' y 'GSE'.
expression_type = "PYTHON3"



 # Bloque de código que define la lógica de la función 'indice' para el cálculo.

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
 # Nota: Este código asume que los campos 'Hacinamiento' y 'GSE' ya existen en la clase de entidad.
#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")

 # Obtener el primer mapa del proyecto actual.

aprxMap = aprx.listMaps()[0]

 # Añadir la clase de entidad de entrada (fcIn) al mapa.
aprxMap.addDataFromPath(fcIn)

# Listar el contenido actual del mapa.
content = []
content.append(aprxMap.listLayers()[0].name)
#Entorno
#Definir entorno

aprx = arcpy.mp.ArcGISProject("CURRENT")




   # Llamar a la función 'CalculateField' para calcular el nuevo valor del campo.

   
arcpy.management.CalculateField(fcIn, field, expression, expression_type, code_block)
