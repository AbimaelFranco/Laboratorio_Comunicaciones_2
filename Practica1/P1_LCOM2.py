import numpy as np

def cifrado_cesar(texto, clave):
    resultado = []
    for letra in texto:
        if letra.isalpha():
            offset = ord('a') if letra.islower() else ord('A')
            cifrada = chr((ord(letra) - offset + clave) % 26 + offset)
            resultado.append(cifrada)
        else:
            resultado.append(letra)
    return ''.join(resultado)

def descifrado_cesar(texto, clave):
    return cifrado_cesar(texto, -clave)

def cifrado_hill(texto, clave):
    clave_matrix = np.array(clave)
    texto_numeros = [ord(letra) - ord('a') for letra in texto.lower() if letra.isalpha()]
    while len(texto_numeros) % clave_matrix.shape[0] != 0:
        texto_numeros.append(0)
    texto_matrix = np.array(texto_numeros).reshape(-1, clave_matrix.shape[0])
    resultado_matrix = np.dot(texto_matrix, clave_matrix) % 26
    cifrado = ''.join(chr(num + ord('a')) for fila in resultado_matrix for num in fila)
    return cifrado

def descifrado_hill(texto, clave):
    clave_matrix = np.array(clave)
    clave_inverse = np.linalg.inv(clave_matrix)
    clave_inverse = np.round(clave_inverse * np.linalg.det(clave_matrix)) % 26
    return cifrado_hill(texto, clave_inverse)

def menu():
    while True:
        print("\nSelecciona un tipo de operación:")
        print("1. Cifrado César")
        print("2. Descifrado César")
        print("3. Cifrado Hill")
        print("4. Descifrado Hill")
        print("5. Salir")
        opcion = input("Ingresa el número de la opción: ")

        if opcion == '5':
                print("¡Hasta luego!")
                break

        if opcion == '1' or opcion == '2':
            texto = input("Ingresa el texto: ")
            clave = int(input("Ingresa la clave (número entero): "))
            if opcion == '1':
                resultado = cifrado_cesar(texto, clave)
            else:
                resultado = descifrado_cesar(texto, clave)
        elif opcion == '3' or opcion == '4':
            texto = input("Ingresa el texto: ")
            clave_str = input("Ingresa la clave como una matriz 2x2 separada por comas y espacios (ejemplo: 2, 3, 5, 7): ")
            clave = [int(x.strip()) for x in clave_str.split(',')]
            clave = np.array(clave).reshape(2, 2)
            if opcion == '3':
                resultado = cifrado_hill(texto, clave)
            else:
                resultado = descifrado_hill(texto, clave)
        else:
            print("Opción inválida.")
            return
        
        print("Resultado:", resultado)

menu()