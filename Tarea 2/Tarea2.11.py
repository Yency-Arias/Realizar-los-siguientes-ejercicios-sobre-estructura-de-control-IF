#            ---Cálculo de impuestos---
#solicitando el salario mensual al usuario
salario = float(input('Ingresa tu salario mensual: '))

#calculando el impuesto segun el salario
if salario < 10000:
    impuesto = 0
elif salario <= 30000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20

#mostrando el resultado
print('El impuesto aplicado es:', impuesto)
print('Tu salario despues del impuesto es:', salario - impuesto)