import BasicPlot as bp
import functions as func

'''
prioritization plot
exp - 1
'''
class E1Plot:

    def __init__(self):
        self.DataSet = []

    # read data from source file
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
                name = f.readline().strip()
                # skip one line
                f.readline()
                # xLabel line
                line = f.readline().strip()
                xLabel = line[0:line.index(':')]
                xStick = func.String2StringList(line[line.index(':')+2:])
                # other lines
                line = f.readline().strip()
                labels = []
                items = []
                while( True ):
                    if( len(line) == 0 ):
                        break
                    # process one data line
                    labels.append(line[0:line.index(':')])
                    items.append(func.String2FloatList(line[line.index(':')+2:]))
                    # next one
                    line = f.readline().strip()

                # item[k] / items[0] (random)
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


if __name__=='__main__':
    mp = E1Plot()
    mp.readFile("0504.txt")
    mp.linePlot("save")

