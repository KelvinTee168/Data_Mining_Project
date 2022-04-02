from re import S
import pandas as pd
import streamlit as st
import numpy as np

# import q1
# import q2
# import q3
# import q4
# import q5
# import q6
# import q7
# import q8
# import q9
# import q10
# import q11
# import q12
# import q13
# import q14
import home
import eda
import SVR
import DTR
import NB
import RFC
import KNN
import NeuralNet

st.set_page_config(page_title='What\'s interesting about a Laundry Shop?', page_icon=None, layout="wide",
                    initial_sidebar_state="auto", menu_items=None)
PAGES = {
    "Home" : home,
    "Exploratory Data Analyis" : eda,
    "Models - Regression (SVR) ": SVR,
    "Models - Regression (DecisionTree)": DTR,
    "Models - Classification (NB)" : NB,
    "Models - Classification (RFC)" : RFC,
    "Models - Classification (KNN)" : KNN,
    "Models - Classification (NN)" : NeuralNet,
}
st.sidebar.title('The Data Mining Process')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()









