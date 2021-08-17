import math
def main():
    #escribe tu código abajo de esta línea
    Área = float(input('Área a pintar en metros: '))
    cantidad = int(input('Rendimiento (m2/1): '))
    litrospintura = Área/cantidad
    print('Litros a comprar: '+ str(int(math.ceil(litrospintura))))
if __name__ == '__main__':
    main()
