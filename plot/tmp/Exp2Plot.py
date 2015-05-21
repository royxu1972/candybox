import functions as fc
import basicPlot as bp

class EData:
    def __init__(self, name, data):
        self.name = name
        self.data = []
        for each in data:
            self.data.append((float(each)))

    def __str__(self):
        return self.name + " " + " ".join(str(e) for e in self.data)


class E2Plot:
    def __init__(self):
        self.tway = []
        self.parameter = []
        self.value = []
        self.DATA = []      # data[par][val]

    def Par(self, p):
        for k in range(0, len(self.parameter)):
            if( p == self.parameter[k] ):
                return k

    def Val(self, v):
        for k in range(0, len(self.value)):
            if( v == self.value[k] ):
                return k

    # read exp2 data
    def readFromFile(self, filename):
        f = open(filename, "r")
        # the first 3 lines
        line = f.readline().strip().split()
        self.tway = fc.String2Integer(line[1:])
        line = f.readline().strip().split()
        self.parameter = fc.String2Integer(line[1:])
        line = f.readline().strip().split()
        self.value = fc.String2Integer(line[1:])

        # t = 2 skip
        f.readline()

        # data
        for i in range(0, len(self.parameter)):
            each_par = []
            for j in range(0, len(self.value)):
                line = f.readline().strip().split()
                each_val = EData(line[0], line[1:])
                each_par.append(each_val)
            self.DATA.append(each_par)

        # e.g. print p = 30 v = 10
        # print(self.DATA[self.Par(30)][self.Val(10)])


    # plotPar()
    # x-axis <-- ratio (0.000 0.050 0.100 0.200 0.400 0.600 0.800 1.000 2.000 4.000)
    # y-axis <-- t-measure
    # each line <-- value (2, 4, 6, 8, 10)
    def plotPar(self, filename, par):
        self.readFromFile(filename)

        ratio = [0.000, 0.050, 0.100, 0.200, 0.400, 0.600, 0.800, 1.000, 2.000, 4.000]

        # line data
        data = []
        legend = []
        for i in range(0, len(self.value), 1):
            p = self.Par(par)
            v = self.Val(self.value[i])
            legend.append((self.DATA[p][v]).name)
            data.append((self.DATA[p][v]).data)

        d = bp.Data("fixed P", "ratio", "t-measure", ratio, data, legend)
        plot = bp.BPlot()
        plot.line(d)

    # plotRatio()
    # x-axis <-- parameter
    # y-axis <-- t-measure
    # each line <-- value (2, 4, 6, 8, 10)
    def plotRatio(self, filename, rat):
        self.readFromFile(filename)

        ratio = [0.000, 0.050, 0.100, 0.200, 0.400, 0.600, 0.800, 1.000, 2.000, 4.000]
        for k in range(0, len(ratio)):
            if( rat == ratio[k] ):
                index = k

        # line data
        data = []
        legend = []
        # for each v
        for i in range(0, len(self.value), 1):
            v = self.Val(self.value[i])
            vd = []
            # for each p
            for j in range(0, len(self.parameter)):
                p = self.Par(self.parameter[j])
                vd.append((self.DATA[p][v]).data[index])

            data.append(vd)
            legend.append("CA(N;2,p,"+str(self.value[i])+")")

        d = bp.Data("fixed ratio", "parameter", "t-measure (ordered / default)", self.parameter, data, legend)
        plot = bp.BPlot()
        plot.line(d)

    # plotVal()
    # x-axis <-- parameter
    # y-axis <-- t-measure
    # each line <-- ratio
    def plotVal(self, filename, val):
        self.readFromFile(filename)

        ratio = [0.000, 0.100, 0.200, 0.400, 0.600, 0.800, 1.000, 2.000, 4.000]

        # line data
        data = []
        legend = []
        v = self.Val(val)
        # for each ratio
        for each in ratio:
            vd = []
            index = ratio.index(each)

            for i in range(0, len(self.parameter)):
                p = self.Par(self.parameter[i])
                vd.append((self.DATA[p][v]).data[index])

            data.append(vd)
            legend.append("ratio = " + str(each))

        d = bp.Data("fixed value", "parameter", "t-measure (ordered / default)", self.parameter, data, legend)
        plot = bp.BPlot()
        plot.line(d)





















