book_pages = int(input())
pages_per_hour = int(input())
days_limit = int(input())

total_time_to_reed = book_pages // pages_per_hour
time_to_reed_per_day = total_time_to_reed // days_limit

print(time_to_reed_per_day)
