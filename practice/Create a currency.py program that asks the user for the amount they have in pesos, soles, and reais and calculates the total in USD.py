# Write code below 💖

PESO_TO_USD = 0.056
SOLE_TO_USD = 0.27
REAI_TO_USD = 0.20

pesos = float(input("What do you have left is pesos: "))
soles = float(input("What do you have left is soles: "))
reais = float(input("What do you have left is reais: "))

usd_from_pesos = pesos * PESO_TO_USD
usd_from_soles = soles * SOLE_TO_USD
usd_from_reais = reais * REAI_TO_USD

total_usd = usd_from_pesos + usd_from_soles + usd_from_reais

print(f"The total amount in USD is: ${total_usd:.2f}")

