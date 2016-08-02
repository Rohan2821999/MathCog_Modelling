import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from matplotlib import cm
import numpy as np
import math

data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,)
Reaction_T = data['RT']
distance  = abs(data['n1'] - data['n2'])

for i in xrange (len(Reaction_T)):
    if(Reaction_T[i])<2000:
        plt.scatter(distance[i],Reaction_T[i])
plt.plot(distance,np.poly1d(np.polyfit(distance,Reaction_T,1))(distance),color='r')
plt.show()
