import matplotlib.pyplot as plt
year = [1950,1960,1980,1990]
pop = [2,3,4,5]

plt.plot(year,pop) #(x,y)
plt.show() #Show the plot

plt.scatter(year,pop)
plt.show()


plt.xscale('log') #To make the x axis scale as logarithmic
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population Projections")
plt.xticks([0,1,2],["OB","1B","2B"])
plt.yticks([123,123,134,14,5,])
values = [1,2,33]
plt.hist(values,bins = 10)

plt.clf() #Clears the plots


plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col,alpha = 0.8)
#Here s is for giving the size of the bubble based on np_pop value
#Here c is for giving the colors from color matrix
#Here alpha is to change the opacity of the matrix
plt.text(1550, 71, 'India') #To write something in front of a particular bubble
plt.grid(True) #To activate gridlines in yout plot

world = {"a":1,"b":2,"c":3} #Creates a dictionary
world['a'] #Prints 1
print(world.keys()) # Prints dict_keys(['a', 'b', 'c', 'd'])
world = {"a":1,"b":2,"c":3, "a":4} #Overwrites a =1
for key,value in world.items(): print(key); print(value)
world["sea"] = 24 #Adds an element in the dictonary at the end
del world["sea"] #Deletes the key and its value
europe = { 'spain': { 'c':'m', 'popu':46.77 },'france': { 'al':'pas', 'pot':66.03 },}

#Numpy elements can house array with only one data type
#Pandas can take elements of all types and combine them
#Each row and coloum have a unique labels
import pandas as pd
pd.read_csv("ADDRESS",index_col = 0) #To tell the first coloum contains the indexes for rows
cars = pd.DataFrame(my_dict) #Stores the list/dictonary as pandas dataframe
cars.index = row_labels #To specify the row indexes of dataframe from list row_labels
# print(brics["country"]) #Returns the elements of the coloum coutnry
# print(brics[["country"]]) #Returns the elements of the coloumn country in a dataframe format
# #THis is actually a list in a dataframe
# print(type(brics["country"])) #Returns the type which is pandas.core.series.Series
# print(type(brics[["country"]])) #Returns in a dataframe format
#brics[1:4] #Index starts with zero
#brics.loc["US"] #loc is to select based on labels. Returns the row with index US
#brics.locs[["RU","IN","CH"],["country","capital"]] #Returns row index as RU IN CH and coloum index as country and capital
#brics.iloc[1] #iloc is to select based on positions. Returns the 2nd row (starts with zero)

x = 1
y = 3
print(x>1 and y > 3)
#And Or Not operators work in variables but not in arrays, lists, tuples, dataframes etc
#To use comparision operators with numpy use the following:

is_huge = brics["area"] > 30 #Subsets the data frame and prints the same with values True or False
print(brics[is_huge])

import numpy as np
np.logical_and()
np.logical_or()
np.logical_not()

fam = [1,2,3,4,5]
for h in fam: print(h) #prints each element
for index,height in enumerate(fam):
    print("index " + str(index) + ": "+ str(height)) #First one gets the index value and second one gets the element value

fam = [10, 20, 30, 40, 50]
for height, index in enumerate(fam):
    print(index)
    print(height)

for i in np.nditer(arr):  # Iterates over the array

# brics is a pandas dataframe
for i in #brics: print(i)  # This will print the coloumn names only
for lab, row in brics.iterrow():  # lab: Row lablel #Row: Row element
    print(lab)  # Prints out the label once and does not print rest of them until all elements are printed
    print(row)  # Prints out all the elements of that particular label
for lab, row in brics.iterrow():
    print(lab + row["capital"])  # only prints the label and the capital
    #brics.loc[lab, "name_length"] = len(
        #row["country"])  # Makes a new coloumn in dataframe with lenght of the string in country
# The method in above line is very inefficient though and takes a lot of computation power
#brics["name_length"] = brics["country"].apply(
    len)  # Applies the length function rows in country and prints in newcoloumn
np.random.rand()  # Returns a number between 0 and 1 (Uniform Distribution)
np.random.seed(123)  # Set the seed t ensure reproducibility
coin = np.random.randint(0, 2)  # Generates a integer random number between 0 and 2 (not including 2)(including 0)
