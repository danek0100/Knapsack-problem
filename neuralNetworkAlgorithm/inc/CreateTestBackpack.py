import random as rn

from geneticAlgorithm.src.Item import Item


def generateDataWithAnswer(volume, b=0, max_cost=100):
    if b == 0:
        b = rn.randint(volume/2, volume * 10)
    k = rn.randint(volume/10, volume-1)
    k_index = set()
    while len(k_index) < k:
        k_index.add(rn.randint(0, volume-1))
    print("Indexes = " + str(k_index))
    k_mass = [0 for _ in range(volume)]
    k_cost = [0 for _ in range(volume)]
    sum_m = 0
    added_m = 0
    sum_cost = 0
    for index in k_index:
        if added_m == k - 1:
            k_mass[index] = b - sum_m
            k_cost[index] = rn.randint(max_cost // 2, max_cost)
            sum_cost += k_cost[index]
            break
        k_mass[index] = rn.randint(b // k - rn.randint(0, b // k // 3), b // k + rn.randint(0, b // k // 2))
        k_cost[index] = rn.randint(max_cost // 2, max_cost)
        sum_m += k_mass[index]
        sum_cost += k_cost[index]
        added_m += 1

    for i in range(volume):
        if k_mass[i] == 0:
            k_mass[i] = rn.randint(b // k - rn.randint(0, b // k // 10), b)
            #k_mass[i] = rn.randint(1, b)
            k_cost[i] = rn.randint(rn.randint(0, sum_cost // volume - k - 1), sum_cost // volume - k)

    itemsArray = []
    i = 0
    while i < volume:
        itemsArray.append(Item(k_mass[i], k_cost[i], 0))
        i += 1
    return itemsArray, sum_cost
