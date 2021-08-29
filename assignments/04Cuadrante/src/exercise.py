def main():
    # Escribe tu código abajo de esta línea
    grad = float(input("Introduce los grados: "))
    if grad < 0 or grad > 360:
        print("exede")
    if grad == 0 or grad == 90 or grad == 180 or grad == 360 or grad == 270:
        print("eje")
    if grad > 0 and grad < 90:
        print("Cuadrante 1")
    if grad > 90 and grad < 180:
        print("Cuadrante 2")
    if grad > 180 and grad < 270:
        print("Cuadrante 3")
    if grad > 270 and grad < 360:
        print("Cuadrante 4")

if __name__ == '__main__':
    main()
