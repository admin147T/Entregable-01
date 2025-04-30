import numpy as np

def ingresar_vector(nombre):
    while True:
        print("Ingrese los elementos del vector", nombre, "separados por comas (máximo 10):", end=" ")
        entrada = input().strip()
        if not entrada:
            print("No se permite vacío. Intente de nuevo.")
            continue

        partes = entrada.split(",")
        if len(partes) > 10:
            print("Máximo permitido: 10 elementos. Intente de nuevo.")
            continue

        try:
            vector = [int(x.strip()) for x in partes]
            np_vector = np.array(vector)
            print("Vector", nombre, "ingresado:", np_vector)
            return np_vector
        except ValueError:
            print("Todos los elementos deben ser números enteros. Intente de nuevo.")

def propiedades_aritmeticas():
    print("Seleccione una propiedad aritmética:")
    print("1. Conmutativa")
    print("2. Asociativa")
    print("3. Distributiva")
    print("4. Identidad")
    print("5. Inverso")

    while True:
        opcion = input("Ingrese el número de la propiedad que desea (1-5): ").strip()
        if not opcion or not opcion.isdigit() or int(opcion) not in range(1, 6):
            print("Opción inválida. Intente de nuevo.\n")
            continue
        opcion = int(opcion)
        break

    if opcion == 1:  # Conmutativa
        print("\nPropiedad Conmutativa: a + b = b + a  y  a * b = b * a")
        a = ingresar_vector("A")
        b = ingresar_vector("B")
        if len(a) != len(b):
            print("Los vectores deben tener la misma longitud.")
            return
        print("A + B:", a + b)
        print("B + A:", b + a)
        print("¿Se cumple conmutativa en suma?", "Sí" if np.array_equal(a + b, b + a) else "No")
        print("A * B:", a * b)
        print("B * A:", b * a)
        print("¿Se cumple conmutativa en multiplicación?", "Sí" if np.array_equal(a * b, b * a) else "No")

    elif opcion == 2:  # Asociativa
        print("\nPropiedad Asociativa: (a + b) + c = a + (b + c)")
        a = ingresar_vector("A")
        b = ingresar_vector("B")
        c = ingresar_vector("C")
        if len(a) != len(b) or len(b) != len(c):
            print("Todos los vectores deben tener la misma longitud.")
            return
        print("(A + B) + C:", (a + b) + c)
        print("A + (B + C):", a + (b + c))
        print("¿Se cumple asociativa en suma?", "Sí" if np.array_equal((a + b) + c, a + (b + c)) else "No")
        print("(A * B) * C:", (a * b) * c)
        print("A * (B * C):", a * (b * c))
        print("¿Se cumple asociativa en multiplicación?", "Sí" if np.array_equal((a * b) * c, a * (b * c)) else "No")

    elif opcion == 3:  # Distributiva
        print("\nPropiedad Distributiva: a * (b + c) = a*b + a*c")
        a = ingresar_vector("A")
        b = ingresar_vector("B")
        c = ingresar_vector("C")
        if len(a) != len(b) or len(b) != len(c):
            print("Todos los vectores deben tener la misma longitud.")
            return
        print("A * (B + C):", a * (b + c))
        print("A * B + A * C:", (a * b) + (a * c))
        print("¿Se cumple la propiedad distributiva?", "Sí" if np.array_equal(a * (b + c), (a * b) + (a * c)) else "No")

    elif opcion == 4:  # Identidad
        print("\nPropiedad Identidad: a + 0 = a  y  a * 1 = a")
        a = ingresar_vector("A")
        print("A + 0:", a + np.zeros_like(a))
        print("A * 1:", a * np.ones_like(a))
        print("¿Se cumple identidad en suma?", "Sí" if np.array_equal(a + np.zeros_like(a), a) else "No")
        print("¿Se cumple identidad en multiplicación?", "Sí" if np.array_equal(a * np.ones_like(a), a) else "No")

    elif opcion == 5:  # Inverso
        print("\nPropiedad Inverso:")
        a = ingresar_vector("A")

        # Inverso aditivo
        negativo = -a
        suma = a + negativo
        print("A + (-A):", suma)
        print("¿Se cumple inverso aditivo (A + -A = 0)?", "Sí" if np.array_equal(suma, np.zeros_like(a)) else "No")

        # Inverso multiplicativo (solo si no hay ceros)
        if np.any(a == 0):
            print("No se puede calcular el inverso multiplicativo: el vector contiene ceros.")
        else:
            inverso = 1 / a
            producto = a * inverso
            print("A * (1/A):", producto)
            print("¿Se cumple inverso multiplicativo (A * 1/A = 1)?", "Sí" if np.allclose(producto, np.ones_like(a)) else "No")

# Ejecutar
propiedades_aritmeticas()
