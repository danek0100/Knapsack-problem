import matplotlib.pyplot as plt


def printItems(items):
    for item in items:
        print("Weight = " + str(item.weight_) + " | Cost = " + str(item.cost_) + " | State = " + str(item.state_))


def printGraphAnswerToOpt(optimum, data):
    plt.title('Timed answer to optimum')
    optimum_array = [optimum for _ in range(len(data))]
    #time = [i for i in range(len(data))]
    plt.plot(optimum_array)
    plt.plot(data)
    plt.show()


def printTimeGraph(x, y):
    plt.title('Average Time')
    plt.plot(x, y)
    plt.xscale('log', base=10)
    plt.show()


def printAverageAnswerClear(x, y):
    plt.title('Average Answer')
    plt.plot(x, y)
    plt.xscale('log', base=10)
    plt.show()
