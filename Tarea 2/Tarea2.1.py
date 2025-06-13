#                    ---Numero positivo, negativo o cero---
#solicitando al usuario que ingrese un numero
numero = float(input('Ingresa un numero: '))

#determinando si el numero es positivo, negativo o cero
if numero > 0:
    print('El numero es positivo.')
elif numero < 0:
    print('El numero es negativo.')
else:
    print('El numero es cero.')