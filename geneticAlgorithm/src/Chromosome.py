import random as rn


class Chromosome:
    def __init__(self, genes=None):
        if genes is None:
            genes = []
        self.genes_ = genes

    def calculateSuitability(self):
        suitability = 0
        for gene in self.genes_:
            if gene.state_:
                suitability += gene.cost_
        return suitability

    def calculateSumWeight(self):
        weight = 0
        for gene in self.genes_:
            if gene.state_:
                weight += gene.weight_
        return weight

    def shuffleGene(self, condition):
        addedGenes = 0
        while self.calculateSumWeight() <= condition and addedGenes != len(self.genes_):
            geneId = rn.randint(0, len(self.genes_) - 1)
            self.genes_[geneId].state_ = 1
            if self.calculateSumWeight() > condition:
                self.genes_[geneId].state_ = 0
                break
            addedGenes += 1
        return self

    def getGenes(self):
        return self.genes_

    def addGene(self, item):
        self.genes_.append(item)
