import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 3, 2, 3, 1, 2, 5, 1, 4, 8, 3, 6, 22, 5, 6, 3, 54, 17, 68, 19]
xsticks = ["85","88","92","94","96","97", "98","99","00","01","02","03","04","05","06","07","08","09","10","11","12","13","14"]
y = []
sum = 0
for i in range(0, len(x)):
    sum = sum + x[i]
    y.append(sum)
print(y)

plt.figure(figsize=(15, 8))
plt.plot(x, "k--", label="anneal",markerfacecolor='none', ms=6.5, mew=2.5,linewidth=1.5)
plt.plot(y, "k-", label="cumulative",markerfacecolor='none', ms=6.5, mew=2.5,linewidth=1.5)
plt.xlabel("year")
plt.ylabel("number of applications")
x = [k for k in range(0, len(xsticks))]
plt.xticks(x, xsticks)
#plt.legend(loc='best', numpoints=1, fancybox=True)
plt.tight_layout()
plt.show()