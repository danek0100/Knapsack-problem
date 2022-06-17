import random as rn
from geneticAlgorithm.src.Chromosome import Chromosome
from geneticAlgorithm.src.Gene import Gene


def mutation(chromosome, condition):
    prob = rn.randint(0, 1000)
    if prob < 10:
        while True:
            gene = chromosome.getGenes()[rn.randint(0, len(chromosome.getGenes()) - 1)]
            if gene.state_ == 0:
                gene.state_ = 1
                if chromosome.calculateSumWeight() < condition:
                    break
                else:
                    gene.state_ = 0
            else:
                gene.state_ = 0
                if chromosome.calculateSumWeight() < condition:
                    break


def crossover(entityPair, condition):
    geneLength = len(entityPair[0].getChromosome().getGenes())
    breakPoint = rn.randint(1, geneLength-2)
    genes = []
    newChromosome = Chromosome(genes)
    for i in range(breakPoint):
        newGene = Gene(entityPair[0].getChromosome().getGenes()[i].getWeight(),
                       entityPair[0].getChromosome().getGenes()[i].getCost(),
                       entityPair[0].getChromosome().getGenes()[i].getState())

        newChromosome.addGene(newGene)

    for j in range(breakPoint, geneLength):
        newGene = Gene(entityPair[1].getChromosome().getGenes()[j].getWeight(),
                       entityPair[1].getChromosome().getGenes()[j].getCost(),
                       entityPair[1].getChromosome().getGenes()[j].getState())

        newChromosome.addGene(newGene)

    sumWeight = newChromosome.calculateSumWeight()
    i = 0
    while condition < sumWeight and i < len(genes):
        if newChromosome.genes_[i].state_ == 1:
            newChromosome.genes_[i].state_ = 0
            sumWeight -= newChromosome.genes_[i].getWeight()
        i += 1

    mutation(newChromosome, condition)
    return newChromosome
