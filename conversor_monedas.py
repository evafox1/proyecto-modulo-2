# Conversor de monedas

pesos = float(input("Ingrese la cantidad en pesos mexicanos: "))
tipo_cambio = float(input("Ingrese el tipo de cambio del dólar: "))

dolares = pesos / tipo_cambio

print(f"Cantidad en pesos ingresada: ${pesos:} MXN")
print(f"Tipo de cambio ingresado: ${tipo_cambio: } MXN por dólar")
print(f"Cantidad convertida a dólar es de: ${dolares:.2f} USD")