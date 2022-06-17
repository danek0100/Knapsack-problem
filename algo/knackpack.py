import queue
import functools


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.coef = value/weight


class Node:
    def __init__(self, level, profit, bound_, weight):
        self.level = level
        self.profit = profit
        self.bound = bound_
        self.weight = weight

def cmp(a):
    return a.coef


def bound(node, coef, max_weight, items_):
    if node.weight >= max_weight:
        return 0

    profit_bound = node.profit

    j = node.level + 1
    totweight = node.weight

    while (j < coef) and (totweight + items_[j].weight <= max_weight):
        totweight += items_[j].weight
        profit_bound += items_[j].value
        j += 1

    if j < coef:
        profit_bound += (max_weight - totweight) * items_[j].value / items_[j].weight

    return profit_bound


def knapsack(max_weight, items_, coef):
    items_.sort(key=cmp, reverse=True)

    Q = queue.Queue()
    node_u = Node(-1, 0, 0, 0)
    node_v = Node(-1, 0, 0, 0)
    Q.put(node_u)
    maxProfit = 0

    while not Q.empty():
        node_u = Q.get()

        if node_u.level == -1:
            node_v.level = 0

        if node_u.level == coef - 1:
            continue

        node_v.level = node_u.level + 1

        node_v.weight = node_u.weight + items_[node_v.level].weight
        node_v.profit = node_u.profit + items_[node_v.level].value

        if node_v.weight <= max_weight and node_v.profit > maxProfit:
            maxProfit = node_v.profit

        node_v.bound = bound(node_v, coef, max_weight, items_)

        if node_v.bound > maxProfit:
            Q.put(Node(node_v.level, node_v.profit, node_v.bound, node_v.weight))

            node_v.weight = node_u.weight
            node_v.profit = node_u.profit
            node_v.bound = bound(node_v, coef, max_weight, items_)
            if node_v.bound > maxProfit:
                Q.put(Node(node_v.level, node_v.profit, node_v.bound, node_v.weight))

    return maxProfit


W = 10
items = [Item(2, 40), Item(3.14, 50), Item(1.98, 100), Item(5, 95), Item(3, 30)]

n = len(items)

print("Maximum possible profit = " + str(knapsack(W, items, n)))