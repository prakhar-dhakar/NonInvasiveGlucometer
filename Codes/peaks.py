# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:53:21 2018

@author: Prakhar
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.signal import find_peaks

data = pd.read_csv("./great/Person24.csv",delim_whitespace=False)
print(data)
glucometer = 88
name = "Anirudh"
array = data.iloc[:,0]
#array= data[data.columns[1]]
array=array[500:]
arraydata =array.reset_index(drop=True)
elementstoreduce = len(arraydata)%5
arraydata = arraydata[:-elementstoreduce]

peaks, _ = find_peaks(arraydata,height=0,distance=50)
plt.plot(arraydata)'
plt.plot(arraydata[peaks])
n=4
peakarrayold = (arraydata[peaks])
peakarray = peakarrayold.reset_index(drop=False)  
list_of_lists = [peakarray[i:i+n] for i in range(0, len(peakarray), n)]

final_sd = np.std(list_of_lists[1][list_of_lists[1].columns[1]])
for i in range(0,len(list_of_lists)) :
    xold = list_of_lists[i]
    x = xold.reset_index(drop=True)
    mean = np.mean(x[x.columns[1]])
    sd = np.std(x[x.columns[1]])
    if sd>0 and sd<final_sd and len(x)==n :
        index_begin = x['index'][0]
        index_end = x['index'][n-1] 
        gooddata = arraydata[index_begin:index_end]
        maximum = max(gooddata)
        minimum = min(gooddata)
        arr= [maximum-minimum,maximum,minimum,np.mean(gooddata),np.sqrt(np.mean(gooddata**2)),glucometer,name]
        #plt.plot(gooddata)
plt.xlabel("Time")
plt.ylabel("Voltage")               

            


