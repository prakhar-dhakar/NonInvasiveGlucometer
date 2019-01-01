# -*- coding: utf-8 -*-
"""
@author: Prakhar
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


original_data = pd.read_csv("./Final.csv")
print(original_data)
original_data.sort_values(["Glucose"], axis=0, 
                 ascending=True, inplace=True) 
plt.plot(original_data["Rms"],original_data["Glucose"])
#plt.plot(original_data["Rms"],original_data["Glucose"])
plt.xlabel("Rms")
plt.ylabel("Glucose")
plt.title("Graph")
linefit = np.polyfit(original_data["Rms"],original_data["Glucose"],deg=1, rcond=None, full=False)
print(linefit)
#plt.savefig("Vpp.png")
m,b=linefit
for i in range(int(min(original_data["Rms"])), int(max(original_data["Rms"]))):
    plt.plot(i, 1.2*(i * m + b), 'go')
plt.show()