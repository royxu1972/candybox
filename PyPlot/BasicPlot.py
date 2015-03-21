import matplotlib.pyplot as plt

font_large = {'family': 'Arial', 'size': 20}
font_normal = {'family': 'Arial', 'size': 16}
line_style = ["kv-", "ko-", "ks-", "kd-", "k+-", "kv--", "ko--", "ks--", "kd--", "k+--"]

class Data:
    '''
    line plot data[legend][data]
    '''
    def __init__(self, title, xlabel, ylabel, xsticks, data, legend):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xsticks = xsticks
        self.data = data
        self.legend = legend


class BPlot:
    # do a single line plot
    def line(self, Data):
        plt.figure(figsize=(14, 8))
        for index in range(0, len(Data.data)):
            plt.plot(Data.data[index], line_style[index], label=Data.legend[index],
                     markerfacecolor='none', ms=6.5, mew=2.5,
                     linewidth=1.5)

        plt.xlabel(Data.xlabel, fontdict=font_normal)
        plt.ylabel(Data.ylabel, fontdict=font_normal)
        # plt.title(title, fontdict=font_large)
        x = [k for k in range(0, len(Data.xsticks))]
        plt.xticks(x, Data.xsticks)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        plt.tight_layout()
        plt.show()

    # do multiple box plot
    def boxes(self, Datas, column):
        row = len(Datas) // column
        fig, axes = plt.subplots(nrows=row, ncols=column)

        index = 0
        for i in range(0, row):
            for j in range(0, column):
                axes[i, j].boxplot(Datas[index].data, labels=Datas[0].xsticks,
                                   showmeans=True, meanline=True)
                axes[i, j].set_title(Datas[index].title)
                index = index + 1

        #for ax in axes.flatten():
        #    ax.set_yscale('log')
        #    ax.set_yticklabels([])

        fig.subplots_adjust(hspace=0.3)
        plt.show()
