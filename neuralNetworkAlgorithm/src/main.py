from geneticAlgorithm.inc.CreateTestBackpack import generateDataWithAnswer
from geneticAlgorithm.inc.PrintFunctions import *
from neuralNetworkAlgorithm.inc.Functions import *
#from neuralNetworkAlgorithm.inc.GenerateRandomData import *
from geneticAlgorithm.inc.GenerateRandomData import *
import time
import random as rn


i = 100000
T_start = 10
T_param = 0.95
T_step = 3
T_par = 2.0
a_param = 0.1
iteration_num = 1
#maxiter = 1000000
maxCycleNumber = 300
condition_array_x = []
condition_array_y = []
time_array_x = []
time_array_y = []
averageCycleNumber = []
i_max = 1000001
while i < i_max:
    sum_time = 0.0
    sum_optimum = 0.0
    sum_answer = 0.0
    sum_cycleNumber = 0
    #iteration_num = int(maxiter / i / 2)
    #if iteration_num > 100:
    #    iteration_num = 50
   #if i == 100000:
   #     iteration_num = 1
    for j in range(iteration_num):
        condition = rn.randint(i, i * 10)
        data, answer = generateDataWithAnswer(i, condition, i * 10)
        #condition = rn.randint(50, 400)
        #data = generateRandomData(i)
        #answer = i*10
        N = len(data)
        high_board = (len(data) - 1) / len(data)
        start = time.time()
        print("Answer = " + str(answer))
        print("Condition = " + str(condition))
        vector = [0.5 for _ in range(i)]
        T = T_start
        statistic = []
        try_ = 0
        for cycleNumber in range(maxCycleNumber):
            old_vector = vector.copy()
            vector = generationChange(vector, a_param / T, data, T, condition, statistic)
            saturation = getSaturation(vector)
            #if saturation > 0.999 and getEvolutionRate(vector, old_vector) < 0.00001:
                #if decodeAnswer(vector, data)[1] > condition:
                    #a_param *= 1.5
                    #cycleNumber = 0
                    #vector = [0.5 for _ in range(i)]
                    #T = T_start
             #       if 0.1 < saturation < high_board:
             #           T *= 0.985
             #       else:
             #           T *= T_param
             #       continue
             #   sum_cycleNumber += cycleNumber
             #   break
            #if cycleNumber % T_step == 0:
                #T /= T_par
            if 0.1 < saturation < high_board:
                T *= 0.985
            else:
                T *= T_param

        sum_time += time.time() - start
        print("\n--------------------------------------\nAnswer = " + str(decodeAnswer(vector.copy(), data)[0]) + "\nWeight = "
              + str(decodeAnswer(vector, data)[1]) + "\n--------------------------------------\n")
        sum_optimum += answer
        sum_answer += decodeAnswer(vector.copy(), data)[0]
        printGraphAnswerToOpt(answer, statistic)

    time_array_y.append(sum_time/iteration_num)
    time_array_x.append(i)
    condition_array_x.append(i)
    condition_array_y.append(sum_answer/sum_optimum)
    #averageCycleNumber.append(sum_cycleNumber / iteration_num)
    if i < 100:
        i = 10
    i *= 10

print(time_array_y)
print(condition_array_y)
print(averageCycleNumber)
printTimeGraph(time_array_x, time_array_y)
printAverageAnswerClear(condition_array_x, condition_array_y)
