import baseplot as bp
import functions as func

'''
prioritization plot
'''
class E1Plot:

    def __init__(self):
        self.DataSet = []

    # read data from filename, and then do line plot
    # file example:
    # parameter: 10 20 ...
    # random: 128.33 128.33 ...
    # coverage: 119.17 119.17 ...
    # switch-lkh: 113.479 113.479 ...
    # hybrid: 107.96 107.96 ...
    def plotLine(self, filename):
        # read data
        f = open(filename, 'r')
        line = f.readline().strip()
        xLabel = line[:line.index(':')]
        xSticks = func.String2StringList(line[line.index(':')+2:])
        data = []
        legend = []

        line = f.readline()
        while( line ):
            line = line.strip()
            legend.append(line[:line.index(':')])
            d = line[line.index(':')+2:]
            data.append(func.String2FloatList(d))
            line = f.readline()

        # format data to random based
        # data[i][j] = data[0][j] (random) / data[i][j]
        random = list(data[0])
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                data[i][j] = random[j] / data[i][j]

        # plot
        dp = bp.Data("", xLabel, 'ft-value', xSticks, data, legend)
        bp.BPlot().line(dp,"show")


    # read data from source file for line plot
    def readFile(self, filename):
        f = open(filename, 'r')
        name = f.readline().strip()

        line = f.readline()
        while( line ):
            line = line.strip()
            # skip blank lines
            if( len(line) == 0 ):
                line = f.readline()
                continue
            # this is data part
            elif( line.startswith('-') ):
                # skip one line
                f.readline()

                # xLabel line
                line = f.readline().strip()
                xLabel = line[0:line.index(':')]
                xStick = func.String2StringList(line[line.index(':')+2:])
                ratio =  func.StringList2FloatList(xStick)
                # other lines
                line = f.readline().strip()
                labels = []
                items = []
                while( True ):
                    if( len(line) == 0 ):
                        break
                    # process one data line
                    if( line[0:line.index(':')] != "switch-greedy" ):
                        # skip greedy order data
                        labels.append(line[0:line.index(':')])
                        items.append(func.String2FloatList(line[line.index(':')+2:]))
                    # next one
                    line = f.readline().strip()

                # item[k] / items[0] (random based)
                random = list(items[0])
                for i in range(0, len(items)):
                    for j in range(0, len(items[i])):
                        items[i][j] = random[j] / items[i][j]

                ds = bp.Data(name, xLabel, 'ft-value', xStick, items, labels)
                self.DataSet.append(ds)

            # go to the next line
            line = f.readline()

    # show DataSet[] by line plot
    def linePlot(self, tp, index=-1):
        plot = bp.BPlot()
        # show the index figure, start from 0
        if( index != -1 and index >= 0 and index <= len(self.DataSet) ):
            plot.line(self.DataSet[index], Type=tp)
        # show all figures
        elif( index == -1 ):
            for ds in self.DataSet:
                plot.line(ds, Type=tp)
        else:
            print("invalid index value")


    # normalize data file for parallel plot
    # INPUT:  name.txt
    # OUTPUT: name.csv
    def normalFile(self, name):
        p_upper = 60
        p_lower = 10
        v_upper = 8
        v_lower = 2
        r_upper = 2.0
        r_lower = 0.0
        t_dit = { 2: 0.33, 3: 0.66 }
        type_dit = { 1: 0.33, 2: 0.66}

        # read file
        f = open(name + '.txt', 'r')
        first = ','.join(f.readline().split(','))
        allLines = []
        line = f.readline()
        while( line ):
            nums = line.split(',')
            for i in range(0, len(nums)):
                nums[i] = nums[i].strip()
            nums[0] = str((float(nums[0]) - p_lower) / (p_upper-p_lower)) # p
            nums[1] = str((float(nums[1]) - v_lower) / (v_upper-v_lower)) # v
            nums[2] = str(t_dit[nums[2]]) # t
            nums[3] = str(type_dit[nums[3]]) # type
            nums[4] = str((float(nums[4]) - r_lower) / (r_upper-r_lower)) # r

            allLines.append( ','.join(nums) )
            line = f.readline()

        # write to output file
        fw = open(name + ".csv", 'w')
        fw.write(first + '\n')
        for each in allLines:
            fw.write(each + '\n')
        fw.close()

    # show parallel_coordinates plot
    # INPUT: name.csv -- data file
    #        label    -- the name of label column
    #
    def parallelPlot(self, name, label, ):
        plot = bp.APlot()
        plot.parallel(name, label)


if __name__=='__main__':
    mp = E1Plot()
    #mp.readFile("data1.txt")
    #mp.readFile("data.txt")
    #mp.normalFile("1000.csv")
    #mp.parallelPlot("2", "Top")
    #mp.linePlot("save")
    #mp.plotLine("each//parameter")