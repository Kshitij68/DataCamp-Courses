#Pandas has coloumn and row names
import pandas as pd
print(type(AA)) #prints Pandas.core.frame.Dataframe
print(AA.shape) #Prints the shape of the dataframe
print(AA.columns) #Prints the columns of the dataframe
print(AA.iloc[:4,:])
print(AA.head()) #Prints first 5 rows
print(AA.head(0)) #Prints coloumn indexes
print(AA.head(2)) #Prints first two rows
print(AA.tail()) #Prints last 5 rows
print(AA.info())
AA.iloc[::3,-1] = np.nan #Converts every 3rd row in last column into NaN type
low = AA['Date'].values
df_log10 = np.log10(np_vals) #Converts all into log10
da = DataFrame(data) #data: Dictionary format. This makes the keys as column indexes
da['newcolumn'] = 0
da.columns = ['height','gender'] #Changes the column index
da.index = ['A','B','C','D'] #Changes the row index
sunspots = pd.read_csv(filepath, header = None, names = colnames, na_values = '-1')
pd.merge(left=state_populations, right = state_codes,on=None,left_on='state',right_on='name')
