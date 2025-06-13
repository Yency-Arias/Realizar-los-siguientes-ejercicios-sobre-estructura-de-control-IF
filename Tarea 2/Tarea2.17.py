#                    ---Tipo de triángulo---
#pidiendo al usuario las longitudes de los lados
lado1 = float(input('Introduce la longitud del primer lado: '))
lado2 = float(input('Introduce la longitud del segundo lado: '))
lado3 = float(input('Introduce la longitud del tercer lado: '))

#verificando si las longitudes pueden formar un triangulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    
    #determinando el tipo de triangulo
    if lado1 == lado2 == lado3:
        print('\nEl triangulo es equilatero.') #triangulo con todos los lados iguales
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('\nEl triangulo es isosceles.') #triangulo con dos lados iguales
    else:
        print('\nEl triangulo es escaleno.') #triangulo con todos los lados diferentes
else:
    print('\nLas longitudes no forman un triangulo.')