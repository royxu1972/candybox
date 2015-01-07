import matplotlib.pyplot as plt

font_large = {'family':'Arial', 'size':20}
font_normal = {'family':'Arial', 'size':16}
linestyle = ["kv-", "ko-", "ks-", "kd-", "k+-"]

filename1 = "D:\\Workspace\\CombinatorialDesign\\tmp\\data"

class myplot:
	#def __init__(self):

	''' data format
	mean results, xlabel, ylabel
	0.1 0.2 0.3 0.4 0.5
	d1 1 2 3 4 5
	d2 2 3 2 1 4
	'''
	def lineplot(self, filename):
		data = []
		label = []
		xsticks = []
		# read file
		with open(filename, "r") as f:
			lines = f.readlines()
			# set title, xlabel, ylabel
			l1 = lines[0].strip().split(',')
			title = l1[0]
			xlabel = l1[1]
			ylabel = l1[2]

			# set xsticks
			xtp = lines[1].strip().split()
			for k in range(0, len(xtp)):
				xsticks.append(xtp[k])
			x = [k for k in range(0, len(xtp))]

			# set data
			for k in range(2, len(lines)):
				tp = lines[k].strip().split()
				label.append(tp[0])

				d = []
				for y in range(1, len(tp)):
					d.append( float(tp[y]) )
				data.append(d)

		# do plot
		plt.figure(figsize=(14,8))
		for index in range(0, len(data)):
			plt.plot(data[index], linestyle[index], markerfacecolor='none', ms=6.5, mew=2.5, label=label[index], linewidth=1.5)

		plt.xlabel(xlabel, fontdict=font_normal)
		plt.ylabel(ylabel, fontdict=font_normal)
		#plt.title(title, fontdict=font_large)
		plt.xticks(x, xsticks)
		plt.legend(loc='best', numpoints=1, fancybox=True)
		plt.tight_layout()
		plt.show()

	#def boxplot(self, filename):

# run
mp = myplot()
mp.lineplot(filename1)