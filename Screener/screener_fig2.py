import pylab
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


x = [1,7,9,11.5,13]
y = [0.25,0.43,0.55,0.58,0.56]
x2 = [14,16]
y2 = [0.61,0.57]

plt.scatter(x,y,color = sns.xkcd_rgb["spruce"],s=50,label='CORRECT')
plt.scatter(x2,y2,color = sns.xkcd_rgb["red"],s=60,marker = 'x',lw=2,label='INCORRECT')
plt.legend()


plt.plot([1,7], [0.25, 0.43], 'k-',lw=1,color= sns.xkcd_rgb["denim blue"])
plt.plot([7,9], [0.43, 0.55], 'k-',lw=1,color = sns.xkcd_rgb["denim blue"])
plt.plot([9,11.5], [0.55, 0.58], 'k-',lw=1,color = sns.xkcd_rgb["denim blue"])
plt.plot([11.5,14], [0.58, 0.61], 'k-',lw=1,color = sns.xkcd_rgb["denim blue"])
plt.plot([14,13], [0.61, 0.56], 'k-',lw=1,color = sns.xkcd_rgb["denim blue"])
plt.plot([13,16], [0.56, 0.57], 'k-',lw=1,color = sns.xkcd_rgb["denim blue"])

plt.text(4,0.27,'Fast RT',fontsize=12,color ="black")
plt.text(13,0.5,'Slow RT',fontsize=12,color ="black")

plt.text(1,0.27,'1',fontsize=12,color ="black")
plt.text(7,0.45,'2',fontsize=12,color ="black")
plt.text(9,0.57,'3',fontsize=12,color ="black")
plt.text(11.5,0.60,'4',fontsize=12,color ="black")
plt.text(12.3,0.55,'6',fontsize=12,color ="black")
plt.text(14.3,0.61,'5',fontsize=12,color ="black")
plt.text(16.3,0.56,'7',fontsize=12,color ="black")

plt.xlabel("Size",color = "black",fontsize=18)
plt.ylabel("Ratio",color = "black",fontsize=18)
plt.xlim(0,25)
plt.ylim(0.2,0.9)
plt.tick_params(labelsize = 18)
plt.show()
