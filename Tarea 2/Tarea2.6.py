#               ---Calificacion aprobatoria---
#pidiendo la nota a usuario
nota = float(input('Ingrese la nota del estudiante (0-100): '))

#verificando la nota
if 0 <= nota <= 100:
    if nota >= 60:
        print(f'\n¡El estudiante ha aprobado con exito la materia con {nota}/100!')
    
    else:
        print(f'\nLamentablemente el estudiante ha reprobado con {nota}/100')
else:
    print(f'\n{nota} es una calificacion invalida. Debe estar entre 0 y 100.')