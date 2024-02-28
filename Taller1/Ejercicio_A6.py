import math

def calcular_fuerza_avance(presion, radio_superior):
    area_avance = math.pi * radio_superior**2
    fuerza_avance = presion * area_avance
    return fuerza_avance

def calcular_fuerza_retroceso(presion, radio_superior, radio_inferior):
    area_retroceso = math.pi * (radio_superior**2 - radio_inferior**2)
    fuerza_retroceso = presion * area_retroceso
    return fuerza_retroceso

presion = float(input("Ingrese la presión en el cilindro (en Pascal): "))
radio_superior = float(input("Ingrese el radio superior del cilindro (en metros): "))
radio_inferior = float(input("Ingrese el radio inferior del cilindro (en metros): "))

#fuerzas
fuerza_avance = calcular_fuerza_avance(presion, radio_superior)
fuerza_retroceso = calcular_fuerza_retroceso(presion, radio_superior, radio_inferior)

print(f"Fuerza de avance: {fuerza_avance} Newtons")
print(f"Fuerza de retroceso: {fuerza_retroceso} Newtons")