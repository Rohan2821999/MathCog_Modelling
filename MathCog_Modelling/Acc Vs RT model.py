# Avg. RT vs Avg. Accuracy Model for Each Subject
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

data_file = np.genfromtxt(r'anon_screener_scores.csv',delimiter = ',' ,names = True, dtype = None,)
data2 = np.genfromtxt(r'anon_raw_symbolic.csv',delimiter = ',' ,names = True, dtype = None,)
ssid = data_file['sid']
age = data_file['age']
grade = data_file['grade']

ssid_file2 = data2['sid']
ssid_list = ssid.tolist()
acc = data2['ACC']
RT = data2['RT']


Avg_RT , Avg_Acc = [], []

Actual_E = np.array(data2['easyness'])
#print(Actual_E)

new_ssid = 0
RT_new = 0
RT_added = 0
x = 0
acc_new = 0
acc_added = 0


for i in xrange(len(Actual_E)):
    if (np.isnan(Actual_E[i])) == False:
        if 1 > Actual_E[i] > -1:
            if ssid_file2[i] in ssid:
                if ssid_file2[i] == new_ssid:
                    x += 1
                    #print("here"+str(i))
                    RT_new = RT[i]
                    acc_new = acc[i]
                    RT_added = RT_added + RT_new
                    acc_added = acc_added + acc_new
                    #print(RT_added)
                    #code here
                else:
                    #print(i)
                    new_ssid = ssid_file2[i]
                    #print(RT_new, new_ssid,i)
                    if i != 1:
                        Avg_RT.append(RT_added/(x+1))
                        Avg_Acc.append((acc_added/(x+1))*100)
                    #print(x+1)
                    x = 0
                        #print(RT_added / x)
                    RT_added = RT[i]
                    acc_added = acc[i]
print(Avg_Acc)
print(Avg_RT)
for i in xrange(len(Avg_Acc)):
    plt.scatter(Avg_Acc[i],Avg_RT[i])
plt.xlabel("Avg Accuracy")
plt.ylabel("Avg Reaction Time")
plt.show()
