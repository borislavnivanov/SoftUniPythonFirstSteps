CHICKEN = 10.35
FISH = 12.40
VEGAN = 8.15
DESERT = 20 / 100    # 20% of total order
DELIVERY_SURCHARGE = 2.50

count_chicken = int(input())
count_fish = int(input())
count_vegan = int(input())

total_order: float = count_chicken * CHICKEN
total_order += count_fish * FISH
total_order += count_vegan * VEGAN
total_order += total_order * DESERT
total_order += DELIVERY_SURCHARGE

print(total_order)