class Item:
    def __init__(self, weight, cost, state):
        self.weight_ = weight
        self.cost_ = cost
        self.state_ = state

    def getWeight(self):
        return self.weight_

    def getCost(self):
        return self.cost_

    def getState(self):
        return self.state_

