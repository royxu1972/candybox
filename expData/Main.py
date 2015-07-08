from Stats import Stats
from Case import Case
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

orders = ["random", "coverage", "switch-greedy", "switch-GA", "switch-LKH", "Hybrid", "NSGA-II"]

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
                self.statsName.append( orders[i] + " Vs. " + orders[j] )

        # the following data is used to create box plot
        # |cases| * |orders|
        self.box_Cost = np.zeros(shape=(end-begin+1, 7))
        self.box_RFD = np.zeros(shape=(end-begin+1, 7))
        self.box_EPSILON = np.zeros(shape=(end-begin+1, 7))
        self.box_IGD = np.zeros(shape=(end-begin+1, 7))
        self.box_Ft = np.zeros(shape=(end-begin+1, 7))

        # scan file
        self.scanFiles(begin, end)


    def printStats(self):
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
        print(str)

    def printMeanBox(self):
        print("Cost Box")
        print(self.box_Cost)
        print("\nRFD Box")
        print(self.box_RFD)
        print("\nEPSILON Box")
        print(self.box_EPSILON)
        print("\nIGD Box")
        print(self.box_IGD)
        print("\nFt Box")
        print(self.box_Ft)


    def scanFiles(self, begin, end):
        for index in range(begin, end+1):
            case = Case( index, orders, "data//" + str(index) + ".txt" )
            stats = Stats(case)

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

    def boxplot(self, name):
        sel = { "Cost"    : self.box_Cost,
                "RFD"     : self.box_RFD,
                "EPSILON" : self.box_EPSILON,
                "IGD"     : self.box_IGD,
                "Ft"      : self.box_IGD }
        data = sel[name]
        plt.figure( figsize=(10, 5) )
        plt.boxplot(data)
        plt.xticks([x+1 for x in range(0, len(orders))],
                   orders,
                   rotation=20)
        plt.ylim([-0.1,1.1])
        plt.tight_layout()
        plt.show()


if __name__=='__main__':
    exp = Exp(0, 10)
    #exp.printMeanBox()
    exp.boxplot("Cost")



    #k = Case("0", orders, "data//0.txt")
    #print(k)
    #s = Stats(k)
    #print(s)
