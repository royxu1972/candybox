from Stats import Stats
from Case import Case
import numpy as np
import matplotlib.pyplot as plt

ORDERS = ["random", "coverage", "switch-greedy", "switch-GA", "switch-LKH", "Hybrid", "NSGA-II"]

class Exp:

    def __init__(self, begin, end):
        # the following data is used to create the very stats table
        # + / = / -
        self.exp_Cost = np.zeros(shape=(21,3))
        self.exp_RFD = np.zeros(shape=(21,3))
        self.exps_EPSILON = np.zeros(shape=(21,3))
        self.exp_IGD = np.zeros(shape=(21,3))
        self.exp_Ft = np.zeros(shape=(21,3))

        self.statsName = []
        for i in range(6,-1,-1):
            for j in range(i-1,-1,-1):
                self.statsName.append( ORDERS[i] + " Vs. " + ORDERS[j] )

        # the following data is used to create box plot
        # |cases| * |orders|
        self.box_Cost = np.zeros(shape=(end-begin+1, 7))
        self.box_RFD = np.zeros(shape=(end-begin+1, 7))
        self.box_EPSILON = np.zeros(shape=(end-begin+1, 7))
        self.box_IGD = np.zeros(shape=(end-begin+1, 7))
        self.box_Ft = np.zeros(shape=(end-begin+1, 7))

        # the best orders in term of Ft
        self.bestMeanFt = []    # which has the minimum mean value
        self.bestStatsFt = []   # which significantly outperforms others

        # scan file
        self.scanFiles(begin, end)


    def writeStats(self):
        str = "# Stats Cost + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exp_Cost[k]) + " " + self.statsName[k] + "\n"
        str += "\n# Stats RFD + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exp_RFD[k]) + " " + self.statsName[k] + "\n"
        str += "\n# Stats EPSILON + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exps_EPSILON[k]) + " " + self.statsName[k] + "\n"
        str += "\n# Stats IGD + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exp_IGD[k]) + " " + self.statsName[k] + "\n"
        str += "\n# Stats Ft + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exp_Ft[k]) + " " + self.statsName[k] + "\n"
        f = open('stats.data','w')
        f.write(str)
        f.close()

    def printMeanBox(self):
        print("Cost Box");print(self.box_Cost)
        print("\nRFD Box");print(self.box_RFD)
        print("\nEPSILON Box");print(self.box_EPSILON)
        print("\nIGD Box");print(self.box_IGD)
        print("\nFt Box");print(self.box_Ft)

    def writeBestOrder(self):
        f = open('order.data','w')
        f.write("  #   [Mean Value]   [Stats Best]\n")
        for i in range(0, len(self.bestMeanFt)):
            so = self.bestStatsFt[i]
            if so == None:
                so = "None"
            f.write('{0:>3}'.format(i) + '{0:>12}'.format(self.bestMeanFt[i]) + '{0:>14}'.format(so) + '\n')
        f.close()

    def scanFiles(self, begin, end):
        for index in range(begin, end+1):
            case = Case( index, ORDERS, "data//" + str(index) + ".txt" )
            stats = Stats(case)

            # best
            self.bestMeanFt.append( case.bestFtOrder )
            self.bestStatsFt.append( stats.bestFtOrder )

            # + / = / -
            self.exp_Cost += stats.Table_Cost
            self.exp_RFD += stats.Table_RFD
            self.exps_EPSILON += stats.Table_EPSILON
            self.exp_IGD += stats.Table_IGD
            self.exp_Ft += stats.Table_Ft

            # mean box plot
            self.box_Cost[index] = case.Cost_Mean
            self.box_RFD[index] = case.RFD_Mean
            self.box_EPSILON[index] = case.EPSILON_Mean
            self.box_IGD[index] = case.IGD_Mean
            self.box_Ft[index] = case.Ft_Mean

    def boxPlots(self, names):
        for each in names:
            self.boxPlot(each)

    def boxPlot(self, name):
        sel = { "Cost"    : self.box_Cost,
                "RFD"     : self.box_RFD,
                "EPSILON" : self.box_EPSILON,
                "IGD"     : self.box_IGD,
                "Ft"      : self.box_Ft }
        data = sel[name]
        fig = plt.figure( figsize=(10, 5) )
        plt.boxplot(data)
        plt.xticks([x+1 for x in range(0, len(ORDERS))],
                   ORDERS,
                   rotation=20)
        plt.ylim([-0.1,1.1])
        plt.tight_layout()
        fig.canvas.set_window_title(name)
        plt.show()


if __name__=='__main__':
    exp = Exp(0, 58)
    #exp.boxPlot("Cost")
    #exp.printStats()
    exp.writeStats()
    exp.writeBestOrder()
    exp.boxPlots(["Cost", "RFD", "EPSILON", "IGD", "Ft"])
