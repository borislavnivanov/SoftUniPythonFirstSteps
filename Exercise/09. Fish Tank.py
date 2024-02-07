length = int(input())
width = int(input())
height = int(input())
used = float(input()) / 100

volume = length * width * height  # find volume
capacity = volume / 1000          # concert to litters
litters_to_fill = capacity * (1 - used)

print(litters_to_fill)
