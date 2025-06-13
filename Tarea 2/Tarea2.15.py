#               ---Comparación de tres longitudes---
#solicitando los tres lados
lado1 = float(input('Ingrese la longitud del primer lado: '))
lado2 = float(input('Ingrese la longitud del segundo lado: '))
lado3 = float(input('Ingrese la longitud del tercer lado: '))

#verificando la condición para formar un triangulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Las longitudes SI pueden formar un triangulo.')
else:
    print('Las longitudes NO pueden formar un triangulo.')