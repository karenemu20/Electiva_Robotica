#A4 Tipos de robots

def obtener_articulaciones(tipo_robot):
    if tipo_robot == "cilíndrico":
        return "Cilíndrico", 2
    elif tipo_robot == "cartesiano":
        return "Cartesiano", 3
    elif tipo_robot == "esférico":
        return "Esférico", 3
    else:
        return "Tipo de robot no reconocido", None

def main():
    print("INFORMACIÓN SOBRE ROBOTS INDUSTRIALES")
    print("Seleccione el tipo de robot:")
    print("1. Cilíndrico")
    print("2. Cartesiano")
    print("3. Esférico")
    
    opcion = input("Ingrese la opción correspondiente: ")
    
    tipos = {
        "1": "cilíndrico",
        "2": "cartesiano",
        "3": "esférico"
    }
    
    if opcion in tipos:
        tipo_seleccionado = tipos[opcion]
        nombre_tipo, num_articulaciones = obtener_articulaciones(tipo_seleccionado)
        if num_articulaciones is not None:
            print(f"El tipo de robot seleccionado es {nombre_tipo} y posee {num_articulaciones} articulaciones.")
        else:
            print("Error!")
    else:
        print("Opción no válida. Seleccione un número del 1 al 3.")

if __name__ == "__main__":
    main()