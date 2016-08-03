import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import cm
import numpy as np
import math
import pandas as pd

RT_dis = []

data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,)
Reaction_T = data['RT']
distance  = abs(data['n1'] - data['n2'])

for i in xrange (len(Reaction_T)):
    if(Reaction_T[i])<2000:
        plt.scatter(distance[i],Reaction_T[i])

y=np.poly1d(np.polyfit(distance,Reaction_T,1))(distance)
plt.plot(distance,y,color='r')
plt.xlabel('Distance (abs(n1-n2))')
plt.ylabel('Reaction Time')
plt.show()

#for i in xrange(len(y)):
#    print(y[i])

def slope_Yintercept(Y2=y[70],Y1=y[0],X2=distance[70],X1=distance[0]):
    m = ((Y2-Y1)/(X2-X1))
    c = Y2 - (m*X2)
    print(m,c)

df = pd.read_csv('data_sim.csv')
unique_distance = list(set(distance))

for i in xrange(len(distance)):
    if distance[i] == 2:
        RT_dis.append(data[i]['RT'])

print(RT_dis)
Std = np.std(RT_dis)
Mean = np.mean(RT_dis)

print(Std,Mean)

#for dist in unique_distance:
#    RT_dis = df[df[unique_distance==dist]]['RT']

    #print(distance)
    #RT_dis = data[data[unique_distance]==distance]['RT']
    #print(RT_dis)
'''
def Variance():
    Mean = np.sum(distance)/len(distance)
    for i in xrange(len(distance)):
        print(Mean-distance[i])

Variance()
'''
