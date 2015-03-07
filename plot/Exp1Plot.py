import BasicPlot as bp

class E1Plot:

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
            data = bp.Data(l[0].strip(), l[1].strip(), l[2].strip(), xsticks, data, legend)
            plot = bp.BPlot()
            plot.line(data)

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
            data = bp.Data(l[0].strip(), l[1].strip(), l[2].strip(), xs,data,[])
            allData.append(data)

        print("all %d data" % len(allData))
        plot = bp.BPlot()
        plot.boxes(allData,6)

