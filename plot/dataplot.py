import matplotlib.pyplot as plt

font_large = {'family': 'Arial', 'size': 20}
font_normal = {'family': 'Arial', 'size': 16}
line_style = ["kv-", "ko-", "ks-", "kd-", "k+-"]

filename1 = "D:\\Workspace\\CombinatorialDesign\\result\\data"
filename2 = "D:\\Workspace\\CombinatorialDesign\\result\\data-box"


class Data:
        title = ""
        xlabel = ""
        ylabel = ""
        xsticks = []
        data = []
        legend = []
        def __init__(self, title, x, y, xs, data, legend):
            self.title = title
            self.xlabel = x
            self.ylabel = y
            self.xsticks = xs
            self.data = data
            self.legend = legend


class MyPlot:

    def __init__(self):
        print("do plot")

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


    def lineplot(self, filename):
        '''
        title, xlabel, ylabel
	    0.1 0.2 0.3 0.4 0.5
	    d1 1 2 3 4 5
	    d2 2 3 2 1 4
        '''
        with open(filename, "r") as f:
            lines = f.readlines()
            # l = [title, xlabel, ylabel]
            l = lines[0].strip().split(',')
            xsticks = lines[1].strip().split()

            # data
            legend = []
            data = []
            for k in range(2, len(lines)):
                tp = lines[k].strip().split()
                legend.append(tp[0])

                d = []
                for y in range(1, len(tp)):
                    d.append(float(tp[y]))
                data.append(d)

            # save results
            pdata = Data(l[0].strip(), l[1].strip(), l[2].strip(), xsticks, data, legend)
            self.line(pdata)

    def boxplot(self, filename):
        '''
        title, xlabel, ylabel
	    1 2 3 4 5
	    2 3 2 1 4
        '''
        allData = []
        f = open(filename, "r")
        while ( True ):
            line = f.readline()
            if ( not line ):
                break

            # read data
            l = line.strip().split(',')
            xs = []
            data = []
            while ( True ):
                line = f.readline()
                # blank line, end
                if( len(line) == 1 ):
                    break
                # data lines
                line = line.strip().split()
                xs.append( line[0] )    # xsticks[i]
                d = []
                for n in range(1, len(line)):
                    d.append(float(line[n]))
                data.append(d)
            bdata = Data(l[0].strip(), l[1].strip(), l[2].strip(), xs,data,[])
            allData.append(bdata)

        print("all %d data" % len(allData))
        self.boxes(allData,6)


mp = MyPlot()
mp.lineplot(filename1)
#mp.boxplot(filename2)