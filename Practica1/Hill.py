import numpy as np

def matrix_to_letter(n):
    global  encry_string
    encry_string=''
    for i in n:
        for j in i:
            encry_string+=chr(j+97)
    return encry_string 

def encryption(a,b):
    encry_l=[]
    for i in range(0,len(b),2):
        l=[]
        try:
            l += [ord(b[i])-97,ord(b[i+1])-97]
        except:
            l += [ord(b[i])-97,0]
        c=np.matmul(a,l)
        encry_l.append(c%26)

    return matrix_to_letter(encry_l)

msg=input("Ingrese el mensaje a encriptar : ")

msj = "Ingresa la clave como una matriz 2x2 separada por comas: "
clave_str = input(msj)
clave = [int(x.strip()) for x in clave_str.split(',')]

word_list=msg.split(" ")

encrypted_message=''
decrypted_message=''

for i in word_list:
    length=len(i)
    if len(i)%2!=0:
        i=i+'a'
    else:
        pass
    randmat = np.array(clave).reshape(2, 2)
    inv=np.linalg.inv(randmat)
    int_inv=inv.astype(int)
    
    encrypted_message+=" "+encryption(randmat,i)
    decrypted_message+=" "+encryption(int_inv ,encry_string)[0:length]

print("El mensaje encriptado es:",encrypted_message)
print("El mensaje desencriptado es  : ",decrypted_message)