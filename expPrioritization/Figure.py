import matplotlib.pyplot as plt

class Figure:

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
        for index in range(0, len(data)):
            #plt.plot(Data.data[index], line_style[index], label=Data.legend[index], markerfacecolor='none', ms=6.5, mew=2.5, linewidth=0)
            plt.plot(data[index], style[index], label=legend[index])

        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.xticks([k for k in range(0, len(xStick))], xStick)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        # plt.ylim([-0.1,1.1])
        plt.tight_layout()

        plt.show()
        plt.close()


    # Draw two relevant line figures
    # They share the same coordinate and only differ in data
    def lines(self, data1, data2, title1, title2, xLabel, yLabel, xStick, legend, style, norm=False):
        plt.figure(figsize=(10, 6), facecolor='white')

        plt.subplot(1, 2, 1)
        for index in range(0, len(data1)):
            plt.plot(data1[index], style[index], label=legend[index])
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        plt.title(title1)
        plt.xticks([k for k in range(0, len(xStick))], xStick)

        plt.subplot(1, 2, 2)
        for index in range(0, len(data2)):
            plt.plot(data2[index], style[index], label=legend[index])
        plt.title(title2)
        plt.xlabel(xLabel)
        plt.legend(loc='best', numpoints=1, fancybox=True)
        plt.xticks([k for k in range(0, len(xStick))], xStick)
        plt.tight_layout()

        plt.show()



if __name__=='__main__':
    a = Figure()
    data1 = [[1,2,3,4,5],[2,4,6,8,10]]
    data2 = [[3,3,4,5,6],[8,4,2,9,5]]
    xStick = [10,20,30,40,50]
    legend = ["l1","l2"]
    style = ["k.-", "k--"]

    # a.line("", data1, "xx", "yy", xStick, legend, style)
    a.lines(data1,data2,"t1", "t2", "xx", "yy", xStick, legend, style)

