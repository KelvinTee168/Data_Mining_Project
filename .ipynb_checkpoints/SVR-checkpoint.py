from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Support Vector Regression")
    st.write("SVR can be used to tackle the same problems as linear regression solves. Unlike linear regression, however, SVR allows you to model non-linear connections between variables and allows you to tune hyperparameters to change the model's robustness.")

    st.write("The graph below is the regplot of Support Vector Regression for Age_Range.")
    st.image('SVR.png')
    
    st.write("Two error metrics have been used for evaluating and reporting the performance of Support Vector Regression")
    st.write("mean absolute error: 10.23561709468476")
    st.write("mean squared error: 140.8668354505676")
