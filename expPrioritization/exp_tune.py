import plot.baseplot as bp
import numpy as np

titles = ["GA", "NSGA"]
legend = ["Case 1", "Case 2", "Case 3", "Case 4", "Case 5"]
xlabels = ["population size", "maximum number of iteration", "crossover rate", "mutation rate", "population * iteration"]
ylabel = ["total switching cost", "distance to the ideal order"]
xSticks = [["10", "20", "30", "40", "60", "80", "100"],
           ["50", "100", "200", "400", "600", "800", "1000", "1300", "1500", "2000"],
           ["0.1", "0.3", "0.5", "0.7", "0.9"],
           ["0.1", "0.3", "0.5", "0.7", "0.9"],
           ["10*3600", "20*1800", "30*1200", "40*900", "60*600", "80*450", "100*360"]
          ]
style = ["k8-", "k^-", "ks-", "kD-", "k*-"]

def readFile(name):
    f = open(name, 'r')
    lines = f.readlines()

    # population, iteration, crossover, mutation, fitnessEvaluation
    index = [4, 11, 18, 25, 32]
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
dataNSGA = readFile('tuning/nsga.txt')
i = 3

print(dataGA[i])
plt = bp.BasePlot()
plt.lines([dataGA[i], dataNSGA[i]], titles, xlabels[i], ylabel, xSticks[i], legend, style, norm=True)

#a.line(data1, "xx", "yy", xStick, legend, style, norm=True)
#a.lines([data1, data2], ["t1", "t2"], "xx", "yy", xStick, legend, style, norm=True)