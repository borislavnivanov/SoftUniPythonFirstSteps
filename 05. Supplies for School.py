PACK_PENS = 5.80
PACK_HIGHLIGHTER = 7.20
DETERGENT_PER_L = 1.20

pc_of_pen = int(input())
pc_of_highlighter = int(input())
litters_of_detergent = int(input())
discount_coefficient = int(input()) / 100

total_price = pc_of_pen * PACK_PENS
total_price += pc_of_highlighter * PACK_HIGHLIGHTER
total_price += litters_of_detergent * DETERGENT_PER_L
discount_amount = total_price * discount_coefficient
final_price = total_price - discount_amount

print(final_price)
