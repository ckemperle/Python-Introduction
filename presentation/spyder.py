# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:18:28 2019

@author: p_Kemperle
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import re

df = pd.read_csv("Automobile_data.csv")
df.head()
df.describe()
df.info()
df.shape

df.rename(columns={'index': 'Index'}, inplace = True)
df.describe()

del df["Index"]
df.head()

sns.barplot(df.company.value_counts().values, df.company.value_counts().index)
plt.bar(df.company.value_counts().index, df.company.value_counts().values)
plt.hist(df.horsepower)
sns.regplot("horsepower", "price", data = df) #regression/scatter plot
sns.pairplot(df, diag_kind = "kde", plot_kws = {"alpha": 0.2}) #pair plot matrix


raw = pd.read_csv("olympics.csv")
raw.head()
raw.describe()

raw = pd.read_csv("olympics.csv", header = 1)
olympics_df = raw
olympics_df.head()

new_names =  {"Unnamed: 0"     : "Country",
               "? Summer"      : "Summer_olympics",
               "01 !"          : "Gold_summer",
               "02 !"          : "Silver_summer",
               "03 !"          : "Bronze_summer",
               "Total"         : "Total_summer",
               "? Winter"      : "Winter_olympics",
               "01 !.1"        : "Gold_winter",
               "02 !.1"        : "Silver_winter",
               "03 !.1"        : "Bronze_winter",
               "Total.1"       : "Total_winter",
               "? Games"       : "#Games",
               "01 !.2"        : "Gold_total",
               "02 !.2"        : "Silver_total",
               "03 !.2"        : "Bronze_total",
               "Combined total": "Combined_total"}

olympics_df.rename(columns = new_names, inplace = True) #inplace overwrites the df directly
olympics_df.head()

olympics_df.info()

olympics_df["Medal_per_game"] = round((olympics_df.Combined_total / olympics_df["#Games"]), ndigits = 1)
olympics_df.head()

medal_ratio = olympics_df.sort_values(by = ["Medal_per_game"], ascending = False)
medal_ratio.head()

sns.barplot(medal_ratio["Medal_per_game"], medal_ratio["Country"][2:13])
plt.bar(medal_ratio["Medal_per_game"], medal_ratio["Country"])
medal_total = olympics_df.sort_values(by = ["Combined_total"], ascending = False)
fig, ax = plt.subplots(1,2)
sns.barplot(medal_ratio["Medal_per_game"], medal_ratio["Country"][2:12], ax = ax[0])
sns.barplot(medal_total["Combined_total"], medal_total["Country"][2:12], ax = ax[1])
plt.tight_layout() #Makes layout prettier
