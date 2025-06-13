#               ---Numero par o impar---
#solicitando al usuario un numero entero
numero = int(input('Ingresa un numero entero: '))

#verificando si es par o impar
if numero % 2 == 0:
    print(f'\nEl numero {numero} es par.')
else:
    print(f'\nEl numero {numero} es impar.')