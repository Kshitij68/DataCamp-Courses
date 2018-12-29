"""
This course is focused on Machine Learning in the context of Time Series
"""
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('abc.csv')
data2 = pd.read_csv('abc.csv')
# Plot the time series in each dataset
fig, axs = plt.subplots(2, 1, figsize=(5, 10))
data.iloc[:1000].plot(y='data_values', ax=axs[0])
data2.iloc[:1000].plot(y='data_values', ax=axs[1])
plt.show()