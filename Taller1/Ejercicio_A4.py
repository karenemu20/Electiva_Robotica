def calcular_resistencia(temp_rtd):
    R0 = 100.0  # Valor de resistencia a 0°C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12

    if temp_rtd >= 0:
        Rt = R0 * (1 + A * temp_rtd + B * temp_rtd**2)
    else:
        Rt = R0 * (1 + A * temp_rtd + B * temp_rtd**2 + C * (temp_rtd - 100) * temp_rtd**3)

    return Rt

temperatura = float(input("Ingrese la temperatura RTD en grados Celsius: "))
resistencia = calcular_resistencia(temperatura)
print(f"La resistencia de la RTD a {temperatura}°C es {resistencia} ohmios.")