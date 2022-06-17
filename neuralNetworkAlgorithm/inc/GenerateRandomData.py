import random as rn

from neuralNetworkAlgorithm.inc import Item


def generateRandomData(items_number):
    itemsArray = []
    i = 0
    while i < items_number:
        itemsArray.append(Item(rn.randint(1, 100), rn.randint(1, 100), 0))
        i += 1
    return itemsArray
