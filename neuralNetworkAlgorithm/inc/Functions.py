import numpy as np


def g(x, T_):
    return 0.5 * (1 + np.tanh(x/T_))


def getDifference(x):
    if x <= 0:
        return 0
    else:
        return x


def generationChange(v, a, items, T_, condition_, statistic_):
    x = 0
    for i_ in range(len(v)):
        x += items[i_].getWeight() * v[i_]

    for k in range(len(v)):
        x -= items[k].getWeight() * v[k]
        x1 = x + items[k].getWeight() - condition_
        x2 = x - condition_

        vk = items[k].getCost() - a * ((x1 * getDifference(x1))-(x2 * getDifference(x2)))
        v[k] = g(vk, T_)
        x += items[k].getWeight() * v[k]

    statistic_.append(decodeAnswer(v.copy(), items)[0])
    return v


def decodeAnswer(vector, data):
    m_answer = 0
    m_weight = 0
    for i in range(len(vector)):
        vector[i] = int(vector[i])
        if vector[i] == 1:
            m_answer += data[i].getCost()
            m_weight += data[i].getWeight()
    return m_answer, m_weight


def getSaturation(v):
    saturation = 0.0
    for vi in v:
        saturation += (vi - 0.5) ** 2
    return (4.0 / len(v)) * saturation


def getEvolutionRate(v, v_old):
    evoRate = 0.0
    for i in range(len(v)):
        evoRate += (v[i] - v_old[i]) ** 2
    return (10.0/len(v)) * evoRate

