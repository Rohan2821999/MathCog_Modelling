import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
from Plotting_RT import*
from matplotlib import cm
import numpy as np
import math

data = np.genfromtxt(r'data_sim.csv',delimiter = ',' ,names = True, dtype = None,) # Reading raw response data from csv file
ratios = list(set(data['ratio']))
n1s_set = list(set(data['n1']))


cmap = cm.RdYlGn # Choosing Color Map - Numerical Value increases from Red to Green

class Person:
  def __init__(self,w,m,i):
      '''
      Arguments:
       w - weber fraction value (can be type int or float) - numerical coefficient to determine performance in task
       m - slope obtained from numerical distance vs RT map (can be type int or float)
       i - intercept of RT graph (can be type int or float) - Gives average Reaction time of a Person (threshold value of RT is 2000 ms otherwise particpant is penalized)
      '''
        self.w = w
        self.m = m
        self.i = i

  def Ea(self,n_1,r):
      '''
      This function computes Easiness of task dependent on Reaction Time and Accuracy
      Arguments:
      n_1 - One of the numerical numbers in the task
      r - Ratio of numbers in the task

      In order to compute the P_Error an erfc formula consisting of the two numbers and the weber fraction is used
      '''
      m = (self.m)
      intercept = self.i
      w = self.w

      dist = int(n_1 / r) - n_1
      rt = (dist * m) + intercept # Computing Reaction_Time from the values obtained from the RT graph
      n_2 = n_1/r
      numer = abs(n_1-n_2)
      denom = math.sqrt(2)*w*(((n_1**2)+(n_2**2))**0.5)
      P_Err = 0.5*math.erfc(numer/denom)
      P_A = 1 - P_Err
      array_poss = np.random.choice([0,1],size=(10),p=[1-P_A,P_A]) # Generating bin values array (consisting of 0's and 1's)using P_Acc probability
      val = np.random.choice(array_poss)
      if rt<500:
          rt = 500 # re-evaluate RT's < 500
      E = val - (rt/2000.)
      return E
'''
Generating different 'artifical' subjects with different weber fractions, slopes and intercepts
'''
Child1 = Person(0.2,-12.7,1097)
Child2 = Person(0.25,-12.7,1097)
Child3 = Person(0.28,-12.7,1097)
Child4 = Person(0.18,-12.7,1097)


Adult1 = Person(0.15,-20,1100)
Adult2 = Person(0.13,-12.7,1097)
Adult3 = Person(0.13,-12.7,1500)
Adult4 = Person(0.10,-20,1100)


Subjects = [Child1,Child2,Child3,Child4,Adult1,Adult2,Adult3,Adult4]

#Adding a parameter of Guessing due to distraction with P of 0.1
P_Guessing = 0.1
def Plot_E_Space():
    for i in xrange(len(Subjects)):
        #print(i)
        for ratio in ratios:
            for n1 in n1s_set:
                List_Functions = [-1,Subjects[i].Ea(n1,ratio)]
                Easiness = (np.random.choice(List_Functions,p=[P_Guessing,0.9])) #Assuming 10% of the times people get distracted and guess wrong
                c = cm.ScalarMappable(cmap=cmap, norm = mpl.colors.Normalize(vmin=-1,vmax=1))
                colors = c.to_rgba(Easiness)
                plt.figure(i+1)
                plt.scatter([ratio], [n1],color = colors)
        plt.xlabel('Ratio (n1/n2)')
        plt.ylabel('n1')
        plt.savefig("Easiness Plot- Subject "+str(i+1)) # Saving Figure maps of all subjects 

Plot_E_Space()
plt.show()
