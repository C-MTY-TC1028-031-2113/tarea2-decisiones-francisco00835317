
def main():
    edad = int(input("Ingresa tu edad: "))
    if edad < 18 :
        print("No cumples los requisitos")
    elif edad >= 18 :
        ide = input("¿Tienes identificacion oficial? (s/n):")
        if ide == "s" :
            print("Tramite de licencia concedido")
        elif ide == "n" :
            print("No cumples los requisitos")
        else :
            print("Respuesta incorrecta")


if __name__ == '__main__':
    main()
