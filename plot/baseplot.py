import matplotlib.pyplot as plt
import numpy as np

class BasePlot:

    # apply 0-1 normalization to each row of data
    def normalize(self, data):
        """
        INPUT PARAMETER
        ------------------
        data : a 2D np-array, where each row represents a line
        """
        norm = lambda x: (x - x.min()) / (x.max() - x.min())
        re = []
        for each in data:
            re.append(norm(each))
        return re

    # Draw a single line figure
    def line(self, data, xLabel, yLabel, xStick, legend, style, norm=False):
        """
        INPUT PARAMETER
        ------------------
        title   : title of figure
        data    : a 2D array, where each row represents a line
        xLabel  : label of x-axis
        yLabel  : label of y-axis
        xStick  : each stick of x-axis
        legend  : the name of each line
        style   : the type of each line
        norm    : 0-1 normalization for the data of each line
        """

        #plt.style.use('fivethirtyeight')
        #plt.style.use('ggplot')
        plt.figure(figsize=(10, 6), facecolor='white')

        if norm:
            data = self.normalize(data)
            plt.ylim([-0.05, 1.05])

        for index in range(0, len(data)):
            #plt.plot(Data.data[index], line_style[index], label=Data.legend[index], markerfacecolor='none', ms=6.5, mew=2.5, linewidth=0)
            plt.plot(data[index], style[index], label=legend[index])

        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.xticks([k for k in range(0, len(xStick))], xStick)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        plt.tight_layout()

        plt.show()
        plt.close()


    # Draw two relevant line figures
    # They share the same coordinate and only differ in data
    def lines(self, data, titles, xLabel, yLabels, xStick, legend, style, norm=False):
        plt.figure(figsize=(16, 3.5), facecolor='white')
        length = len(data)

        if norm:
            for i in range(0, length):
                data[i] = self.normalize(data[i])

        for i in range(0, length):
            plt.subplot(1, length, i+1)

            for index in range(0, len(data[i])):
                plt.plot(data[i][index], style[index], label=legend[index])

            if i == 0 :
                plt.legend(loc=2, bbox_to_anchor=(-0.35, 1.05), numpoints=1, ncol=1, fontsize=14)

            if norm:
                plt.ylim([-0.05, 1.05])

            plt.xlabel(xLabel, fontsize=14)
            plt.ylabel(yLabels[i], fontsize=14)
            plt.title(titles[i], fontsize=14)
            plt.xticks([k for k in range(0, len(xStick))], xStick)
            plt.tight_layout(rect=[0.1, 0, 1, 1])

        plt.show()



if __name__=='__main__':
    a = BasePlot()
    data1 = np.array([[1,2,3,4,5],[6,7,6,8,10]])
    data2 = np.array([[3,3,4,5,6],[8,4,2,9,5]])
    xStick = [10,20,30,40,50]
    legend = ["l1","l2"]
    style = ["k.-", "k--"]

    #a.line(data1, "xx", "yy", xStick, legend, style, norm=True)
    a.lines([data1, data2], ["t1", "t2"], "xx", "yy", xStick, legend, style, norm=True)



