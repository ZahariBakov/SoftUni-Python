from collections import deque

food_quantity = int(input())
clients = input()
clients = clients.split(" ")
queue = deque()

for ch in clients:
    queue.append(int(ch))

print(max(queue))

while queue:
    current_order = queue.popleft()
    if current_order > food_quantity:
        queue.appendleft(current_order)
        break

    else:
        food_quantity -= current_order
if queue:
    final_print = ''
    while queue:
        final_print += str(queue.popleft()) + " "
    print(f"Orders left: {final_print}")

else:
    print("Orders complete")
