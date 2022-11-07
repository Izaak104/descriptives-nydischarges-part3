##import libraries
import pandas as pd
from tableone import TableOne
import matplotlib.pyplot as plt

#import dataframe
df = pd.read_csv('cleaned_data/new_data.csv', index_col=0)
df

##creating a bar chart on the amount of money spent at each facility
data = df.groupby('FACILITY_NAME')['TOTAL_COSTS'].mean()
fig, ax = plt.subplots()

#Defining the plot and its axis
ax.bar(data.index, data.values)
ax.set_title('EXPENSE PER FACILITY')
ax.autoscale()

plt.show()

##creating a pie chart on total costs per gender
data = df.groupby('GENDER')['TOTAL_COSTS'].mean()
fig, ax = plt.subplots()

#Defining the plot and its axis
ax.pie(data.values, labels=data.index, autopct='%1.0f%%')
ax.set_title('EXPENSE PER GENDER')
ax.autoscale()

plt.show()



