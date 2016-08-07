import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import cm
import numpy as np
import math
import pandas as pd

RT_dis = []

data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,)
ratios = list(set(data['ratio']))
n1s = list(set(data['n1']))
Reaction_T = data['RT']
distances  = abs(data['n1'] - data['n2'])



'''
for i in xrange (len(Reaction_T)):
    if(Reaction_T[i])<=2000:
        plt.scatter(distance[i],Reaction_T[i])

y=np.poly1d(np.polyfit(distance,Reaction_T,1))(distance)
plt.plot(distance,y,color='r')
plt.xlabel('Distance (abs(n1-n2))')
plt.ylabel('Reaction Time')
plt.show()


def slope_Yintercept(Y2=y[70],Y1=y[0],X2=distance[70],X1=distance[0]):
    m = ((Y2-Y1)/(X2-X1))
    c = Y2 - (m*X2)
    print(m,c)

#df = pd.read_csv('data_sim.csv')
#unique_distance = list(set(distance))
'''

#print(RT_dis)
Std = np.std(RT_dis)
Mean = np.mean(RT_dis)

List_Mean = [1102,980,786,1046,1009,850,860,821,850,817]

print(Std,Mean)
#slope_Yintercept()

cmap = cm.RdYlGn
c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=500,vmax=2500))
for ratio in ratios:
    for n1 in n1s:
        dist = int(n1 / ratio)
        RT = (dist * -12.6) + 1097
        val = np.random.normal(RT,370)
        colors = c.to_rgba(val)
        plt.scatter([ratio],[n1],color = colors)

plt.xlabel('Ratio')
plt.ylabel('n1')
plt.show()

#for dist in unique_distance:
#    RT_dis = df[df[unique_distance==dist]]['RT']

    #print(distance)
    #RT_dis = data[data[unique_distance]==distance]['RT']
    #print(RT_dis)
