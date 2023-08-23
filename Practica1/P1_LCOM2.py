import numpy as np

# Función para realizar el cifrado César
def cifrado_cesar(texto, clave):
    resultado = []  # Lista para almacenar el resultado cifrado
    for letra in texto:
        if letra.isalpha():  # Verixxfica si la letra es parte del alfabeto
            offset = ord('a') if letra.islower() else ord('A')
            # Aplica el desplazamiento y módulo 26 para mantenerlo en el rango de letras
            cifrada = chr((ord(letra) - offset + clave) % 26 + offset)
            resultado.append(cifrada)  # Agrega la letra cifrada al resultado
        else:
            resultado.append(letra)  # Si no es letra, la agrega sin cambios al resultado
    return ''.join(resultado)  # Convierte la lista en una cadena y devuelve el resultado

# Función para realizar el descifrado César
def descifrado_cesar(texto, clave):
    return cifrado_cesar(texto, -clave)  # Llama a la función cifrado_cesar con clave negativa

# Función para convertir una matriz numérica en una cadena de letras
def matrix_to_letter(n):
    global encry_string
    encry_string = ''
    for i in n:
        for j in i:
            encry_string += chr(j + 97)  # Convierte el valor a letra (a=0, b=1, ...) y agrega al resultado
    return encry_string 

# Función para realizar el cifrado Hill
def cifrado_hill(a, b):
    encry_l = []  # Lista para almacenar el resultado cifrado
    for i in range(0, len(b), 2):  # Divide el texto en bloques de dos letras
        l = []
        try:
            l += [ord(b[i]) - 97, ord(b[i + 1]) - 97]  # Convierte las letras a números (a=0, b=1, ...)
        except:
            l += [ord(b[i]) - 97, 0]  # Si solo queda una letra en el bloque, rellena con cero
        c = np.matmul(a, l)  # Realiza multiplicación matricial entre la matriz y el bloque de letras
        encry_l.append(c % 26)  # Agrega el resultado a la lista (módulo 26 para mantener en el rango)
    
    return matrix_to_letter(encry_l)  # Convierte la lista en una cadena de letras y devuelve el resultado

# Función que muestra un menú interactivo al usuario
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
            msg = input("Ingresa el texto: ")
            msj = "Ingresa la clave como una matriz 2x2 separada por comas ejemplo (1, 2, 1, 3): "
            clave_str = input(msj)
            clave = [int(x.strip()) for x in clave_str.split(',')]

            word_list = msg.split(" ")  # Divide el texto en palabras
            mensaje_desencriptado = ''
            mensaje_encriptado = ''

            if opcion == '3':
                for i in word_list:
                    length = len(i)
                    if len(i)%2!=0:
                        i=i+'a'
                    randmat = np.array(clave).reshape(2, 2)  # Crea la matriz clave
                    mensaje_encriptado += " " + cifrado_hill(randmat, i)  # Realiza el cifrado Hill
                resultado = mensaje_encriptado
            else:
                for i in word_list:
                    length = len(i)
                    if len(i)%2!=0:
                        i=i+'a'
                    randmat = np.array(clave).reshape(2, 2)  # Crea la matriz clave
                    inv = np.linalg.inv(randmat)  # Calcula la inversa de la matriz
                    int_inv = inv.astype(int)  # Convierte los valores de la matriz inversa a enteros
                    mensaje_desencriptado += " " + cifrado_hill(int_inv, i)[0:length]  # Realiza el descifrado Hill
                resultado = mensaje_desencriptado
        else:
            resultado = "Opción inválida."
        
        print("Resultado:", resultado)

menu()
