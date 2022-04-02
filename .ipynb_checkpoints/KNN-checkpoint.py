from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# K-Nearest Neighbor Classification")
    st.write("The reason we choose KNN is the KNN algorithm can compete with the most accurate models because it deliver highly precise predictions. As a result, the KNN algorithm can be used in applications that require high accuracy but don't require a human-readable model.")
    st.write("We used the following parameters in the models - ")
    data = {
        "neighbors" : [3, 5, 7],
    }
    df = pd.DataFrame(data=data)
    st.table(df)
    st.write("Experiment 1: The figures below shown us the ROC Curves of KNN with the hyperparameters (neighbors=3)")
    st.image(['BASKETS_RF_ROC.png', 'SMOTE_BASKETS_KNN_ROC.png'])
    st.image(['AGE_RF_ROC.png', 'SMOTE_AGE_KNN_ROC.png'])

    st.write("Experiment 2: The figures below shown us the ROC Curves of KNN with the hyperparameters (neighbors=5)")
    st.image(['BASKETS_RF_ROC1.png', 'SMOTE_BASKETS_KNN_ROC1.png'])
    st.image(['AGE_RF_ROC1.png', 'SMOTE_AGE_KNN_ROC1.png'])

    st.write("Experiment 3: The figures below shown us the ROC Curves of KNN with the hyperparameters (neighbors=7)")
    st.image(['BASKETS_RF_ROC2.png', 'SMOTE_BASKETS_KNN_ROC2.png'])
    st.image(['AGE_RF_ROC2.png', 'SMOTE_AGE_KNN_ROC2.png'])