from geneticAlgorithm.inc.CreateTestBackpack import generateDataWithAnswer
from geneticAlgorithm.inc.GenerateFirstGeneration import generateFirstGeneration
from geneticAlgorithm.inc.PrintFunctions import printGraphAnswerToOpt, printTimeGraph, printAverageAnswerClear
from geneticAlgorithm.inc.GenerationChange import generationChange
import random as rn
import time


i = 100
entity_num = 1000
iteration_num = 1
Tm = 100
condition_array_x = []
condition_array_y = []
time_array_x = []
time_array_y = []
i_max = 101
while i < i_max:
    sum_time = 0.0
    sum_optimum = 0.0
    sum_answer = 0.0
    for j in range(iteration_num):
        condition = rn.randint(i, i * 10)
        data, answer = generateDataWithAnswer(i, condition, i * 10)
        start = time.time()
        data = sorted(data[:], key=lambda x: x.getCoefficient())
        print("Answer = " + str(answer))
        print("Condition = " + str(condition))
        population = generateFirstGeneration(data, entity_num, condition)
        statistic = []
        for generationNumber in range(Tm):
            population = generationChange(population, statistic)
        sum_time += time.time() - start
        print("\n--------------------------------------\n" + population.getResult() + "\n--------------------------------------\n")
        sum_optimum += answer
        sum_answer += population.getMaxSuitability()
        #printGraphAnswerToOpt(answer, statistic)
    time_array_y.append(sum_time/iteration_num)
    time_array_x.append(i)
    condition_array_x.append(i)
    condition_array_y.append(sum_answer/sum_optimum)
    i *= 10

print(time_array_y)
print(condition_array_y)
printTimeGraph(time_array_x, time_array_y)
printAverageAnswerClear(condition_array_x, condition_array_y)
