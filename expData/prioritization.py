import numpy as np
import operator

class Prioritization:

    def readfile(self, filename):
        f = open(filename, 'r')
        lines = f.readlines()

        # get the # of orders
        l1 = lines[0]
        orders = l1[l1.find("orders =")+9:].split()
        length_orders = len(orders)

        # compute the index of each sub data set
        start = [2]
        for x in range(0, 4):
            tp = start[x] + length_orders + 2
            start.append(tp)

        # read data
        # Cost, RFD, EPSILON, IGD, Ft-measure
        data = []
        # [
        #   {"alg1":[values], "alg2":[values]},
        #   {}, ...
        # ]
        for x in start:
            each = {}
            for y in range(0, length_orders):
                l2 = lines[x+1+y].strip()
                l2 = l2[l2.find(":")+3:len(l2)-1]
                l2 = l2.split(", ")
                each[orders[y]] = np.array(l2, np.float)
            data.append(each)

        #for each in data:
        #    for od in orders:
        #        print( od + ": " + str(each[od]) )

        # compute the average data
        data_mean = []
        # for each measures
        for i in range(0, 5):
            each = {}
            # for each approach
            for alg in orders:
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
        print("best alg: " + str(orders_best))

        # statistics test
        Wilcoxon = []
        #       alg1  alg2
        # alg1   -     1
        # alg2   0     -
        # where Wilcoxon[i][j] = 1 means that the mean value of approach i
        # is significantly better than that of j





if __name__=='__main__':
    p = Prioritization()
    p.readfile("data//0.txt")

