# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 01:13:21 2018

@author: Prakhar
"""
#This code applies linear regression to the outcomes of all data for prediction

import pandas as pd
#from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

original_data = pd.read_csv("./Final.csv")
#original_data=original_data.tail(-1)
train_y = original_data.Glucose
fatures = ['Mean','Max','Rms','Min','Vpp']
train_X = original_data[fatures]
#train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(train_X)
print(mean_absolute_error(train_y, melb_preds))
train_X = train_X.sort_values(['Mean'], axis=0, 
                 ascending=True,inplace=True) 
plt.xlabel("Mean (Blue is predicted, Orange is original)")
plt.ylabel("Glucose")
plt.plot(train_X["Rms"],melb_preds)
plt.plot(train_X["Rms"],train_y)
print(arr)

