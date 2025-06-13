#              ---Clasificación de números---
#pidiendo tres números al usuario
num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))
num3 = int(input('Ingresa el tercer numero: '))

#verificando si alguno es cero
if num1 == 0 or num2 == 0 or num3 == 0:
    print(f'\nHay al menos un cero entre los numeros.\n({num1}, {num2}, {num3})')
#verificando si todos son positivos
elif num1 > 0 and num2 > 0 and num3 > 0:
    print(f'\nTodos los numeros son positivos.\n({num1}, {num2}, {num3})')
#verificando si todos son negativos
elif num1 < 0 and num2 < 0 and num3 < 0:
    print(f'\nTodos los numeros son negativos.\n({num1}, {num2}, {num3})')
#si no se cumple ninguna de las anteriores, son mixtos
else:
    print(f'\nLos numeros son mixtos\n({num1}, {num2}, {num3}).')