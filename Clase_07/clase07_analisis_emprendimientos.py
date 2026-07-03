"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(lista_ventas):
    """Recibo una lista, la sumo y retorno el total."""
    return sum(lista_ventas)

def calcular_promedio(lista_ventas):
    """Retorna el promedio de las ventas de la lista de ventas"""
    return sum(lista_ventas) / len(lista_ventas)

def calcular_porcentaje(total_ventas,meta):
    """Calcule el porcentaje de cumplimiento de la meta"""
    return total_ventas / meta * 100

def calcular_clasificacion(porcentaje_logro):
    """Clasifica el emprendimiento segun porcentaje de cumplimiento de meta de ventas"""
    if porcentaje_logro >= 100:
        clasificacion_emprendimiento = "Nota alcanzada; emprendimiento rentable"
    elif porcentaje_logro >= 80:
        clasificacion_emprendimiento = "Observacion, no se logro la meta."
    else:
        clasificacion_emprendimiento = "ADVERTENCIA, problemas de rentabilidad, URGE ATENCION"
    return clasificacion_emprendimiento    

#print("Cantidad de sedes:", len(sedes))
#print(type(sedes), "vrs", type(sedes[0]))
#print("Datos por sede: ", sedes[0].keys())
#print("\nPrimer emprendimiento: ", sedes[0]["nombre"])


reporte = []
provincias = set()


for emprendimiento in sedes:
#emprendimiento = sedes[0] #Extrayendo el primer emprendimiento de la lista
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]

total_emprendimiento = calcular_total(ventas)
promedio_emprendimiento = calcular_porcentaje(total_emprendimiento, meta)
promedio_diario = total_emprendimiento / len(ventas)
clasificacion = calcular_clasificacion(promedio_emprendimiento)

provincias.add(emprendimiento["provincia"])
print("\nEmprendimiento: ", emprendimiento["nombre"])
print("Total ventas: ", total_emprendimiento)
print("Porcentaje logro:", promedio_emprendimiento)
print("Promedio diario: ", promedio_diario)
print("Analisis de emprendimiento", clasificacion)

