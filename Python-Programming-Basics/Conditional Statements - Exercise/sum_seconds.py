first_competitors = int(input())
second_competitors = int(input())
third_competitors = int(input())

total_time = first_competitors + second_competitors + third_competitors

hour = total_time // 60
minutes = total_time % 60

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
