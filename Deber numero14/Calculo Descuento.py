# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devolver el monto del descuento
    return descuento

# Llamada a la función calcular_descuento con solo el monto total de la compra
monto_total_1 = 1000
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1

# Llamada a la función calcular_descuento con el monto total de la compra y el porcentaje de descuento
monto_total_2 = 2000
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2

# Mostrar los resultados
print(f"Monto total de la compra: {monto_total_1} - Descuento: {descuento_1} - Monto final a pagar: {monto_final_1}")
print(f"Monto total de la compra: {monto_total_2} - Descuento: {descuento_2} - Monto final a pagar: {monto_final_2}")
