class Gene:
    def __init__(self, weight, cost, state):
        self.weight_ = weight
        self.cost_ = cost
        self.state_ = state
        self.coefficient_ = cost/weight

    def getWeight(self):
        return self.weight_

    def getCost(self):
        return self.cost_

    def getState(self):
        return self.state_

    def getCoefficient(self):
        return self.coefficient_

