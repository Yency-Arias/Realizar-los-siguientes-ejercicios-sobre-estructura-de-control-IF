#               ---Dia de la semana---
# solicitando al usuario un numero del 1 al 7
numero = int(input('Ingresa un numero del 1 al 7: '))

# Lista de dias de la semana
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

#verificando si el numero esta en el rango valido
if 1 <= numero <= 7:
    print('\nEl día correspondiente es:', dias[numero - 1])
else:
    print('\nNumero invalido. Debe estar entre 1 y 7.')