#solicitando peso y altura al usuario
peso = float(input('Introduce tu peso en kilogramos (kg): '))
altura = float(input('Introduce tu altura en metros (m): '))

#verificando que los valores sean positivos
if peso <= 0 or altura <= 0:
    print('\nLos valores deben ser mayores que cero.')
else:
    #calculando el IMC
    imc = peso / (altura ** 2)
    
    #mostrando el IMC con dos decimales
    print(f'\nTu IMC es: {imc:.2f}')

    #clasificando según el IMC
    if imc < 18.5:
        print('Clasificación: Bajo peso')
    elif imc < 25:
        print('Clasificación: Normal')
    elif imc < 30:
        print('Clasificación: Sobrepeso')
    else:
        print('Clasificación: Obesidad')