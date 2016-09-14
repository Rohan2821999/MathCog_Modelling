import pylab
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

y = [0.8]
x = [2]
y2 = [0.3]
x2 = [22]
y3 = [0.85]
x3 = [24]

plt.scatter(x,y,color = sns.xkcd_rgb["spruce"],s=50)
plt.scatter(x2,y2,color = sns.xkcd_rgb["spruce"],s=50)
plt.scatter(x3,y3,color ='red',s=50)

plt.plot([8,28], [0.9, 0.25], 'k-',lw=8,color='blue',alpha=0.3)



plt.xlabel("Size",color = "black",fontsize=18)
plt.ylabel("Ratio",color = "black",fontsize=18)
plt.text(3,0.3,'EASY',fontsize=18,color = sns.xkcd_rgb["spruce"],alpha=0.4)
plt.text(1.7,0.82,'A',fontsize=15,color ="black")
plt.text(21.8,0.25,'B',fontsize=15,color ="black")
plt.text(23.6,0.87,'C',fontsize=15,color ="black")
plt.text(24,0.73,'HARD',fontsize=18,color ="red",alpha=0.4)
plt.tick_params(labelsize = 18)
plt.show()
