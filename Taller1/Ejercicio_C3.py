import numpy as np
import matplotlib.pyplot as plt

def carga_descarga_RC(voltaje, capacitancia, resistencia, tiempo):
    # Constante de tiempo (tau)
    tau = resistencia * capacitancia
    # Carga
    carga = voltaje * (1 - np.exp(-tiempo / tau))
    # Descarga
    descarga = voltaje * np.exp(-tiempo / tau)
    return carga, descarga

def main():
    # Solicitar al usuario los valores de voltaje, capacitancia y resistencia
    voltaje = float(input("Ingrese el valor de voltaje (V): "))
    capacitancia = float(input("Ingrese el valor de capacitancia (F): "))#Faradios
    resistencia = float(input("Ingrese el valor de resistencia (Ω): "))
    
    # Crear un rango de tiempo para graficar
    tiempo = np.linspace(0, 5 * resistencia * capacitancia, 1000)

    # Calcular carga y descarga
    carga, descarga = carga_descarga_RC(voltaje, capacitancia, resistencia, tiempo)

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, carga, label='Carga', color='blue')
    plt.plot(tiempo, descarga, label='Descarga', color='red')
    plt.title('Carga y Descarga en un Circuito RC')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()