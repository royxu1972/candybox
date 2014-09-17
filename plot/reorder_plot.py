from pylab import *


d1_1 = [167, 161, 165, 168, 164, 171]
d1_2 = [165, 166, 165, 165, 165, 166]
d1_3 = 161

# Making a 2-D array only works if all the columns are the
# same length.  If they are not, then use a list instead.
# This is actually more efficient because boxplot converts
# a 2-D array into a list of vectors internally anyway.
data = [d1_1, d1_2]

# multiple box plots on one figure
figure()
boxplot(data)

show()