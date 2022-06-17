from geneticAlgorithm.src.Population import Population
from geneticAlgorithm.src.Chromosome import Chromosome
from geneticAlgorithm.src.Entity import Entity
from geneticAlgorithm.src.Gene import Gene


def generateFirstGeneration(items_data, entities_number, condition):
    population = Population(condition)
    i = 0
    while i < entities_number:
        newGenes = []
        for item in items_data:
            newGene = Gene(item.weight_, item.cost_, item.state_)
            newGenes.append(newGene)
        chromosome = Chromosome(newGenes).shuffleGene(condition)
        entity = Entity(chromosome)
        population.addEntity(entity)
        i += 1
    return population
