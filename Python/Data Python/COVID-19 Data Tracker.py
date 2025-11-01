# COVID-19 Data Tracker

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Case_Information.csv')
print(df.columns)

cases_by_region = df['region'].value_counts()
print(cases_by_region)

status_counts = df['status'].value_counts()
print(status_counts)

df['age'].dropna().astype(float).plot(kind='hist', bins=20, figsize=(8,6))
plt.title("Distribution of Case Ages")
plt.xlabel("Age")
plt.ylabel("Number of Cases")
plt.show()