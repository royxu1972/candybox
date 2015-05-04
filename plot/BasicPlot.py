import matplotlib.pyplot as plt

font_large = {'family': 'Arial', 'size': 20}
font_normal = {'family': 'Arial', 'size': 16}
line_style = ["kv-", "ko-", "ks-", "kd-", "k+-", "kv--", "ko--", "ks--", "kd--", "k+--"]

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


class BPlot:
    # do a single line plot
    def line(self, Data, Type):
        # Type == "show"
        # Type == "save", then save figure to file
        plt.figure(figsize=(14, 8))
        for index in range(0, len(Data.data)):
            plt.plot(Data.data[index], line_style[index], label=Data.legend[index],
                     markerfacecolor='none', ms=6.5, mew=2.5,
                     linewidth=1.5)

        plt.xlabel(Data.xLabel, fontdict=font_normal)
        plt.ylabel(Data.yLabel, fontdict=font_normal)
        plt.title(Data.title, fontdict=font_large)
        x = [k for k in range(0, len(Data.xSticks))]
        plt.xticks(x, Data.xSticks)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        plt.tight_layout()
        # show or save
        if( Type == "show"):
            plt.show()
        elif( Type == "save" ):
            plt.savefig("figs//" + Data.title + ".png")
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
