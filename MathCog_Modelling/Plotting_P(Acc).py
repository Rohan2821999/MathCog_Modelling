# Probablity of Accuracy Response modelling code ----- Author: Rohan Hundia ----

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from Plotting_RT import*
from Easiness_Map import*
from Location_Val import*
from matplotlib import cm
import numpy as np
import math

data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,)
ratios = list(set(data['ratio']))
n1s = (data['n1'])
n1s_set = list(set(data['n1']))
n2s = (data['n2'])
Reaction_T = (data['RT'])

data2 = np.genfromtxt(r'anon_raw_symbolic.csv',delimiter =',',names = True ,dtype = None)
r = np.array(data2['ratio'])
#r = (r[~np.isnan(r)])
n1s_data2 = np.array(data2['n1'])
#n1s_data2 = (n1s_data2[~np.isnan(n1s_data2)])
Actual_E = np.array(data2['easyness'])
#Actual_E = (Actual_E[~np.isnan(Actual_E)])

ns = []
Acc_array, Easiness_Array = [],[]
ratio = []
numerator,denominator,P_Error,P_Acc,array_possible,vals = [],[],[],[],[],[]

w = 0.15
cmap = cm.RdYlGn

ns = []
RT_ns, n1_ns, n2_ns = [],[],[]

for n1,n2,RT in zip(n1s,n2s,Reaction_T):
    temp = [n1, n2, RT]
    if temp not in ns:
        ns.append([n1,n2,RT])
        RT_ns.append(RT)
        n1_ns.append(n1)
        n2_ns.append(n2)

for n1,n2,RT in ns:
    ratio.append(float(n1)/n2)
    numerator.append(abs(n1-n2))
    denominator.append(math.sqrt(2)*w*(((n1**2)+(n2**2))**0.5))
    P_Error.append(0.5*math.erfc(numerator[-1]/denominator[-1]))
    P_Acc.append(1 - P_Error[-1])
    array_possible.append(np.random.choice([0,1],size=(10),p=[1-P_Acc[-1],P_Acc[-1]]))
    vals.append(np.random.choice(array_possible[-1]))

def Plot_BinnedDiff(c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=0.5,vmax=1))):
    for i in xrange(len(RT_ns)):
            if RT_ns[i]< 2000:
                if vals[i] == 0:
                    vals[i] = 0.5
                colors = c.to_rgba(vals[i])
                plt.scatter([ratio[i]], [n1_ns[i]],color = colors)

P_Guessing = 0.1
New_Actual_E = []
def Val_E (c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=-1,vmax=1))):
    for i in xrange(len(Actual_E)):
        if (np.isnan(Actual_E[i])) == False:
            if 1 > Actual_E[i] > -1:
                Subjects = Gen_SimInstances(i)
                if (type(Subjects) != int) and (Subjects != None):
                    Easiness = Subjects.Ea(n1s_data2[i],r[i])
                    Easiness_Array.append(Easiness)
                    New_Actual_E.append(Actual_E[i])
                    plt.scatter([Easiness],[Actual_E[i]])
    print(np.corrcoef(Easiness_Array,New_Actual_E))
    plt.xlabel("Simulated Easiness Vals")
    plt.ylabel("Actual Easiness Vals")
    plt.show()


'''
    for i in xrange(len(RT_ns)):
        if RT_ns[i]<2000:
            E = (vals[i]-(RT_ns[i]/2000.0))
            colors = c.to_rgba(E)
            plt.scatter([ratio[i]], [n1_ns[i]],color = colors)
            print(E)
'''

def Plot_PAcc(c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=0.5,vmax=1))):
    for i in xrange(len(P_Acc)):
        if RT_ns[i]< 2000:
            colors = c.to_rgba(P_Acc[i])
            plt.scatter([ratio[i]], [n1_ns[i]],color = colors)

#Plot_BinnedDiff()
Val_E()
plt.xlabel('Ratio (n1/n2)')
plt.ylabel('n1')
plt.show()
