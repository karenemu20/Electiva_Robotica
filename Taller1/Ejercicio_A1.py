import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

suma = vector1 + vector2
resta = vector1 - vector2
producto_punto = np.dot(vector1, vector2)
producto_cruz = np.cross(vector1, vector2)
division = vector1 / vector2

print("Suma:", suma)
print("Resta:", resta)
print("Producto Punto:", producto_punto)
print("Producto Cruz:", producto_cruz)
print("División:", division)