COVER_SHEET_PER_M2 = 1.50
PAINT_PER_LITTER = 14.50
THINNER_PER_LITTER = 5.00
BAG = 0.40
WORKERS_RATE = 30 / 100

needed_cover_sheet = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours_work = int(input())

# addons coover sheet 2/m2 and paint - 10%
total_sum = (needed_cover_sheet + 2) * COVER_SHEET_PER_M2
total_sum += (needed_paint * 1.10) * PAINT_PER_LITTER
total_sum += needed_thinner * THINNER_PER_LITTER
total_sum += BAG

# work calculation
work_pay = (total_sum * WORKERS_RATE) * hours_work

print(total_sum + work_pay)