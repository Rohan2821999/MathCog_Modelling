#Searching Script
import numpy as np
from Easiness_Map import*

data_file = np.genfromtxt(r'anon_screener_scores.csv',delimiter = ',' ,names = True, dtype = None,)
data_file2 = np.genfromtxt(r'anon_raw_symbolic.csv',delimiter = ',' ,names = True, dtype = None,)
ssid = data_file['sid']
age = data_file['age']
grade = data_file['grade']

ssid_file2 = data_file2['sid']
ssid_list = ssid.tolist()

#for j in xrange(len(ssid_file2)):
def Gen_SimInstances(y):
    if ssid_file2[y] in ssid:
        #print(ssid_file2[j])
        Child = 0
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
            Child = Person(0.16,-16,650)
        elif(14 >= age_grade >= 11 ):
            Child = Person(0.22,-25,750)
        elif(10 >= age_grade >= 8):
            Child = Person(0.25,-30,900)
        elif(age_grade == 7):
            Child = Person(0.27,-32,1000)
        #print(Child,age_grade,ssid_file2[y])
        return(Child)

#Gen_SimInstances
