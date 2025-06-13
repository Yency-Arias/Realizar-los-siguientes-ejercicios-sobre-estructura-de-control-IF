#             ---Calculadora de descuentos---
#solicitando el precio del producto
precio = float(input("Ingrese el precio del producto: $"))

#calculando el descuento segun el monto
if precio < 50:
    descuento = 0
elif 50 <= precio <= 100:
    descuento = 0.05
else:
    descuento = 0.10

#calculando el precio final con descuento
precio_final = precio * (1 - descuento)

#mostrando el resultado
print(f"Precio original: ${precio:.2f}")
print(f"Descuento aplicado: {descuento*100:.0f}%")
print(f"Precio final: ${precio_final:.2f}")