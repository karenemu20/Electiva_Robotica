def fuerza_retroceso(presion, area, longitud):
    fuerza_avance = presion * area
    fuerza_retroceso = presion * area - 2 * presion * longitud
    return fuerza_avance, fuerza_retroceso


presion_cilindro = 10.0  #psi
area_cilindro = 5.0  # Pulgadas - cuadradas
longitud_cilindro = 2.0  # Longitud - pulgadas

avance, retroceso = fuerza_retroceso(presion_cilindro, area_cilindro, longitud_cilindro)

print("Fuerza de avance:", avance, "lbs")
print("Fuerza de retroceso:", retroceso, "lbs")