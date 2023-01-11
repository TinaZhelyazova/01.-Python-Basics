number_of_pages = int(input())
pages_read_for_hour = int(input())
number_of_days=int(input())

hours_needed = number_of_pages/pages_read_for_hour
hours_per_day = hours_needed/number_of_days

print(int(hours_per_day))