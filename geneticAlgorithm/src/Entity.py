class Entity:
    def __init__(self, chromosome):
        self.chromosome_ = chromosome
        self.suitability_ = self.chromosome_.calculateSuitability()
        self.sumWeight_ = self.chromosome_.calculateSumWeight()

    def getChromosome(self):
        return self.chromosome_

    def getSuitability(self):
        return self.suitability_

    def getSumWeight(self):
        return self.sumWeight_
