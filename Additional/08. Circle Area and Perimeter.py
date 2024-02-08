from math import pi

radius = float(input())

# calculate perimeter 2 * pi * r
perimeter = radius * pi * 2

# calculate area pi * r\2
exponent = 2
area = (radius ** exponent) * pi

print(f'{area:.2f}\n{perimeter:.2f}')
