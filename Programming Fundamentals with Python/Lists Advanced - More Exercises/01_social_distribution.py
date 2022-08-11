population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

if sum(population) / len(population) < minimum_wealth:
    print("No equal distribution possible")

else:
    min_num = min(population)

    while min_num < minimum_wealth:
        needed_sum = minimum_wealth - min_num
        max_num = max(population)

        min_num_index = population.index(min_num)
        max_num_index = population.index(max_num)

        population[min_num_index] += needed_sum
        population[max_num_index] -= needed_sum

        min_num = min(population)

    print(population)
