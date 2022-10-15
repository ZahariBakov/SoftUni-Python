from collections import deque

ramens = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while ramens and customers:
    if ramens[-1] == customers[0]:
        ramens.pop()
        customers.popleft()
    elif ramens[-1] > customers[0]:
        ramens[-1] -= customers.popleft()
    elif ramens[-1] < customers[0]:
        customers[0] -= ramens.pop()

if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(y) for y in customers)}")
else:
    print("Great job! You served all the customers.")
    if ramens:
        print(f"Bowls of ramen left: {', '.join(str(y) for y in ramens)}")
