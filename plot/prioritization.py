import numpy as np
import baseplot as bp

'''
plot for prioritization experiment
'''
class PrioritizationPlot:

    def compareAll(self, filename):
        """
        Read .log file to compare f(t)-measure values of different orders. By default,
        only 4 orders (random, coverage, switch-lkh, hybrid) are examined.

        FORMAT OF EACH LINE
        -------------------
        random = 654 coverage = 621 switch-lkh = 618 hybrid = 586
        """

        # read data from file
        data = []
        with open(filename) as f:
            for line in f:
                each = line.strip().split()
                # read element[2], element[5], element[8], element[11]
                tp = [float(each[2]), float(each[5]), float(each[8]), float(each[11])]
                data.append(tp)
        data = np.array(data)

        # data normalization (each row for a case)
        size = data.shape[0]
        for i in range(0, size):
            data[i] = (data[i] - data[i].min())/(data[i].max() - data[i].min())

        # data transpose (each row for a line)
        data = data.T

        # do plot
        xLabel = "case of SUT"
        yLabel = "normalized f(t)-measure"
        title = "comparing different testing orders"
        xSticks = [k+1 for k in range(0, size)]
        legend = ["random", "coverage", "switch-lkh", "hybrid"]

        d = bp.Data(data, xLabel, yLabel, xSticks, legend, title)
        plot = bp.BPlot()
        plot.line(d,"show")

if __name__=='__main__':
    p = PrioritizationPlot()
    p.compareAll("2-way.samples.1000.log")