import math

def volumen_prisma(base, altura):
    return base * altura

def volumen_piramide(base, altura):
    return (1/3) * base * altura

def volumen_cono(radio, altura):
    return (1/3) * math.pi * radio**2 * altura

def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura

def main():
    while True:
        print("CÁLCULO DE VOLUMENES")
        print("Seleccione el sólido del que desea calcular el volumen:")
        print("1. Prisma")
        print("2. Pirámide")
        print("3. Cono")
        print("4. Cilindro")
        print("5. Salir")

        opcion = int(input("Sólido correspondiente (Ingrese 5 para salir): "))

        if opcion == 5:
            break  # Salir del bucle si elige la opción 5

        if 1 <= opcion <= 4:
            if opcion == 1:
                base = float(input("Ingrese la base del prisma: "))
                altura = float(input("Ingrese la altura del prisma: "))
                resultado = volumen_prisma(base, altura)
                print("El volumen del prisma es:", resultado)
            elif opcion == 2:
                base = float(input("Ingrese la base de la pirámide: "))
                altura = float(input("Ingrese la altura de la pirámide: "))
                resultado = volumen_piramide(base, altura)
                print("El volumen de la pirámide es:", resultado)
            elif opcion == 3:
                radio = float(input("Ingrese el radio del cono: "))
                altura = float(input("Ingrese la altura del cono: "))
                resultado = volumen_cono(radio, altura)
                print("El volumen del cono es:", resultado)
            elif opcion == 4:
                radio = float(input("Ingrese el radio del cilindro: "))
                altura = float(input("Ingrese la altura del cilindro: "))
                resultado = volumen_cilindro(radio, altura)
                print("El volumen del cilindro es:", resultado)
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 5.")

if __name__ == "__main__":
    main()
