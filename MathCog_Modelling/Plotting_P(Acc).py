import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import cm
import numpy as np
import math

P_Error = []
BinaryBns = []
P_Acc = []
numerator = []
denominator = []


data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,)
ratios = list(set(data['ratio']))
n1s = list(set(data['n1']))
n2s = list(set(data['n2']))

w = 0.15 # weber fraction values
cmap = cm.RdYlGn
c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=0.5,vmax=1))

#print(numerator)
#print numerator[2]

for ratio in ratios:
    for n1 in n1s:
        print(n1)
        #numerator = abs(n1-n2)
        #denominator = (math.sqrt(2)*w*(((n1**2)+(n2**2))**0.5))
        #P_Error = 0.5*math.erfc(numerator/denominator)
        #P_Acc = 1 - P_Error
        colors = c.to_rgba(P_Acc)
        plt.scatter([ratio], [n1],color = colors)


#plt.scatter([ratios], [n1s])
#print(P_Acc)
#plt.scatter(ratio,P_Acc)
plt.xlabel('Ratio (n1/n2)')
plt.ylabel('n1')
plt.show()
