import Item as I
import numpy as np

class Prioritization:
    orders = ["random", "coverage", "switch-greedy", "switch-GA", "switch-LKH", "Hybrid", "NSGA-II"]
    metrics = ["Cost", "RFD", "EPSILON", "IGD", "Ft-measure"]

    def __init__(self):
        self.statsAll = {}
        for m in self.metrics:
            self.statsAll[m] = np.zeros(shape=(21,3))   # + / = / -

        self.statsName = []
        for i in range(6,-1,-1):
            for j in range(i-1,-1,-1):
                self.statsName.append( self.orders[i] + " VS " + self.orders[j] )

    def printStats(self):
        print("###### Stats ######")
        for m in self.metrics:
            print( "# " + m )
            print("  + / = / -")
            tp = self.statsAll[m]
            for i in range(0, len(tp)):
                print( str(tp[i]) + "\t" + self.statsName[i] )


    def scanFiles(self, begin, end):
        for index in range(begin,end+1):
            item = I.Item()
            item.readfile( "data//" + str(index) + ".txt" )

            for m in self.metrics:
                tp = item.StatisticArray[m]
                tpSum = np.zeros(shape=(21,3))  # + / = / -
                for i in range(0, len(tp)):
                    if  tp[i] == "+":
                        tpSum[i][0] += 1
                    elif tp[i] == "=":
                        tpSum[i][1] += 1
                    elif tp[i] == "-":
                        tpSum[i][2] += 1
                    else:
                        print("ERROR MAIN")

                self.statsAll[m] = self.statsAll[m] + tpSum


if __name__=='__main__':
    #p = I.Item()
    #p.readfile("data//5.txt")
    #p.print()
    exp1 = Prioritization()
    exp1.scanFiles(0,58)
    exp1.printStats()

