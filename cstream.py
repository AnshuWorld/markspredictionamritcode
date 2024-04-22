import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
with st.sidebar:
    selected=option_menu("Amrit Keshari",["Marks Prediction"],default_index=0)
st.header(f"Welcome to Our {selected} Page .......")
if selected=="Home":
    user_input = st.number_input("Enter the number of hours you study: ")
    if st.button("Predict"):
        sharaddata = {'Hours_study': [2,3,4,5,6,7,8,9,10], 'Exam_score': [50,60,70,75,80,80,76,56,67]}
        df = pd.DataFrame (sharaddata)
        X = df[['Hours_study']]
        y= df[['Exam_score']]
        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)
        model=LinearRegression()
        model.fit(X_train,y_train)    
        
        predicted_score=model.predict([[user_input]])
        st.write(f"Predicted Exam Score: {predicted_score}")
