import numpy as np

def crear_matriz():
    matriz = []

    while True:
        print("Ingrese el número de filas (máximo 10): ", end="")
        filas = input().strip()
        print("Ingrese el número de columnas (máximo 10): ", end="")
        columnas = input().strip()

        if not filas or not columnas:
            print("No se permiten valores vacíos. Intente de nuevo.\n")
            continue

        if not filas.isdigit() or not columnas.isdigit():
            print("Debe ingresar números enteros positivos. Intente de nuevo.\n")
            continue

        filas = int(filas)
        columnas = int(columnas)

        if filas <= 0 or columnas <= 0:
            print("El número de filas y columnas debe ser mayor que cero.\n")
            continue
        
        if filas > 10 or columnas > 10:
            print("El número máximo permitido de filas y columnas es 10. Intente de nuevo.\n")
            continue
        break

    print("\nIngrese los elementos de la matriz", filas, ",", columnas)

    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                print("Elemento", i+1, ",", j+1, end=": ")
                valor = input().strip()
                if not valor:
                    print("No se permite valor vacío. Intente de nuevo.")
                    continue
                try:
                    num = float(valor)
                    fila.append(num)
                    break
                except ValueError:
                    print("Debe ingresar un número válido. Intente de nuevo.")
        matriz.append(fila)

    matriz_np = np.array(matriz)

    print("\nLa matriz generada es:")
    for fila in matriz_np:
        print("[", end="")
        for elem in fila:
            if elem == int(elem):
                print(int(elem), end=" ")
            else:
                print(elem, end=" ")
        print("]")  # Cerramos el corchete por fila

# Ejecutar la función
crear_matriz()
