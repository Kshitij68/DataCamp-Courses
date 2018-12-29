"""
A relational database consists of tables
Tables can be related to one another by using keys

SQLAlchemy
Generate SQL queries using Python code
Tow main pieces:
    Core (Relational Model Focused)
    ORM (Object Relational Model)

There are many different types of databases:
    SQLite
    PostgreSQL
    MySQL
    MS SQL
    Oracle


An engine is a common interface to the database from SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite://census_nyc.sqlite')
connection = engine.connect()
print(engine.table_names())

Reflection
Reflection reads database and builds SQLAlchemy table objects
from sqlalchemy import MetaData, Table
metadeta = Metadeta()
census = Table('census',metadeta,autoload = True, autoload_wit=engine)
print(repr(census))
"""

# Import create_engine
from sqlalchemy import create_engine, Table, MetaData
# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print table names
print(engine.table_names())
# Print census table metadata
print(repr(census))
# Print the column names
print(census.columns.keys())
# Print full table metadata
print(repr(metadata.tables['census']))

"""
Basic SQL Querying
from sqlalchemy import create_engine
engine = create_engine('sqlite:///census_nyc.sqlite')
connection = engine.connect()
stmt = 'SELECT * from people'
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()

first_row = results[0]
print(first_row)

print(first_row.keys())
print(first_row.state)
"""


