def excutable():
    print("\n--------------CODIFICACIÓN EN HAMMING--------------\n")
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

def validacion(cadena):
    for caracter in cadena:
        if caracter != '0' and caracter != '1':
            return False
    return True

def main():
    
    while True:
        input_data = input("Ingrese la serie de bits a codificar: ")
        if validacion(input_data):
            break
        else:
            print("\nEl mensaje debe contener solo 0s y 1s, ingresa un nuevo mensaje:")
        
    encoded_data = hamming_encode(input_data)
    print("Datos codificados con Hamming:", encoded_data)

excutable()