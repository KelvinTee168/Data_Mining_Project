from re import S
import pandas as pd
import streamlit as st
import numpy as np

def app():
    st.write("# Primary Findings")
    st.write("The dataset we been used in this project is called **'LaundryData\_2021\_T2.csv'**. After we read the dataset, there are 4000 rows and 22 columns. Below are some details of the Data :")
    st.image('Dataframe.png')
    st.image('Dataframe_dtypes.png')
    st.image('Dataframe_describe.png')
    st.image('Dataframe_describe1.png')
    st.write("Please use the navigation bar to navigate between different parts of the project!")

    #clusters
    st.write("# Clusterings ")
    st.write('Clustering is the process of splitting a population or set of data points into many groups so that data points in the same group are more similar than data points in other groups. To put it another way, the goal is to separate groups with similar characteristics and assign them to clusters.')
    st.write('The clustering technique we used for our analysis is **K-Means Clustering**, we attempted to make use of the location data to cluster the data.')
    st.image(['Coordinate.png','K-Means.png'])

    st.write("# Associations Rule Mining")
    st.write('In transaction databases, relational databases, and other information repositories, association rule mining is the discovery of common patterns, relationships, correlations, or causal structures among collections of items or objects.')
    st.write('We used **Apriori Algorithm**, for our purpose.')
    st.image(['Apriori.png', 'Apriori1.png'])
    st.image(['Apriori2.png', 'Apriori3.png', 'Apriori4.png'])

    st.write("# Missing Data Points ")
    st.write('We looked for missing values in each column. Among the 22 columns, 16 of the columns had missing data. Among the 16 columns only 4 columns had missing data in more than 200 rows. Which none of the columns had missing value in more that 5\% of the rows. After this exploration, we decided to impute the data using SimpleImputer, which is described in the next section')
    st.image(['MissingData.png'])

    st.write("# Imputation ")
    st.write('For the missing values, we have used the strategy called \'most_frequent\' from SimpleImputer. It will replace missing values using the most frequent value along each column. It can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.')
    st.image(['Imputation.png', 'Imputation1.png'])

    st.write("# Age of customers in the laundry shop")
    st.write('The box plot shows that large majority of the customers in the shop age between 30 to 50 years old and the median age of the customers is around 40. Majority of the customers are middle aged people. There are no outliers in the Age_Range and the data is normally distributed.')
    st.image(['Histogram.png', 'Boxplot_1.png'])

    st.write('We can also see the same data apparent in our histogram plot of the Age\_Range variable. There are only a little over 200 people out of 4000 data points who are either less that 20 years old or more than 60 years old.')

    st.write('# Correlation between variables')
    st.write('The heatmap below shows us that the correlation between variables. Inside the diagram, it has shown us that the longitude has a very weak correlation with Age_Range and latitude. Other than that, the other variables has no correlation with each other.')
    st.image('Correlation.png')

