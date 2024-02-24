def calcular_resistencia(pt100_temperatura):
    resistencia_0 = 100.0
    coeficiente_temperatura = 0.00385

    resistencia = resistencia_0 * (1 + coeficiente_temperatura * pt100_temperatura)
    return resistencia

temperatura = 30.0
resistencia_calculada = calcular_resistencia(temperatura)
print("Resistencia a", temperatura, "grados Celsius:", resistencia_calculada)