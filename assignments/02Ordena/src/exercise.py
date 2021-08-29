def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x < y and y < z :
        print(x)
        print(y)
        print(z)
    elif x < y and z < y :
        print(x)
        print(z)
        print(y)
    elif z < y and x < y:
        print(z)
        print(x)
        print(y)
    elif z < x and y < x:
        print(z)
        print(y)
        print(x)
    elif y < x and x < z:
        print(y)
        print(x)
        print(z)
    elif y < z and z < x:
        print(y)
        print(z)
        print(x)

if __name__=='__main__':
    main()
