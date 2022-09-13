stack_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
rack_needed = 1
current_rack = rack_capacity

while stack_of_clothes:
    
    current_clothes = stack_of_clothes.pop()
    if current_rack >= current_clothes:
        current_rack -= current_clothes

    else:
        rack_needed += 1
        current_rack = rack_capacity
        current_rack -= current_clothes

print(rack_needed)
