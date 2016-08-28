# Generating simulated people from (Easiness_Map.py) according to SSID vals from other CSV file
# -- Author: Rohan Hundia --
import numpy as np
from Easiness_Map import*

data_file = np.genfromtxt(r'anon_screener_scores.csv',delimiter = ',' ,names = True, dtype = None,)
data_file2 = np.genfromtxt(r'anon_raw_symbolic.csv',delimiter = ',' ,names = True, dtype = None,)
ssid = data_file['sid']
age = data_file['age']
grade = data_file['grade']

ssid_file2 = data_file2['sid']
ssid_list = ssid.tolist()
acc = data_file2['ACC']
#practice = data_file2['practice']

#for j in xrange(len(ssid_file2)):
def Gen_SimInstances(y):
    '''
    Argument y is defined in Plot_PAcc.py script where y are the iterated values till length of all easiness vals
    This function also checks age groups/ class of each subject (person) and converts class to age.
    Generates different instances of simulted people for each age group.
    '''
    if ssid_file2[y] in ssid:
        #print(ssid_file2[j])
        Child = 0
        c = 0
        var = (ssid_list.index(ssid_file2[y]))
        age_grade = 0
        if (np.isnan(age[var]) == False) and (np.isnan(grade[var]) == True):
            age_grade = int(round(age[var]))
        if (np.isnan(age[var]) == False) and (np.isnan(grade[var]) == False):
            age_grade = int(round(age[var]))
        if (np.isnan(age[var]) == True) and (np.isnan(grade[var]) == False):
            age_grade = int(grade[var] + 5)
        #print(ssid_list[var],age_grade)
        if (18 >= age_grade >= 15):
            Child = Person(0.17,-16,500)
            #c = 'red'
        elif(14 >= age_grade >= 11 ):
            Child = Person(0.17,-30,600)
            #c = 'blue'
        elif(10 >= age_grade >= 8):
            Child = Person(0.17,-40,700)
            #c = 'green'
        elif(age_grade == 7):
            Child = Person(0.17,-50,800)
            #c = 'yellow'

        #if acc[y] == 0:
            #c = 'red'
        #if acc[y] == 1:
            #c = 'green'
           #Child = None
           #c = None


        #print(Child,age_grade,ssid_file2[y])
        return Child,c

#Gen_SimInstances
