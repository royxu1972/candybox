import plot.baseplot as bp
import numpy as np

titles = ["GA", "NSGA"]
legend = ["Case 1", "Case 2", "Case 3", "Case 4", "Case 5"]
xlabels = ["population", "iteration", "crossover rate", "mutation rate"]
ylabel = "indicator"
xSticks = [[10, 20, 30, 40, 60, 80, 100],
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           [1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5]
          ]
style = ["k-", "k.-", "k+-", "ks-", "kd-"]

def readFile(name):
    f = open(name, 'r')
    lines = f.readlines()

    # population, iteration, crossover, mutation
    index = [4, 11, 18, 25]
    case = 5

    data = []
    for i in range(0, len(index)):
        eachParameter = np.empty((case, len(xSticks[i])))
        for j in range(0, case):
            line = lines[index[i]+j].strip()[8:]
            eachParameter[j] = np.fromstring(line, dtype=float, sep=' ')
        data.append(eachParameter)

    return data



dataGA = readFile('tuning/ga.txt')
i = 3

print(dataGA[i])

plt = bp.BasePlot()
plt.lines([dataGA[i], dataGA[i]], titles, xlabels[i], ylabel, xSticks[i], legend, style, norm=True)


#a.line(data1, "xx", "yy", xStick, legend, style, norm=True)
#a.lines([data1, data2], ["t1", "t2"], "xx", "yy", xStick, legend, style, norm=True)