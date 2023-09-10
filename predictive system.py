# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_model=pickle.load(open('C:/Users\manoj kulkarni/OneDrive/Desktop/machine learning/models/trained_model.sav','rb')) 
input_data=(1,103,30,38,83,43.3,0.183,33)
input_data_nump=np.asarray(input_data)
input_data_nump = input_data_nump.reshape(1,-1)
prediction = loaded_model.predict(input_data_nump)

if(prediction[0]==1):
 print('you are diabetic')
else:
 print('you are not diabetic')