width = float(input()) * 100
length = float(input()) * 100

length -= 100.00   # account for corridor
places_per_length = length // 70

places_per_width = width // 120

total_places = places_per_width * places_per_length
total_places -= 3   # account for door and console

print(total_places)
