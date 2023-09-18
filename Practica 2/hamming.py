def main():
    while True:
        print("Menú:")
        print("1. Ejecutar")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            principal()
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1 para ejecutar o 2 para salir.")

def principal():
    ##Ingreso de mensaje a transmitir y validacion
    while True:
        data = input("\nIngresa el mensaje binario a transmitir: ")
        if validacion(data):
            # print("El mensaje ingresado es: ", data)
            break
        else:
            print("\nEl mensaje debe contener solo 0s y 1s, ingresa un nuevo mensaje:")

    # Calcula la cantidad de bits redundantes necesarios
    m = len(data)
    r = calcRedundantBits(m)

    # Determina las posiciones de los bits redundantes
    arr = posRedundantBits(data, r)
    # print("La posicion de los bits de redundancia son: ", arr)

    # Determina los bits de paridad
    arr = calcParityBits(arr, r)

    # Determina el bit extra de hamming extendido
    paridad = hamming_extendido(data)
    print("Bit de paridad de Hamming extendido: ", paridad)
    arr1 = str(paridad) + arr

    # Datos a transferir
    print("Los datos transferidos son: " + arr1)
    print("\n")

    ##Ingreso de mensaje con error y validacion
    while True:
        arr = input("Ingresa el mensaje binario erroneo a recibido (con un error): ")
        if validacion(arr):
            print("Datos con error: " + arr)
            bit_paridad_error = arr[0]
            arr = arr[1:]
            break
        else:
            print("El mensaje debe contener solo 0s y 1s, ingresa un nuevo mensaje:")

    # print("Datos con error: " + arr)

    #Comprobacion de errores
    correccion = detectError(arr, r)
    if bit_paridad_error != str(paridad):
        print("Error en Bit de paridad de Hamming Extendido")
    elif(correccion == 0):
        print("No hay errores en el mensaje recibido.")
    else:
        print("La posición del error es:", len(arr) - correccion + 2, "desde la izquierda. \n")

def validacion(cadena):
    for caracter in cadena:
        if caracter != '0' and caracter != '1':
            return False
    return True

def calcRedundantBits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            print("La cantidad de bits de paridad añadidos son: ", i)
            return i

def hamming_extendido(data):
    num = 0
    suma = 0
    for i in range(len(data)):
        num = data[i]
        if num == '1':
            suma+= 1
        
    # print("Cantidad de 1 en cadena:", suma)
    
    if suma%2 == 0:
        return 0
    else:
        return 1

def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''

    # Insersion de 0 en bits de potencia 2
    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    # Inversion de posiciones en la cadena
    return res[::-1]

def calcParityBits(arr, r):
    n = len(arr)

    # Para encontrar el bit de paridad r, itera desde 0 hasta r - 1
    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # Si la posición tiene un 1 en la posición
            # i-ésima significativa, se aplica una operación XOR
            # al valor del array para encontrar el valor del bit de paridad.
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
                # Se usa -1 * j ya que el array está invertido

        # Concatenación de cadenas
        # (0 a n - 2^r) + bit de paridad + (n - 2^r + 1 a n)
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:]
    return arr

def detectError(arr, nr):
    n = len(arr)
    res = 0

    # Calcula nuevamente los bits de paridad
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])

        # Crea un número binario al concatenar
        # los bits de paridad juntos.
        res = res + val*(10**i)

    # Convierte binario a decimal
    return int(str(res), 2)

main()