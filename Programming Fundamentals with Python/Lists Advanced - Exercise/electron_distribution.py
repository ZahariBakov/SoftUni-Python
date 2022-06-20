electrons_number = int(input())
electrons_distribution = []
position_of_shell = 0

while electrons_number > 0:
    position_of_shell += 1
    adding_electrons = 2 * position_of_shell**2
    if electrons_number >= adding_electrons:
        electrons_number -= adding_electrons
        electrons_distribution.append(adding_electrons)
    else:
        electrons_distribution.append(electrons_number)
        electrons_number -= electrons_number

print(electrons_distribution)
