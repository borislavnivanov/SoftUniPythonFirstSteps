# INPUT
m2 = float(input())

base_price = 7.61
discount = 18/100  # 18%

# SOLUTION
total_price = m2 * base_price
final_price = total_price * discount

# OUTPUT
print(f"The final price is: {total_price - final_price} lv.")

print(f"The discount is: {final_price} lv.")
