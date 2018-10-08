import math
def circuloArea(radio):
    return radio**2 * math.pi

def cuadradoArea(lado):
    return lado*lado

def trianguloArea(base,altura):
    return (base*altura)/2

def agregarLista(lista,cantidad):
    for i in range(cantidad):
        a = input("Ingrese a agregar: ")
        lista.append(a)
        

def main():
    lista = []
    opc = ''
    while(opc != 's'):
        print("1) Calcular area del circulo")
        print("2) Calcular el area de un cuadrado")
        print("3) Calcular el area de un triangulo")
        print("4) Agregar a la lista")
        print("s) Salir")
        opc = input("Ingerese su opc: ")

        if opc == '1':
            radio = (float)(input("Ingrese el radio del circulo: "))
            print("El area del ciruculo es", circuloArea(radio))
        elif opc == '2':
            lado = (float)(input("Ingrese el lado del circulo: "))
            print("El area del cuadrado es: ", cuadradoArea(lado));
        
        elif opc == '3':
            base = (float)(input("Ingrese la base del triangulo: "))
            altura = (float)(input("Ingrese la altura del triangulo: "))
            print("El area del triagunlo", trianguloArea(base,altura))
        
        elif opc == '4':
            cantidad = (int)(input("Ingrese la cantidad de elementos que quiere añadir: "))
            agregarLista(lista,cantidad)

            for i in lista:
                print("Elemento: ", i)


if __name__ == "__main__":
    main()