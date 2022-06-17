from geneticAlgorithm.src.Population import Population
from geneticAlgorithm.inc.Crossover import crossover
from geneticAlgorithm.inc.Selection import selection, binaryTournamentSelection
from geneticAlgorithm.src.Entity import Entity
import random


def generationChange(population, statistic):
    newPopulation = Population(population.getCondition())
    entityNumber = len(population.getPopulation())
    oldEntityNumber = int(entityNumber * 0.1)
    i = 0
    populationCopy = population.copy()
    # Best entity
    while i < int((entityNumber - oldEntityNumber) * 0.7):
        pair = selection(populationCopy, True)
        newGene = crossover(pair, population.getCondition())
        newEntity = Entity(newGene)
        newPopulation.addEntity(newEntity)
        entityForRemove = random.randint(0, 1)
        populationCopy.getPopulation().remove(pair[entityForRemove])
        i += 1

    # Худшие
    while i < int((entityNumber - oldEntityNumber) * 0.8):
        pair = selection(populationCopy, False)
        newGene = crossover(pair, population.getCondition())
        newEntity = Entity(newGene)
        newPopulation.addEntity(newEntity)
        entityForRemove = random.randint(0, 1)
        populationCopy.getPopulation().remove(pair[entityForRemove])
        i += 1

    # Случайные
    while i < int((entityNumber - oldEntityNumber) * 0.9):
        pair = selection(populationCopy, False, True)
        newGene = crossover(pair, population.getCondition())
        newEntity = Entity(newGene)
        newPopulation.addEntity(newEntity)
        entityForRemove = random.randint(0, 1)
        populationCopy.getPopulation().remove(pair[entityForRemove])
        i += 1

    # Лучшие старые
    while i < entityNumber:
        oldEntity = binaryTournamentSelection(population)
        newPopulation.addEntity(oldEntity)
        population.population_.remove(oldEntity)
        i += 1

    #statistic.append(newPopulation.getMaxSuitability())
    #statistic.append(newPopulation.getAverageSuitability())
    return newPopulation
