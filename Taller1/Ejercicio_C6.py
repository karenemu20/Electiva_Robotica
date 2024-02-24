import cv2
import numpy as np

def obtener_contornos(imagen_path):
    imagen = cv2.imread(imagen_path)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, umbral = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos_xy = []
    for contorno in contornos:
        xy = np.squeeze(contorno)
        contornos_xy.append(xy)
    return contornos_xy

def main():
    logos = ["chevrolet_logo.png", "hyundai_logo.png", "mazda_logo.png", "toyota_logo.png", "audi_logo.png"]
    for logo in logos:
        contornos = obtener_contornos(logo)
        print(f"Coordenadas de contornos del logo {logo[:-4]}:")
        for i, contorno in enumerate(contornos):
            print(f"Contorno {i + 1}:")
            for x, y in contorno:
                print(f"X: {x}, Y: {y}")
        print("")

if __name__ == "__main__":
    main()