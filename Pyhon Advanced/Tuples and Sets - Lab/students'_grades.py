n = int(input())
students = {}

for _ in range(n):
    name, grade_as_str = input().split()
    grade = float(grade_as_str)

    if name not in students:
        students[name] = []

    students[name].append(grade)

for data in students.items():
    print(data)
    print(f"{data[0]} -> {' '.join([f'{x:.2f}' for x in data[1]])} "
          f"(avg: {(sum(data[1]) / len(data[1])):.2f})")
    print(data[1])
    print(f"{' '.join([f'{x:.2f}' for x in data[1]])}")
