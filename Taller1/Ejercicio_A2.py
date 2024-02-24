import numpy as np

# inicializar
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

# Operaciones
suma_matriz = matriz1 + matriz2
resta_matriz = matriz1 - matriz2
producto_punto_matriz = np.dot(matriz1, matriz2)
producto_cruz_matriz = np.cross(matriz1, matriz2)
division_matriz = np.divide(matriz1, matriz2)

print("Suma de matrices:", suma_matriz)
print("Resta de matrices:", resta_matriz)
print("Producto Punto de matrices:", producto_punto_matriz)
print("Producto Cruz de matrices:", producto_cruz_matriz)
print("División de matrices:", division_matriz)