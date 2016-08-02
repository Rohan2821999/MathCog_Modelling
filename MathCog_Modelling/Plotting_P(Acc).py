import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import numpy as np
import math

P_Error = []

data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,)
ratio = data['ratio']
n1 = data['n1']
n2 = data['n2']

w = 0.15 # weber fraction values
numerator = abs(n1-n2)
denominator = math.sqrt(2)*w*(((n1**2)+(n2**2))**0.5)

#print(numerator)
#print numerator[2]

for i in xrange (len(numerator)):
    P_Error = 0.5*math.erfc(numerator[i]/denominator[i])
    #print(P_Error)
    P_Acc = 1 - P_Error
    plt.scatter([ratio[i]], [n1[i]], color=[(P_Acc),(P_Acc),(P_Acc)])


#print(P_Acc)
#plt.scatter(ratio,P_Acc)
plt.xlabel('Ratio (n1/n2)')
plt.ylabel('n1')
plt.show()
