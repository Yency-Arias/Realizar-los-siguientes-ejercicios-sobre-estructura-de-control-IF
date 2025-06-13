#             ---Número mayor entre dos---
#solicitando al usuario dos numeros
num1 = float(input('Ingresa el primer numero: '))
num2 = float(input('Ingresa el segundo numero: '))

#comparando los numeros
if num1 > num2:
    print(f'\n{num1} es mayor que {num2}.')
elif num2 > num1:
    print(f'\n{num2} es mayor que {num1}.')
else:
    print('\nAmbos numeros son iguales.')