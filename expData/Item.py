import numpy as np
import operator
from scipy import stats

class Item:
    metrics = ["Cost", "RFD", "EPSILON", "IGD", "Ft-measure"]
    orders = ["random", "coverage", "switch-greedy", "switch-GA", "switch-LKH", "Hybrid", "NSGA-II"]

    def __init__(self):
        self.Data = []
        self.Data_Mean = []

        self.Statistic = {}
        self.StatisticArray = {}

    def print(self, data=False, mean=True, stats=True):
        if data:
            print("------------- data -------------")
            for i in range(0,5):
                print( self.metrics[i] )
                cc = self.Data[i]
                for each in cc:
                    print( each + ": " + str(cc[each]) )
        if mean:
            print("------------- mean data -------------")
            print(self.orders)
            line = "  #\t\t"
            for i in range(0, 5):
                line += self.metrics[i] + "\t\t"
            print(line)
            for j in range(0, 7):
                tp = []
                for i in range(0, 5):
                    tp.append(self.Data_Mean[i][self.orders[j]])
                tp = np.array(tp)
                np.set_printoptions(precision=3, suppress=True)
                print(tp)
        if stats:
            print("------------- stats -------------")
            for m in self.metrics:
                w = self.Statistic[m]
                print("\n" + m)

                index = 0
                for i in range(6,-1,-1):
                    for j in range(i-1,-1,-1):
                        print(w[i][j] + "\t" + self.orders[i] + " VS " + self.orders[j] )
                        if self.StatisticArray[m][index] != w[i][j] :
                            print("ERROR")
                        index += 1


    def readfile(self, filename):
        f = open(filename, 'r')
        lines = f.readlines()
        length_orders = len(self.orders)

        # compute the index of each sub data set
        start = [2]
        for x in range(0, 4):
            tp = start[x] + length_orders + 2
            start.append(tp)

        # read data
        data = []
        # [
        #   {"alg1":[values], "alg2":[values]}, (Cost)
        #   {},                                 (RFD)
        #   ...                                 (...)
        # ]
        for x in start:
            each = {}
            for y in range(0, length_orders):
                l2 = lines[x+1+y].strip()
                l2 = l2[l2.find(":")+3:len(l2)-1]
                l2 = l2.split(", ")
                each[self.orders[y]] = np.array(l2, np.float)
            data.append(each)

        #for each in data:
        #    for od in orders:
        #        print( od + ": " + str(each[od]) )

        # compute the average data
        data_mean = []
        # [
        #   {"alg1":mean, "alg2":mean}, (Cost)
        #   {},                         (RFD)
        #   ...                         (...)
        # ]
        # for each measures
        for i in range(0, 5):
            each = {}
            # for each approach
            for alg in self.orders:
                tp = data[i][alg].mean()
                each[alg] = tp
            data_mean.append(each)

        #for each in data_mean:
        #    print(each)

        # determine the best order based on mean value of each metric
        orders_best = []
        # Cost, RFD, EPSILON, IGD, Ft-measure
        orders_best.append(min(data_mean[0].items(), key=operator.itemgetter(1))[0])
        orders_best.append(max(data_mean[1].items(), key=operator.itemgetter(1))[0])
        orders_best.append(min(data_mean[2].items(), key=operator.itemgetter(1))[0])
        orders_best.append(min(data_mean[3].items(), key=operator.itemgetter(1))[0])
        orders_best.append(min(data_mean[4].items(), key=operator.itemgetter(1))[0])
        #print("best alg: " + str(orders_best))

        self.Data = data
        self.Data_Mean = data_mean
        self.statisticUpdarte(data)

    def statisticUpdarte(self, data):
        """
        :param data
        :return Wilcoxon
        """
        Wilcoxon = {}
        # for Wilcoxon["measure"],
        #       alg1  alg2
        # alg1   \\     +
        # alg2   -      \\

        # the small value the better
        for c in [0, 2, 3, 4]:
            current = data[c]
            wtp = []
            for alg1 in self.orders:
                tp = []
                for alg2 in self.orders:
                    if alg1 == alg2 :
                        tp.append( "\\" )
                    else:
                        x1 = current[alg1]
                        x2 = current[alg2]
                        if np.array_equal(x1, x2):  # same value array
                            tp.append("=")
                        else:
                            [T, p] = stats.wilcoxon(x1, x2, zero_method='wilcox')
                            if p < 0.05 :
                                if x1.mean() < x2.mean():
                                    tp.append("+")  # alg1 is better than alg2
                                else:
                                    tp.append("-")  # alg1 is worse than alg2
                            else:
                                tp.append("=")  # alg1 is equal to alg2
                wtp.append(tp)
            Wilcoxon[self.metrics[c]] = wtp

        # the large value the better
        current = data[1]
        wtp = []
        for alg1 in self.orders:
            tp = []
            for alg2 in self.orders:
                if alg1 == alg2 :
                    tp.append( "\\" )
                else:
                    x1 = current[alg1]
                    x2 = current[alg2]
                    if np.array_equal(x1, x2):  # same value array
                        tp.append("=")
                    else:
                        [T, p] = stats.wilcoxon(x1, x2, zero_method='wilcox')
                        if p < 0.05 :
                            if x1.mean() > x2.mean():
                                tp.append("+")  # alg1 is better than alg2
                            else:
                                tp.append("-")  # alg1 is worse than alg2
                        else:
                            tp.append("=")  # alg1 is equal to alg2
            wtp.append(tp)
        Wilcoxon["RFD"] = wtp

        self.Statistic = Wilcoxon

        # reformat to an array
        for m in self.metrics:
            w = Wilcoxon[m]
            tp = []
            for i in range(6,-1,-1):
                for j in range(i-1,-1,-1):
                    tp.append(w[i][j])
            self.StatisticArray[m] = tp