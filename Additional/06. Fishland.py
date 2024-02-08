mackerel_kg = float(input())
sprinkle_kg = float(input())
bonito_kg = mackerel_kg * 1.60
safrid_kg = sprinkle_kg * 1.80
mussels_kg = 7.50

bought_bonito = float(input())
bought_safrid = float(input())
bought_mussels = float(input())

bill = bought_bonito * bonito_kg
bill += bought_mussels * mussels_kg
bill += bought_safrid * safrid_kg

print(f'{bill:.2f}')