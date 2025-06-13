#              ---Mayor entre tres numeros---
#solicitando al usuario tres numeros
num1 = float(input('Ingresa el primer numero: '))
num2 = float(input('Ingresa el segundo numero: '))
num3 = float(input('Ingresa el tercer numero: '))

#determinando el mayor de los tres
mayor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

#mostrando el resultado
print('\nEl numero mayor es:', mayor)