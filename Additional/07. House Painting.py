x = float(input())      # height of house
y = float(input())      # width of house
h = float(input())      # height triangle side of the roof

# main house - green paint
exponent = 2

# front and back sides - deduct door 1.2m by 2m
area_house_front_back = x ** exponent
area_house_front_back = area_house_front_back * 2
door_area = 1.2 * 2
area_house_front_back -= door_area

# sides - deduct windows on each side - square 1.5m
area_house_sides = x * y
area_house_sides = area_house_sides * 2
window_area = 1.5 ** exponent
window_area = window_area * 2
area_house_sides -= window_area

total_green_paint = area_house_front_back + area_house_sides

# roof - red paint

# main sides
area_roof_main = x * y
area_roof_main = area_roof_main * 2

# rectangle front and back
area_roof_triangle = (x * h) / 2
area_roof_triangle = area_roof_triangle * 2

total_red_paint = area_roof_main + area_roof_triangle

# green paint 1l per 3.4m2
# red paint 1l per 4.3m2

litter_green_paint = total_green_paint / 3.4
litter_red_paint = total_red_paint / 4.3

print(f'{litter_green_paint:.2f}')
print(F'{litter_red_paint:.2f}')
