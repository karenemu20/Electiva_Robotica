import math

def cilindricas(x, y, z):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    z_cylindricas = z
    return r, theta, z_cylindricas

def   esfericas  (x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r)
    return r, theta, phi

x, y, z = 3, 4, 5
Coordenadas_cilindricas = cilindricas(x, y, z)
Coordenadas_esfericas = esfericas(x, y, z)

print("Coordenadas cilíndricas:", Coordenadas_cilindricas)
print("Coordenadas esféricas:", Coordenadas_esfericas)
