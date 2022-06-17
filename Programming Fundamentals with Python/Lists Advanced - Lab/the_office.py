employees_happiness = list(map(int, input().split()))
factor = int(input())
total_happiness = 0
employees_count = []
happy_employees = 0

for employer in range(len(employees_happiness)):
    total_happiness += employees_happiness[employer] * factor
    employees_count.append(employees_happiness[employer] * factor)

average_happiness = total_happiness / len(employees_happiness)

for i in range(len(employees_count)):
    if employees_count[i] >= average_happiness:
        happy_employees += 1
if happy_employees >= len(employees_happiness) / 2:
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(employees_happiness)}. Employees are not happy!")
