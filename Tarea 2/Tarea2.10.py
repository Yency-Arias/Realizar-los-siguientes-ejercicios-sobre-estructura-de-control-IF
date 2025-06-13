#              ---Clasificación de angulos---
#solicitando al usuario el valor del angulo
angulo = float(input('Ingresa el valor del angulo en grados: '))

#determinando el tipo de angulo
if angulo > 0 and angulo < 90:
    print('El angulo es agudo.')
elif angulo == 90:
    print('El angulo es recto.')
elif angulo > 90 and angulo < 180:
    print('El angulo es obtuso.')
elif angulo == 180:
    print('El angulo es llano.')
else:
    print('Angulo invalido. Debe estar entre 0° y 180°.')