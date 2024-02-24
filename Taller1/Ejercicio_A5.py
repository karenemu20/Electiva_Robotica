import numpy as np

def rotacion_x(angulo):
    return np.array([[1, 0, 0], [0, np.cos(angulo), -np.sin(angulo)], [0, np.sin(angulo), np.cos(angulo)]])

def rotacion_y(angulo):
    return np.array([[np.cos(angulo), 0, np.sin(angulo)], [0, 1, 0], [-np.sin(angulo), 0, np.cos(angulo)]])

def rotacion_z(angulo):
    return np.array([[np.cos(angulo), -np.sin(angulo), 0], [np.sin(angulo), np.cos(angulo), 0], [0, 0, 1]])


angulo_rotacion = np.pi/4  # Radianes
matriz_rotacion_x = rotacion_x(angulo_rotacion)
matriz_rotacion_y = rotacion_y(angulo_rotacion)
matriz_rotacion_z = rotacion_z(angulo_rotacion)

print("Matriz de rotación en X:\n", matriz_rotacion_x)
print("Matriz de rotación en Y:\n", matriz_rotacion_y)
print("Matriz de rotación en Z:\n", matriz_rotacion_z)