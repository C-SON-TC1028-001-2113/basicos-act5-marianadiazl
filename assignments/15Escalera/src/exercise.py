import math
def main():
    #escribe tu código abajo de esta línea
    altura = int(input('Altura de la casa: '))
    angulo = int(input('Angulo en grados: '))
    escalera = round(math.fabs(altura/math.sin(math.radians(angulo))))
    print('Largo de la escalera: ' + str(escalera))

if __name__ == '__main__':
    main()
