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

y=np.poly1d(np.polyfit(distances,Reaction_T,1))(distances) # Create a best fit line and generate y coordinates of that line

def Plot_RT_Regression():
    '''
     For Reaction Time < 2000 ms generate a scatter plot for discrete numericals
     distance vs Reaction time
    '''
    for i in xrange (len(Reaction_T)):
        if(Reaction_T[i])<=2000:
            plt.scatter(distances[i],Reaction_T[i])

    plt.plot(distances,y,color='r')
    plt.xlabel('Distance (abs(n1-n2))')
    plt.ylabel('Reaction Time')
    plt.show()

def slope_Yintercept(Y2=y[70],Y1=y[0],X2=distances[70],X1=distances[0]):
    '''
    Computes Slope and Y_intercept of the best fit line from the equation.
    Arguments - Y1, Y2, X2, X1
    '''
    m = ((Y2-Y1)/(X2-X1))
    c = Y2 - (m*X2) #  Y intercept
    return(m,c)
    #print(m,c)

#slope_Yintercept()
def NormalizedRT_map():
    '''
    Generate Color map based on RT as the mean and average standard deviation computed from
    another script : 370
    '''
    cmap = cm.RdYlGn
    m = slope_Yintercept()[0]
    intercept = slope_Yintercept()[1]
    c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=500,vmax=2500))
    for ratio in ratios:
        for n1 in n1s:
            dist = n1 - int(n1 / ratio)
            RT = (dist * m) + intercept
            val = np.random.normal(RT,370)
            colors = c.to_rgba(val)
            plt.scatter([ratio],[n1],color = colors)


    plt.xlabel('Ratio')
    plt.ylabel('n1')
    plt.show()
#NormalizedRT_map()
