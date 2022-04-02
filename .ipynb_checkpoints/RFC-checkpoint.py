from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Random Forest Classification")
    st.write("For the dataset we using, it consists of multiclass problems and Random Forest algorithm is well suited to multiclass situations so this is why we choose Random Forest. Random Forest can also be used to combine numerical and categorical data. Each classifier in the ensemble is a decision tree classifier, with each node's split determined by a random selection of attributes. Each tree votes during classification, and the most popular class is returned.")
    st.write("We used the following parameters in the models - ")
    data = {
        "depth" : [5, 10, 5],
        "trees" : [1000, 1000, 500]
    }
    df = pd.DataFrame(data=data)
    st.table(df)
    st.write("Experiment 1: The figures below shown us the ROC Curves of Random Forest Classifier with the hyperparameters (random\_state=1, n\_estimators=1000, max\_depth=5)")
    st.image(['BASKETS_RF_ROC.png', 'SMOTE_BASKETS_RF_ROC.png'])
    st.image(['AGE_RF_ROC.png', 'SMOTE_AGE_RF_ROC.png'])

    st.write("Experiment 1: The figures below shown us the ROC Curves of Random Forest Classifier with the hyperparameters (random\_state=1, n\_estimators=1000, max\_depth=10)")
    st.image(['BASKETS_RF_ROC1.png', 'SMOTE_BASKETS_RF_ROC1.png'])
    st.image(['AGE_RF_ROC1.png', 'SMOTE_AGE_RF_ROC1.png'])

    st.write("Experiment 1: The figures below shown us the ROC Curves of Random Forest Classifier with the hyperparameters (random\_state=1, n\_estimators=500, max\_depth=5)")
    st.image(['BASKETS_RF_ROC2.png', 'SMOTE_BASKETS_RF_ROC2.png'])
    st.image(['AGE_RF_ROC2.png', 'SMOTE_AGE_RF_ROC2.png'])