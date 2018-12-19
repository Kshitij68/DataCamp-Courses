"""
What is Spark?
    Platform for cluster computing
    Lets you spread data and computations over clusters with multiple nodes
    Splitting makes it easy to work as each node works on smaller amount of data

    As each node works on subset of data, the calculations including data processing and computation are performed in \
    parallel over the nodes in the cluster
    With greater computing power comes greater complexity

    Deciding whether or not Spark is the best solution for your problem takes some experience, but you can consider \
    questions like these:
        Is my data too big to work on a single machine?
        Can my calculations be easily parallelized?

Using Spark in Python
    First step is to connect to a cluster
    In practice a cluster will be hosted on a remote machine that's connected to all other nodes.
    There will be one computer called the master that manages splitting up the data and the computations
    The master is connected to rest of the computers in the cluster, which are called slaves.
    The master sends the slaves data and calculations to run, and they send their results back to the master

    Creating the connection is as simple as creating an instance of the SparkContext class.
    Cluster takes a few optional arguments that allow you to specify the attributes of the cluster you're connecting to.

    An object holding these attributes can be created with the SparkConf() constructor

"""

# Exercise I
from pyspark import SparkContext
sc = SparkContext()
# Verify that PySpark is connected
print(sc)
# Prints the Spark Version
print(sc.version)

"""
Using DataFrames
    Spark's core data structure is the Resilient Distributed Dataset (RDD)
    Low level object that lets Spark work its magic by splitting the data across multiple nodes in the cluster
    RDD are hard to work with directly, so you'll be using Spark DataFrame abstraction built on top of RDDs
    
    Spark DataFrames were designed to behave a lot like SQL table (which are not only better designed but more \
    optimized to do complicated calculations that RDDs
    
    When you start modifying and combining columns and rows of the data, there are many ways to arrive at the same \
    result, but some often take much longer than others.
    
    To start working you have to create a SparkSession object from your SparkContext
"""
# Exercise II - Creating a Spark Session
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
spark = SparkSession()

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)

# Exercise III - Print tables
# Print the tables in the catalog
print(spark.catalog.listTables())

# Exercise IV - Run Queries
# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()

# Exercise V - Convert Query to Pandas DataFrame
# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())

"""
Create a Spark Cluster from Pandas DataFrame

spark_temp = spark.createDataFrame(pandas_dataframe)

The output of the above code will be stored locally. This means you can use all Spark DataFrame methods on it, but you \
can't access the data in other contexts. For example, .sql() will throw an error. To access the data in this way you \
will have to save it as a temporary table

spark_temp.createOrReplaceTempView()
This creates it as a temporary table 
"""

# Exercise
import pandas as pd

pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(spark.catalog.listTables())

# Add spark_temp to the catalog
# Using createOrReplaceTempView method: This safely creates a new temproray table if nothing was there before,\
# or updates an existing table if one was already defined. This will be useful to avoid running into problems with \
# duplicate tables
spark_temp.createOrReplaceTempView('temp')

# Examine the tables in the catalog again
print(spark.catalog.listTables())

# Exercise
# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path,header = True)

# Show the data
airports.show()