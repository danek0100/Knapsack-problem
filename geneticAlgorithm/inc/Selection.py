import random as rn


def selection(population, best=True, random=False):
    populationCopy = population.copy()
    func = rn.randint(0, 2)
    if func == 0:
        search = binaryTournamentSelection
    elif func == 1:
        search = proportionalSelection
    else:
        search = sliceTournamentSelection

    if random:
        search = proportionalSelection

    firstEntity = search(populationCopy, best)
    populationCopy.getPopulation().remove(firstEntity)
    secondEntity = search(populationCopy, best)
    return [firstEntity, secondEntity]


def binaryTournamentSelection(population, best=True):
    choice = -1
    if not best:
        choice = 0

    entityNumber = len(population.getPopulation())
    firstEntity = rn.randint(0, entityNumber - 1)
    secondEntity = rn.randint(0, entityNumber - 1)
    while firstEntity == secondEntity:
        secondEntity = rn.randint(0, entityNumber - 1)
    pair = [population.getPopulation()[firstEntity], population.getPopulation()[secondEntity]]
    return sorted(pair, key=lambda x: x.getSuitability())[choice]


def sliceTournamentSelection(population_, best=True):
    choice = -1
    if not best:
        choice = 0

    population = population_.getPopulation()
    if len(population) == 1:
        return population[0]

    startOffset = 0
    endOffset = 1
    if len(population) >= 3:
        startOffset = rn.randint(0, int(len(population) / 2 - 1))
        endOffset = rn.randint(startOffset + 1, len(population) - 1)

    best_entity = sorted(population[startOffset: endOffset], key=lambda x: x.getSuitability())[choice]
    return best_entity


def proportionalSelection(population, best=True):
    wheelOfFortune = []
    population_array = population.getPopulation()
    if len(population_array) == 1:
        return population_array[0]
    else:
        wheelOfFortune.append(population_array[0].getSuitability())

    for i in range(1, len(population_array)):
        wheelOfFortune.append(population_array[i].getSuitability() + wheelOfFortune[i-1])

    randomSuitability = rn.randint(0, wheelOfFortune[-1])
    i = 0
    while randomSuitability > wheelOfFortune[i]:
        i += 1
    return population_array[i]
