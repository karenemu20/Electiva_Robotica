import random
def generador_de_numeros(min, max, num):
    return [random.randint(min, max) for _ in range(num)]
print("GENERADOR DE NÚMEROS ALEATORIOS\nIngrese un rango de números")
min = int(input('Desde el número: \n'))
max = int(input('Hasta el número: \n'))
num = int(input('Ingrese la cantidad de números aleatorias a generar dentro de ese rango: \n'))
lst = generador_de_numeros(min,max,num)
print('Los números aleatorios generados entre', min, "y", max, "son:", lst, '\n')
