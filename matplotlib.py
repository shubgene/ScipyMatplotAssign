# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 23:30:28 2018

@author: shurastogi
"""
import pandas as pd
import matplotlib.pyplot as plt

# Male & female proportion
url="https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"
titanic=pd.read_csv(url)
total_count=titanic['sex'].count()
female_count="{0:.2f}".format(float(len(titanic[titanic['sex']=='female'])/total_count) * 100)
male_count="{0:.2f}".format(float(len(titanic[titanic['sex']=='male'])/total_count) * 100)
labels='Male','Female'
sizes=[male_count,female_count]
figs,s=plt.subplots()
s.pie(sizes,labels=labels,shadow=True,startangle=90)


#2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
plt.scatter(titanic['age'],titanic['fare'],label='scatter Plot',c=pd.factorize(titanic['sex'])[0])