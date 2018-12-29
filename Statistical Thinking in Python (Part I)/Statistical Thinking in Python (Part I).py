import pandas as pd
df = pd.read_csv('file.csv')
import matplotlib.pyplot as plt
plt.hist(df['name'],bins=10)
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()

import seaborn as sns
sns.set() #Results in nicely formatted plots. Import matplotlib.pyplot and seaborn for this
plt.hist(df['name'],bins=10)
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()

sns.swarmplot(x='state',y='dem_share',data=df_swing)
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()

import numpy as np
x = np.sort(df_swing['dem_share'])
y = np.arange(1,len(x)+1)/len(x) #arange function arange[start_value,stop_value,gap]
plt.plot(x,y,marker='.',linestyle='none') #linestyle = 'none makes dotted line graph
plt.margins(0.02) #Ensures a bufffer of 2% is kept at ends

_ = sns.boxplot(x='east_west',y='dem_share',data=df_all_states)
#Creates a boxplot with x being divided on based of categorical data of east_west

print(np.percentile(petal,percentiles)) #THis prints the 'percentiles' in the array petal
plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',linestyle='none')  #Overlays percentiles as red markers
print(variance_explicit,variance_np) #Prints them adjacently

random = np.random.random(size = 4) #Prints 4 numbers between 0 and 1 (Uniform random distrubution)
sample = np.random.binomial(60,0.1,size = 50) #60:n 0.2:p
sample = np.random.poisson(6,size = 10000)
sample = np.random.normal(mu,sigma,size = 10000)
sample = np.random.exponential(mu,size = 10000)
