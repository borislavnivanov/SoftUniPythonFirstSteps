EUR_EXCHANGE_RATE = 1.94

price_per_kg_vegetables = float(input())
price_per_kg_fruits = float(input())

vegetables_sold_kg = int(input())
fruits_sold_kg = int(input())

bill = vegetables_sold_kg * price_per_kg_vegetables
bill += fruits_sold_kg * price_per_kg_fruits

print(f'{bill / EUR_EXCHANGE_RATE:.2f}')
