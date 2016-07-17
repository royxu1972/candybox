import baseplot as bp
from stats import Stats
from case import Case
import numpy as np
import matplotlib.pyplot as plt

ORDERS = ["random", "coverage", "switch-greedy", "switch-GA", "switch-LKH", "Hybrid", "NSGA-II"]

class Exp:

    def __init__(self, begin, end):
        # the following data is used to create the very stats table
        # + / = / -
        self.exp_Cost = np.zeros(shape=(21,3))
        self.exp_RFD = np.zeros(shape=(21,3))
        self.exp_EPSILON = np.zeros(shape=(21,3))
        self.exp_IGD = np.zeros(shape=(21,3))
        self.exp_Ft = np.zeros(shape=(21,3))
        self.exp_RFDc = np.zeros(shape=(21,3))

        self.statsName = []
        for i in range(6,-1,-1):
            for j in range(i-1,-1,-1):
                self.statsName.append( ORDERS[i] + " vs " + ORDERS[j] )

        # the following data is used to create box plot
        # |cases| * |orders|
        self.box_Cost = np.zeros(shape=(end-begin+1, 7))
        self.box_RFD = np.zeros(shape=(end-begin+1, 7))
        self.box_EPSILON = np.zeros(shape=(end-begin+1, 7))
        self.box_IGD = np.zeros(shape=(end-begin+1, 7))
        self.box_Ft = np.zeros(shape=(end-begin+1, 7))
        self.box_RFDc = np.zeros(shape=(end-begin+1, 7))

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
            str += np.array_repr(self.exp_EPSILON[k]) + " " + self.statsName[k] + "\n"
        str += "\n# Stats IGD + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exp_IGD[k]) + " " + self.statsName[k] + "\n"
        str += "\n# Stats Ft + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exp_Ft[k]) + " " + self.statsName[k] + "\n"
        str += "\n# Stats RFDc + / = / -\n"
        for k in range(0, 21):
            str += np.array_repr(self.exp_RFDc[k]) + " " + self.statsName[k] + "\n"

        f = open('stats.data','w')
        f.write(str)
        f.close()

    def writeStatsLatex(self):
        ss = ""
        for k in range(0, 21):
            ss += self.statsName[k] + " & "
            # RFD
            ss += str(self.exp_RFD[k][0].astype(int)) + " & / & " + \
                  str(self.exp_RFD[k][1].astype(int)) + " & / & " + \
                  str(self.exp_RFD[k][2].astype(int)) + " & "
            # cost
            ss += str(self.exp_Cost[k][0].astype(int)) + "& / &" + \
                  str(self.exp_Cost[k][1].astype(int)) + " & / & " + \
                  str(self.exp_Cost[k][2].astype(int)) + " & "
            # epsilon
            ss += str(self.exp_EPSILON[k][0].astype(int)) + " & / & " + \
                  str(self.exp_EPSILON[k][1].astype(int)) + " & / & " + \
                  str(self.exp_EPSILON[k][2].astype(int)) + " & "
            # igd
            ss += str(self.exp_IGD[k][0].astype(int)) + " & / & " + \
                  str(self.exp_IGD[k][1].astype(int)) + " & / & " + \
                  str(self.exp_IGD[k][2].astype(int))
            ss += "\\\ \n"
        print(ss)
        print("\n\n")

        ss = ""
        for k in range(0, 21):
            ss += self.statsName[k] + " & "
            # RFDc
            ss += str(self.exp_RFDc[k][0].astype(int)) + " & / & " + \
                  str(self.exp_RFDc[k][1].astype(int)) + " & / & " + \
                  str(self.exp_RFDc[k][2].astype(int)) + " & "
            # ft
            ss += str(self.exp_Ft[k][0].astype(int)) + " & / & " + \
                  str(self.exp_Ft[k][1].astype(int)) + " & / & " + \
                  str(self.exp_Ft[k][2].astype(int))
            ss += "\\\ \n"
        print(ss)


    def printMeanBox(self):
        print("Cost Box");print(self.box_Cost)
        print("\nRFD Box");print(self.box_RFD)
        print("\nEPSILON Box");print(self.box_EPSILON)
        print("\nIGD Box");print(self.box_IGD)
        print("\nFt Box");print(self.box_Ft)
        print("\nRFDc Box");print(self.box_RFDc)


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
            case = Case( str(index), ORDERS, "data//" + str(index) + ".txt" )
            stats = Stats(case)

            # best
            self.bestMeanFt.append( case.bestFtOrder )
            self.bestStatsFt.append( stats.bestFtOrder )

            # + / = / -
            self.exp_Cost += stats.Table_Cost
            self.exp_RFD += stats.Table_RFD
            self.exp_EPSILON += stats.Table_EPSILON
            self.exp_IGD += stats.Table_IGD
            self.exp_Ft += stats.Table_Ft
            self.exp_RFDc += stats.Table_RFDc

            # mean box plot
            self.box_Cost[index] = case.Cost_Mean
            self.box_RFD[index] = case.RFD_Mean
            self.box_EPSILON[index] = case.EPSILON_Mean
            self.box_IGD[index] = case.IGD_Mean
            self.box_Ft[index] = case.Ft_Mean
            self.box_RFDc[index] = case.RFDc_Mean

            #print("------------------")
            #print(case)
            #print("------------------")
            #print(stats)

    def boxPlots(self, names):
        for each in names:
            self.boxPlot(each)

    def boxPlot(self, name):
        sel = { "Cost"    : self.box_Cost,
                "RFD"     : self.box_RFD,
                "EPSILON" : self.box_EPSILON,
                "IGD"     : self.box_IGD,
                "Ft"      : self.box_Ft,
                "RFDc"    : self.box_RFDc }
        data = sel[name]
        fig = plt.figure(figsize=(10, 5))
        plt.boxplot(data)
        plt.xticks([x+1 for x in range(0, len(ORDERS))], ORDERS, rotation=16)
        plt.ylim([-0.1,1.1])
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.tight_layout()
        fig.canvas.set_window_title(name)
        plt.show()



