a= 1
while True:
    print("el piso actual es: ", a)
    print("Ingrese piso de destino: ")
    b= int(input())
    if a<b:
        print("El ascensor está subiendo")
    elif a>b:
        print("El ascensor está bajando")
    else:
        print("El destino no puede ser el mismo")
    a=b        