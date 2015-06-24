import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import parallel_coordinates

font_large = {'family': 'Arial', 'size': 20}
font_normal = {'family': 'Arial', 'size': 16}
line_style = ["k.-", "k--", "k-", "k--", "ks--", "kd--", "k+--"]

class Data:
    def __init__(self, data, xLabel, yLabel, xSticks, legend, title=""):
        """
        Parameters
        ----------
        data: (ndarray) -- data point (n * m)
        xLabel: (String) -- label of x-axis
        yLabel: (String) -- label of y-axis
        xSticks: (list of String, ['x1', 'x2', ...]) -- size = m
        legend: (list of string, ['lg1', 'lg2', ...]) -- size = n
        title: (String) -- title of figure
        """
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.xSticks = xSticks
        self.data = data
        self.legend = legend

    def print(self):
        print("Title: " + self.title)
        print("xLabel: " + self.xLabel)
        print("yLabel: " + self.yLabel)
        print(self.xSticks)
        print(self.data)
        print(self.legend)



class APlot:
    # plot parallel coordinate
    # INPUT: name.csv -- data file
    #        label    -- the name of label column
    #        unique   -- only show single data
    def parallel(self, name, label, unique=""):
        if( unique == "" ):
            data = pd.read_csv( name + '.csv' )

            hybrid = 0
            switch = 0
            coverage = 0
            for i in range(0, 1000):
                ll = data.values[i][0]
                if( ll == "hybrid" ):
                    hybrid += 1
                elif( ll == "switch-lkh" ):
                    switch += 1
                elif( ll == "coverage" ):
                    coverage += 1
                else:
                    print("error")
                    return
            print("hybrid = %d, switch = %d, coverage = %d" % (hybrid, switch, coverage))

            plt.figure()
            parallel_coordinates(data, label)
            plt.show()


class BPlot:
    """
    Basic Plot
    """

    def line(self, Data, Type):
        """
        Parameter
        ---------
        Data: the data to be plotted
        Type: (String) -- whether "show" figure or "save" to file
        """

        plt.style.use('fivethirtyeight')
        #plt.style.use('ggplot')

        plt.figure(figsize=(14, 8), facecolor='white')
        for index in range(0, len(Data.data)):
            #plt.plot(Data.data[index], line_style[index], label=Data.legend[index], markerfacecolor='none', ms=6.5, mew=2.5, linewidth=0)
            plt.plot(Data.data[index], label=Data.legend[index])

        plt.xlabel(Data.xLabel)
        plt.ylabel(Data.yLabel)
        plt.title(Data.title)

        x = [k for k in range(0, len(Data.xSticks))]
        plt.xticks(x, Data.xSticks)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        plt.tight_layout()

        #plt.axis((1,len(x),-0.1,1.1))

        # show or save
        if( Type == "show"):
            plt.show()
        elif( Type == "save" ):
            plt.savefig("data//" + Data.title + ".png")
        plt.close()
