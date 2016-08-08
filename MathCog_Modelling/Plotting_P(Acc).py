import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import cm
import numpy as np
import math


data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,)
ratios = list(set(data['ratio']))
n1s = (data['n1'])
n2s = (data['n2'])
ns = []

w = 0.15 # weber fraction values
cmap = cm.RdYlGn
c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=0.5,vmax=1))

#print(numerator)
#print numerator[2]

ns = []
for n1,n2 in zip(n1s,n2s):
    temp = [n1, n2]
    if temp not in ns:
        ns.append([n1,n2])


for n1,n2 in ns:
    ratio = float(n1)/n2
    numerator = (abs(n1-n2))
    denominator = (math.sqrt(2)*w*(((n1**2)+(n2**2))**0.5))
    P_Error = (0.5*math.erfc(numerator/denominator))
    P_Acc = (1 - P_Error)
    print(P_Acc)
    colors = c.to_rgba(P_Acc)
    plt.scatter([ratio], [n1],color = colors)


plt.xlabel('Ratio (n1/n2)')
plt.ylabel('n1')
plt.show()
