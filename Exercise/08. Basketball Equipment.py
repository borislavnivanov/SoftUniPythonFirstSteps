fee = int(input())

# shoes = fee - 40%
shoes = fee * (1 - (40 / 100))

# clothes = shoes - 20%
clothes = shoes - (shoes * (20 / 100))

# ball = 1/4 of clothes
ball = clothes / 4

# accessories = 1/5 of ball
accessories = ball / 5

print(fee + shoes + clothes + ball + accessories)