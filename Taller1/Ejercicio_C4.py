import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #para crear un sistema de coordenadas tridimensional

def dibujar_vector(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar el sistema de coordenadas
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

    # Dibujar el vector
    ax.quiver(0, 0, 0, x, y, z, color='k', arrow_length_ratio=0.1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def main():
    # Solicitar al usuario las coordenadas del vector
    x = float(input("Ingrese la coordenada X del vector: "))
    y = float(input("Ingrese la coordenada Y del vector: "))
    z = float(input("Ingrese la coordenada Z del vector: "))

    # Dibujar el vector
    dibujar_vector(x, y, z)

if __name__ == "__main__":
    main()