"""libreria JSON"""
import json

Jasondata = { "nombre" , "Python" , "tipo" , "backend","paradigma","PDO"}

JasonToPython = json.loads(Jasondata)

print("nuestros datos son:{}".format(JasonToPython))
