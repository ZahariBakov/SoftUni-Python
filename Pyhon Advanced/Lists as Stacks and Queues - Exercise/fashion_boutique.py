stack_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
rack_needed = 1
current_rack = rack_capacity

while stack_of_clothes:
    current_clothes = stack_of_clothes[-1]

    if current_rack >= current_clothes:
        stack_of_clothes.pop()
        current_rack -= current_clothes
    else:
        rack_needed += 1
        current_rack = rack_capacity

print(rack_needed)
