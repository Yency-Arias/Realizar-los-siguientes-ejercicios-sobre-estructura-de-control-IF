#            ---Descuento por edad---
#pidiendo la edad al usuario
edad = int(input('Por favor, ingresa tu edad: '))

#verificando si aplica descuento
if edad > 60:
    print(f'¡Aplicas para el descuento del 50% en el cine!')
else:
    print('No aplicas para el descuento.')