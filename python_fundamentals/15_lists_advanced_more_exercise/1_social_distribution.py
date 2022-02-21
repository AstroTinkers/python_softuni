population = [int(i) for i in input().split(", ")]
min_wealth = int(input())
equality = True
for i in population:
    wealthiest = max(population)
    wealthiest_index = population.index(wealthiest)
    if i != wealthiest:
        if population[population.index(i)] < min_wealth:
            population[wealthiest_index] -= min_wealth - i
            population[population.index(i)] = min_wealth
        if wealthiest <= min_wealth:
            print("No equal distribution possible")
            equality = False
            break
if equality:
    print(population)
