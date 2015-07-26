import numpy as np

class Case:

    def __init__(self, name, orders, file):
        self.name = name
        self.orders = orders

        # read data
        data = self.readFromFile(file)

        # data, ndarray, size as |orders| * 30 array
        self.Cost = data[0]
        self.RFD = data[1]
        self.EPSILON = data[2]
        self.IGD = data[3]
        self.Ft = data[4]

        # mean values of each orders under each metric
        norm = lambda x: (x - x.min()) / (x.max() - x.min())
        self.Cost_Mean = norm( np.mean(self.Cost, axis=1) )
        self.RFD_Mean = norm( np.mean(self.RFD, axis=1) )
        self.EPSILON_Mean = norm( np.mean(self.EPSILON, axis=1) )
        self.IGD_Mean = norm( np.mean(self.IGD, axis=1) )
        self.Ft_Mean = norm( np.mean(self.Ft, axis=1) )

        # the best one
        self.bestFtOrder = self.orders[np.argmin(self.Ft_Mean)]

    def __str__(self):
        str = "# " + self.name
        str += "\nCost \n" + np.array_repr(self.Cost)
        str += "\nRFD \n" + np.array_repr(self.RFD)
        str += "\nEPSILON \n" + np.array_repr(self.EPSILON)
        str += "\nIGD \n" + np.array_repr(self.IGD)
        str += "\nFt \n" + np.array_repr(self.Ft)

        str += "\n\nMean Cost\n" + np.array_repr(self.Cost_Mean)
        str += "\nMean RFD\n" + np.array_repr(self.RFD_Mean)
        str += "\nMean EPSILON\n" + np.array_repr(self.EPSILON_Mean)
        str += "\nMean IGD\n" + np.array_repr(self.IGD_Mean)
        str += "\nMean Ft\n" + np.array_repr(self.Ft_Mean)
        return str


    def readFromFile(self, filename):
        """
        read data from file
        """
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
        #   [|orders| * 30], [|orders| * 30], [|orders| * 30], [|orders| * 30], [|orders| * 30]
        # ]
        for x in start:
            each = np.empty((length_orders, 30))
            for y in range(0, length_orders):
                l2 = lines[x+1+y].strip()
                l2 = l2[l2.find(":")+3:len(l2)-1]
                each[y] = np.fromstring(l2, dtype=float, sep=',')
            data.append(each)

        return data