# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 23:52:41 2023

@author: manoj kulkarni
"""

import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open('trained_model.sav','rb'))


#creating a function for prediction

def diabetes_prediction(input_data):
    
    input_data_nump=np.asarray(input_data)
    input_data_nump = input_data_nump.reshape(1,-1)
    prediction = loaded_model.predict(input_data_nump)
    
    if(prediction[0]==1):
     return('you are diabetic')
    else:
     return('you are not diabetic')
 
    
def main():
    
    #giving a title 
    st.title('Diabetes Prediction')
    
    #getting the input data from user
    
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose Levels')
    BloodPressure=st.text_input('Blood Pressure')
    SkinThickness=st.text_input('Skin Thinkness Levels')
    Insulin=st.text_input('Insulin Levels')
    BMI=st.text_input('Body Mass Index')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age of the Person')
    
    
    
    #code for pred
    
    diagnosis=''
    
    #creating a button for pred
    
    if st.button('Diabetes Test Result'):
        diagnosis= diabetes_prediction([Pregnancies , Glucose , BloodPressure , SkinThickness , Insulin , BMI , DiabetesPedigreeFunction , Age])
    
   
    st.success(diagnosis)
    
    

    
