pages = int(input())
pages_per_hour = int(input())
days = int(input())

reading_time = pages / pages_per_hour
need_hour = reading_time // days

print(need_hour)
