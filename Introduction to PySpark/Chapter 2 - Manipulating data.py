"""
Manipulating data

In this chapter the focus is on using methods defined by Spark's dataframe class to perform common data operations

You can do column wise operations using .withColumn method

Updating Spark DataFrame is somewhat different than Pandas because that Spark DataFrame is immutable. This means it \
cannot be changed and so columns can't be updated in place.

df = df.withColumn("newcol", df.oldCol * 3)
The above code is similar to apply function in pandas
"""