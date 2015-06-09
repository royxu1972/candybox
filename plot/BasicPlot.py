import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import parallel_coordinates

font_large = {'family': 'Arial', 'size': 20}
font_normal = {'family': 'Arial', 'size': 16}
line_style = ["k:", "k-", "k--", "ko-", "k+-", "kv--", "ko--", "ks--", "kd--", "k+--"]

class Data:
    def __init__(self, title, xLabel, yLabel, xSticks, data, legend):
        '''
        INPUT REQUIRED:
            title (String): title of figure
            xLabel (String): label of x-axis
            yLabel (String): label of y-axis
            xSticks (['x1', 'x2', ...]): x-sticks
            data ([d1, d2, ...])
            legend (['lg1', 'lg2', ...])
        '''
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

        # reformat data
        else:
            return
            '''
            f = open(name + '.csv', 'w')
            f.write(','.join(Label) + '\n')
            for i in range(0, len(Matrix)):
                if( Matrix[i][len(Matrix[i])-1] == "coverage" ):
                    f.write(str(Matrix[i][0]))
                    for j in range(1, len(Matrix[i])):
                        f.write(','+str(Matrix[i][j]))
                        f.write('\n')
            f.close()
            '''


class BPlot:
    # do a single line plot
    def line(self, Data, Type):
        # Type == "show"
        # Type == "save", then save figure to file
        plt.style.use('fivethirtyeight')
        plt.figure(figsize=(14, 8), facecolor='white')
        for index in range(0, len(Data.data)):
            #plt.plot(Data.data[index], line_style[index], label=Data.legend[index], markerfacecolor='none', ms=6.5, mew=2.5, linewidth=1.5)
            plt.plot(Data.data[index], label=Data.legend[index])

        plt.xlabel(Data.xLabel)
        plt.ylabel(Data.yLabel)
        #plt.title(Data.title)
        x = [k for k in range(0, len(Data.xSticks))]
        plt.xticks(x, Data.xSticks)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        plt.tight_layout()
        # show or save
        if( Type == "show"):
            plt.show()
        elif( Type == "save" ):
            plt.savefig("data//" + Data.title + ".png")
        plt.close()

    # do multiple box plot
    def boxes(self, Datas, column):
        row = len(Datas) // column
        fig, axes = plt.subplots(nrows=row, ncols=column)

        index = 0
        for i in range(0, row):
            for j in range(0, column):
                axes[i, j].boxplot(Datas[index].data, labels=Datas[0].xSticks,
                                   showmeans=True, meanline=True)
                axes[i, j].set_title(Datas[index].title)
                index = index + 1

        #for ax in axes.flatten():
        #    ax.set_yscale('log')
        #    ax.set_yticklabels([])

        fig.subplots_adjust(hspace=0.3)
        plt.show()
