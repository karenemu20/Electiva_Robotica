import matplotlib.pyplot as plt
import numpy as np

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

# rango  de -200°C a 200°C
temperaturas = np.arange(-200, 201, 1)

# resistencia   
resistencias = [calcular_resistencia(temp) for temp in temperaturas]

plt.plot(temperaturas, resistencias, label='Comportamiento PT100')
plt.title('Comportamiento de un sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (ohmios)')
plt.grid(True)
plt.legend()
plt.show()
