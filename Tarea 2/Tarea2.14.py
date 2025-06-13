#                  ---Conversión de calificaciones---
#solicitando un numero al usuario
nota = int(input('Ingrese la calificacion del estudiante (0-100): '))

#verificando la clasificacion
if nota >= 0 and nota <= 59:
    print(f'\nEs una lastima. El estudiante obtuvo F por sacar {nota} en su calificacion')
elif nota >= 60 and nota <= 69:
    print(f'\nVaya. El estudiante obtuvo D por sacar {nota} en su calificacion')
elif nota >= 70 and nota <= 79:
    print(f'\nEl estudiante obtuvo C por sacar {nota} en su calificacion')
elif nota >= 80 and nota <= 89:
    print(f'\nMuy bien! El estudiante obtuvo B por sacar {nota} en su calificacion!')
elif nota >= 90 and nota <= 100:
    print(f'\nExcelente! El estudiante obtuvo A por sacar {nota} en su calificacion!')
else:
    print('\nCalificacion invalida. Por favor, ingrese una calificacion del 0 hasta 100')