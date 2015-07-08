import numpy as np
from scipy import stats
import operator

class Stats:

    def __init__(self, case):
        self.case = case

        # p-values of Wilcoxon test
        self.Wilcox_Cost = self.statsUpdarte(case.Cost, operator.le)
        self.Wilcox_RFD = self.statsUpdarte(case.RFD, operator.ge)
        self.Wilcox_EPSILON = self.statsUpdarte(case.EPSILON, operator.le)
        self.Wilcox_IGD = self.statsUpdarte(case.IGD, operator.le)
        self.Wilcox_Ft = self.statsUpdarte(case.Ft, operator.le)

        # the name list of alg(A) Vs. alg(B)
        self.statsName = []
        for i in range(6, -1, -1):
            for j in range(i-1, -1, -1):
                self.statsName.append( case.orders[i] + " Vs. " + case.orders[j] )

        # the very table of each metric
        self.Table_Cost = self.updateTable(self.Wilcox_Cost)
        self.Table_RFD = self.updateTable(self.Wilcox_RFD)
        self.Table_EPSILON = self.updateTable(self.Wilcox_EPSILON)
        self.Table_IGD = self.updateTable(self.Wilcox_IGD)
        self.Table_Ft = self.updateTable(self.Wilcox_Ft)

    def __str__(self):
        str = "Cost as + \  = \  -\n"
        for k in range(0, 21):
            str += np.array_repr(self.Table_Cost[k]) + " " + self.statsName[k] + "\n"
        str += "\nRFD as + \  = \  -\n"
        for k in range(0, 21):
            str += np.array_repr(self.Table_RFD[k]) + " " + self.statsName[k] + "\n"
        str += "\nEPISILON as + \  = \  -\n"
        for k in range(0, 21):
            str += np.array_repr(self.Table_EPSILON[k]) + " " + self.statsName[k] + "\n"
        str += "\nIGD as + \  = \  -\n"
        for k in range(0, 21):
            str += np.array_repr(self.Table_IGD[k]) + " " + self.statsName[k] + "\n"
        str += "\nFt as + \  = \  -\n"
        for k in range(0, 21):
            str += np.array_repr(self.Table_Ft[k]) + " " + self.statsName[k] + "\n"
        return str

    def statsUpdarte(self, arr, opt):
        """
        :parameter
            arr -- an |orders| * 30 ndarray
            opt -- operator, indicating how to compare a and b
        :return
            sta -- an |orders| * |orders| list, where sta[i][j] = + / = / -,
                   representing alg[i] is better / equal / worse than alg[j]
        """
        sta = []
        length = len(self.case.orders)

        for alg1 in range(0, length):
            tp = []
            for alg2 in range(0, length):
                if alg1 == alg2 :
                    tp.append( "\\" )
                else:
                    x1 = arr[alg1]
                    x2 = arr[alg2]
                    if np.array_equal(x1, x2):  # same value array
                        tp.append("=")
                    else:
                        [T, p] = stats.wilcoxon(x1, x2, zero_method='wilcox')
                        if p <= 0.05 :
                            if opt( x1.mean(), x2.mean() ):
                                tp.append("+")  # alg1 is better than alg2
                            else:
                                tp.append("-")  # alg1 is worse than alg2
                        else:
                            tp.append("=")  # alg1 is equal to alg2
            sta.append(tp)
        #for each in sta:
        #    print(each)
        return sta

    def updateTable(self, stats):
        """
        :parameter
            stats -- an |orders| * |orders| list
        :return
            tb -- ndarray, an pair-wise comparison between any
                  two algorithms (the order based on self.statsName)
        """
        # each column represents + / = / -
        # each row represents a algorithm pair
        tb = np.zeros(shape=(21,3))
        index = 0
        for i in range(6, -1, -1):
            for j in range(i-1, -1, -1):
                if stats[i][j] == "+":
                    tb[index][0] = 1
                elif stats[i][j] == "=":
                    tb[index][1] = 1
                elif stats[i][j] == "-":
                    tb[index][2] = 1
                else:
                    print("ERROR in updateTable")
                index += 1
        return tb