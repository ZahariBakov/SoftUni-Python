from collections import deque


def pizzas_processing(pizzas, employes):
    total_pizzas = 0

    while pizzas and employees:
        while pizzas[0] > employees[-1]:
            pizzas[0] -= employees[-1]
            total_pizzas += employees.pop()

            if not pizzas or not employees:
                return total_pizzas

        total_pizzas += pizzas.popleft()
        employes.pop()

    return total_pizzas


pizzas = deque([int(x) for x in input().split(", ") if 0 < int(x) < 11])
employees = [int(x) for x in input().split(", ")]

total_pizzas = pizzas_processing(pizzas, employees)


if not pizzas:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizzas)}")
