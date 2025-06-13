#               ---Conversión de horas a turnos---
#pidiendo la hora al usuario
hora = int(input('Introduce la hora (0-23): '))

#verificando que la hora este en el rango valido
if hora < 0 or hora > 23:
    print(f'\n{hora} es una hora invalida. Debe estar entre 0 y 23.')
else:
    if 6 <= hora <= 11:
        print(f'\nSon las {hora}:00 de la mañana.')
    elif 12 <= hora <= 17:
        print(f'\nSon las {hora}:00 de la tarde.')
    elif 18 <= hora <= 23:
        print(f'\nSon las {hora}:00 de la noche.')
    else:
        print(f'\nSon las {hora}:00 de la madrugada.') # 0 <= hora <= 5