#                 ---Evaluación de temperatura---
#solicitando la temperatura al usuario
temperatura = float(input('Introduce la temperatura en grados Celsius: '))

#evaluando la temperatura y mostrar el mensaje correspondiente
if temperatura < 0:
    print('\nHace mucho frío')
elif temperatura >= 0 and temperatura <= 20:
    print('\nClima fresco')
elif temperatura >= 21 and temperatura <= 30:
    print('\nClima agradable')
else:
    print('\nHace mucho calor') #temperatura > 30