import basicPlot as bp
import functions as func
from random import uniform

'''
prioritization plot
'''
class E1Plot:

    def __init__(self):
        self.DataSet = []
        self.Matrix = []
        self.MatrixLabel = ['P', 'V', 'T', 'Type', 'R', 'Name']

    # read data from source file
    def readFile(self, filename):
        dictP = { 10:0.0, 20:0.5, 30:1.0, 40:1.5, 60:2.0 }
        dictV = { 2:0.0,  3:0.5,  4:1.0,  6:1.5,  8:2.0 }
        p_init = [0.00095, 0.40095, 0.80095, 1.20095, 1.60095]
        t_init = [0.00095, 1.00095]
        #dictP = { 4:0.0, 6:1.0, 10:2.0 }
        #dictV = { 2:0.0, 3:1.0, 4:2.0  }
        dictT = { 2:0.5,  3:1.5 }
        dictType = { 1:0.5,  2:1.5 }

        f = open(filename, 'r')
        name = f.readline().strip()
        name = name[name.index('=')+1:]
        imT = int(name[:name.index(',')])
        imType = int(name[name.index('=')+1:])
        #print( "t = %d, type = %d" %(imT, imType) )

        line = f.readline()
        while( line ):
            line = line.strip()
            # skip blank lines
            if( len(line) == 0 ):
                line = f.readline()
                continue
            # this is data part
            elif( line.startswith('-') ):
                # get P and V
                name = f.readline().strip()     # p = 10 , v = 3
                imP = int(name[3:name.index(',')])
                imV = int(name[name.index(',')+5:])
                #print( "p = %d, v = %d" %(imP, imV) )

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

                #
                # MATRIX
                # determine the top rank, the smaller value the better
                #
                for j in range(0, len(ratio)):
                    value = items[0][j]
                    rank = labels[0]
                    for i in range(1, len(items)):
                        if( items[i][j] < value ):
                            value = items[i][j]
                            rank = labels[i]
                    imR = ratio[j]
                    imRank = rank
                    #print("ratio = %f, rank = %s" %(imR, imRank) )
                    '''
                    if( imP == 10 ):
                        dictP_imP = p_init[0]
                        p_init[0] += 0.00095
                    elif( imP == 20 ):
                        dictP_imP = p_init[1]
                        p_init[1] += 0.00095
                    elif( imP == 30 ):
                        dictP_imP = p_init[2]
                        p_init[2] += 0.00095
                    elif( imP == 40 ):
                        dictP_imP = p_init[3]
                        p_init[3] += 0.00095
                    else:
                        dictP_imP = p_init[4]
                        p_init[4] += 0.00095
                    '''

                    if( imP == 10 ):
                        dictP_imP = uniform(0.0, 0.3)
                    elif( imP == 20 ):
                        dictP_imP = uniform(0.4, 0.7)
                    elif( imP == 30 ):
                        dictP_imP = uniform(0.8, 1.1)
                    elif( imP == 40 ):
                        dictP_imP = uniform(1.2, 1.5)
                    else:
                        dictP_imP = uniform(1.6, 1.9)

                    if( imType == 1 ):
                        dictT_imType = uniform(0.0, 0.9)
                    else:
                        dictT_imType = uniform(1.0, 1.9)

                    if( imV == 2 ):
                        dictP_imV = uniform(0.0, 0.3)
                    elif( imV == 3 ):
                        dictP_imV = uniform(0.4, 0.7)
                    elif( imV == 4 ):
                        dictP_imV = uniform(0.8, 1.1)
                    elif( imV == 6 ):
                        dictP_imV = uniform(1.2, 1.5)
                    else:
                        dictP_imV = uniform(1.6, 1.9)

                    self.Matrix.append([dictP_imP, dictP_imV, dictT[imT], dictT_imType, imR, imRank])

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

    # show parallel_coordinates plot
    def parallelPlot(self, name, label):
        plot = bp.APlot()
        plot.parallel(name, label)


if __name__=='__main__':
    mp = E1Plot()
    #mp.readFile("data1.txt")
    #mp.readFile("data.txt")
    mp.parallelPlot("poly.csv", "Top")
    #mp.linePlot("save")