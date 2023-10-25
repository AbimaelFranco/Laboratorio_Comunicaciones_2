import serial
import time

def excutable():
    print("\n--------------DECODIFICACION EN HAMMING--------------\n")
    while True:
        print("Menú:")
        print("1. Ejecutar")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            main()
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1 para ejecutar o 2 para salir.")

def calculate_parity_bits(data):
    n = len(data)
    m = 1
    while 2 ** m <= n + m:
        m += 1

    code = [0] * (n + m)
    j = 0

    for i in range(1, n + m + 1):
        if i == 2 ** j:
            j += 1
        else:
            code[i - 1] = int(data.pop(0))

    for j in range(m):
        parity = 0
        for i in range(1, n + m + 1):
            if i & (2 ** j) != 0:
                parity ^= code[i - 1]
        code[2 ** j - 1] = parity

    return code

def hamming_encode(input_data):
    data = list(input_data)
    code = calculate_parity_bits(data)
    return ''.join(map(str, code))

def hamming_decode(encoded_data):
    data = list(encoded_data)
    n = len(data)
    m = 1
    while 2 ** m <= n:
        m += 1

    errors = 0
    for j in range(m):
        parity = 0
        for i in range(1, n + 1):
            if i & (2 ** j) != 0:
                parity ^= int(data[i - 1])
        if parity != 0:
            errors += 2 ** j

    if errors > 0:
        print(f"Se ha detectado un error en el bit {errors} de paridad.")
        data[errors - 1] = '0' if data[errors - 1] == '1' else '1'
        print("Datos corregidos:", ''.join(data))
    else:
        print("No se ha detectado ningún error.")
        print("Datos originales:", ''.join(data[0:]))

def hamming_reverse(data_with_parity):
    data = list(data_with_parity)
    n = len(data)  
    m = 1
    while 2 ** m <= n:
        m += 1

    decoded_data = []

    for i in range(1, n + 1):
        if i not in (2 ** j for j in range(m)):
            decoded_data.append(data[i - 1])

    return ''.join(decoded_data)

def validacion(cadena):
    for caracter in cadena:
        if caracter != '0' and caracter != '1':
            return False
    return True

def main():

    try:
        serialArduino = serial.Serial("COM11", 9600)
        time.sleep(1)
        print("Conexión exitosa con arduino")

        while True:
            encoded_data = serialArduino.readline().decode('ascii')
            nombre_archivo = "archivo.txt"

            with open(nombre_archivo, "w") as archivo:
                archivo.write(encoded_data)
            nombre_archivo = "archivo.txt"

            with open(nombre_archivo, "r") as archivo:
                mensaje = archivo.read()
                mensaje=mensaje[0:len(mensaje)-1]

            encoded_data=mensaje

            if validacion(encoded_data):
                break

        hamming_decode(encoded_data)
        decoded_data = hamming_reverse(encoded_data)
        print("Datos originales después de decodificar:", decoded_data)

    except:
            advertencia = "\033[91mProblema de conexión con tarjeta arduino.\033[0m"
            print(advertencia)

excutable()