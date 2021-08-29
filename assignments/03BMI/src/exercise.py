def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    if peso == 0 or altura == 0:
        print("Revisa tus datos, alguno de ellos es erroneo")
    indice = int(peso)/((altura)**2)
    if indice < 20:
        print("Peso bajo")
    if 20 <= indice < 25:
        print("Peso normal")
    if 25 <= indice < 30:
        print("Sobrepeso")
    if 30 <= indice < 40:
        print("Obesidad")
    if indice > 40:
        print("Obesidad morbida")

if __name__=='__main__':
    main()