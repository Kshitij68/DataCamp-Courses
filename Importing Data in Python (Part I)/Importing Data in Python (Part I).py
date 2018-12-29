#Flat file - Txt, CSV
#plain text files - marktwain files
file = open("yolo.txt", mode = 'r') #r is to read the text file
text = file.read()
file.close() #Close the connection to the file
#The file is now successfully copied
print(text)
print(file.closed) #To check wheter the file is closed
with open("yolo.txt", mode = 'r') as file: #with is called a context manager
    print(file.read())
data = np.loadtxt(filename, delimiter = ',', skiprows = 1, usecols = [0,2], dtype  = str) #When the file is csv type.
#Delimiter: Seperated by comma, skiprows skips the first row, usecols ensures only first and third coloumn are taken
d = np.recfromcsv(file) #To import csv file

data_array = df.values #Converts the dataframe into numpy array
data = pd.read_csv(file,nrows = 5, header = None) #header = None means no header in the file
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing']) #na_values gives 'Nothing'
#Pickled File: File type specific to python
import pickle
with open('pickle.pkl','rb') as file: #rb is an arguement in open
    data = pickle.load(file)
data = pd.ExcelFile('file.xlsx')
print(data.sheet_names) #Prints the list sheets in the excel file
df1 = data.parse('sheetname') #Load according to sheet name
df1 = data.parse(0) #Load according to index
df2 = xl.parse(1, parse_cols=[0], skiprows=[0], names=['Country']) #What the fuck!!

from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file: #To read SAS file
    df_sas= file.to_data_frame()
data = pd.read_stata("urbanpop.dta") #To read stata files
#HDF5 : Hierachical Data Format Files
import h5py
data = h5py.File('filename','r')
print(type(data)) #prints hdf5 file
for key in data.keys():
    print(key)

import scipy.io
filename = 'work.mat'
mat = filename.io.loadmat(filename)
print(type(mat)) #Dictionary type
print(np.shape(mat['CYratioCyt'])) #Prints the shape of dictionary

from sqlalchemy import create_engine
engine = create_engine('sqlite:///Northwind.sqlite') #Links to the SQL server
table_names = engine.table_names() #Prints the table names

# To select a table from SQL: SELECT * FROM Table_Name
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite') #Links to the SQL server
con = engine.connect()
rs = con.execute('SELET * FROM Orders')
df = pd.DataFrame(rs.fetchall()) #FETCH ALL IN THE PANDAS DATAFRAME
df.columns = rs.keys() #To select all the coloumns in the sql database (coloumn names are not choosen by default)
con.close() #To close the connection

#To save you the trouble of closing the connection, use this method
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite') #Links to the SQL server
with engine.connect() as con:
    rs = con.execute('SELET * FROM Orders')
    df = pd.DataFrame(rs.fetchmany(size = 5)) #Fetches only 5 rows instead of all the rows
    df.columns = rs.keys() #To select all the coloumns in the sql database (coloumn names are not choosen by default)

df = pd.read_sql_query("SELECT * FROM ORDERS",engine)    