class ExpTime:

    def __init__(self):
        self.legend = ["switch-greedy", "switch-GA", "switch-LKH", "Hybrid", "NSGA-II"]
        self.xAxis = []
        # number of points * 7 algorithms
        self.points = []
        self.LEN = 0

        V = [2, 3, 4, 5, 6, 7, 8]
        N = [10, 20, 30, 40, 50, 60]
        self.REF = np.zeros(len(V)*len(N))
        tp = []
        # v^2 * log(n)
        index = 0
        for n in N:
            for v in V:
                self.REF[index] = v * n
                tp.append( "%d * %d" % (n, v) )
                index += 1
        #print(self.REF)
        self.ARG = self.REF.argsort()
        print("ARG\n" + str(self.ARG))

        print(tp)
        for i in range(0, len(self.ARG)):
            self.xAxis.append(tp[self.ARG[i]])
        print(self.xAxis)


    def readFile(self, filename):
        data = np.loadtxt(filename).T
        print(data.shape)

        # the first row is xAxis
        self.points = data[3:] / 1000
        print(self.points)
        self.LEN = self.points.shape[0]

        # sorting
        arg = self.ARG
        for k in range(0, self.LEN):
            self.points[k] = self.points[k][arg]
        #print(self.points)


    def doPlot(self, filename):
        self.readFile(filename)

        #plt.style.use('fivethirtyeight')
        #plt.style.use('ggplot')
        line_style = ["k-.", "k-", "k:", "k.-", "ko-"]

        plt.figure(figsize=(14, 5.2), facecolor='white')
        for index in range(0, self.LEN):
            plt.plot(self.points[index], line_style[index], label=self.legend[index], markerfacecolor='none', ms=6.5, mew=2.5, linewidth=1.25)
            #plt.plot(self.points[index], label=self.legend[index])

        x = [k*3 for k in range(0, int(len(self.REF)/3))]
        y = []
        for each in x:
            y.append(self.xAxis[each])
        plt.xticks(x, y)

        plt.legend(loc='best', numpoints=1, fancybox=True, fontsize=14)
        plt.xlim(0, len(self.REF)-1)
        plt.ylim(-10,1400)
        plt.xlabel("the number of parameters (n) * the number of values (v)", fontsize=14)
        plt.ylabel("the execution time (second)", fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.tight_layout()

        # line from (0, 0) to (8.5, 450)
        plt.plot([0, 8.5], [0, 450], 'k--', lw=1)
        # line from (33.2, 156) to (41, 0)
        plt.plot([28.8, 41], [450, 0], 'k--', lw=1)

        # sub plot
        subplt = plt.axes([0.26, 0.4, 0.45, 0.5])
        for index in range(0, self.LEN):
            subplt.plot(self.points[index], line_style[index], label=self.legend[index], markerfacecolor='none', ms=6.5, mew=2.5, linewidth=1.75)
        subplt.set_xlim(0, len(self.REF)-1)
        subplt.set_ylim(-0.2, 4)
        subplt.set_xticklabels([])
        subplt.tick_params(axis='both', which='major', labelsize=14)

        plt.show()


if __name__=='__main__':

    e = Exp(0, 389)
    #e.boxPlot("Cost")
    #e.writeStats()
    #e.writeBestOrder()
    e.boxPlots(["Cost", "RFD", "EPSILON", "IGD", "Ft", "RFDc"])
    #e.writeStatsLatex()

    #ep = ExpTime()
    #ep.doPlot("exp/cost data.txt")
