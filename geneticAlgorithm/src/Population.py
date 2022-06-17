from geneticAlgorithm.inc.PrintFunctions import printItems


class Population:
    def __init__(self, condition=0, population=None):
        if population is None:
            population = []
        self.population_ = population
        self.condition_ = condition

    def addEntity(self, entity):
        self.population_.append(entity)

    def getPopulation(self):
        return self.population_

    def checkAnswer(self):
        for i in range(1, len(self.population_)):
            if self.population_[i].getSumWeight() == \
                    self.population_[i - 1].getSumWeight() and \
                    self.population_[i].getSumWeight() == \
                    self.population_[i - 1].getSuitability():
                continue
            else:
                return False
        return True

    def printPopulation(self):
        for i in range(len(self.population_)):
            print('\n')
            print("Entity = " + str(i) + " | SumWeight = " + str(
                self.population_[i].getSumWeight()) + " | Suitability = " + str(
                self.population_[i].getSuitability()))
            print("----------------------------------------------")
            items = self.population_[i].gene_.itemsChair_
            printItems(items)

    def printOneEntity(self, i):
        print("Entity = " + str(i) + " | SumWeight = " + str(
            self.population_[i].getSumWeight()) + " | Suitability = " + str(
            self.population_[i].getSuitability()))
        print("----------------------------------------------")
        items = self.population_[i].gene_.genes_
        printItems(items)

    def checkCondition(self, sumWeight):
        if sumWeight > self.condition_:
            return False
        else:
            return True

    def getCondition(self):
        return self.condition_

    def getResult(self):
        return "Max Suitability = " + str(self.getMaxSuitability())

    def getMaxSuitability(self):
        maxSuitability = 0
        for entity in self.population_:
            if entity.getSuitability() > maxSuitability:
                maxSuitability = entity.getSuitability()
        return maxSuitability

    def getAverageSuitability(self):
        sumSuitability = 0
        numberEntity = len(self.population_)
        for entity in self.population_:
            sumSuitability += entity.getSuitability()
        return sumSuitability / numberEntity

    def copy(self):
        newPopulation = Population(self.condition_)
        for entity in self.population_:
            newPopulation.addEntity(entity)
        return newPopulation
