#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import Libraries i.e pandas
import pandas as pd


# ## Extract data from website(worldometer)

# In[2]:


url = "https://www.worldometers.info/world-population/nigeria-population/"


# In[3]:


pd.read_html(url)


# In[4]:


table1 = pd.read_html(url)[1]
table1.head() # To show the top five(5) rows


# In[5]:


table2 = pd.read_html(url)[2]
table2.head() # To show the top five(5) rows


# In[6]:


table3 = pd.read_html(url)[3]
table3.head() # To show the top five(5) rows


# ## Transform the headers

# In[7]:


table1.columns


# In[8]:


table1.columns = ['Year', 'Population', 'Yearly%Change', 'YearlyChange',
       'Migrants (net)', 'MedianAge', 'FertilityRate', 'Density(P/Km²)',
       'UrbanPop%', 'UrbanPopulation', 'ShareofWorldPop',
       'WorldPopulation', 'NigeriaGlobal Rank']
table1.head()


# In[9]:


table2.columns


# In[10]:


table2.columns = ['Year', 'Population', 'Yearly%Change', 'YearlyChange',
       'Migrants(net)', 'MedianAge', 'FertilityRate', 'Density(P/Km²)',
       'UrbanPop %', 'UrbanPopulation', 'ShareofWorldPop',
       'WorldPopulation', 'Nigeria Global Rank']
    
table2.head()


# In[11]:


table3.columns


# In[12]:


table3.columns = ['SerialNumber', 'CITYNAME', 'POPULATION']
table3.head()


# ## Load data into PostgreSQL Database

# In[13]:


import psycopg2 # For connect to postgresql database and executing queries
from sqlalchemy import create_engine # To efficiently manage and reuse database connections


# In[14]:


# Database Credentials

from sqlalchemy import create_engine
username = 'postgres'
password = '************'
host = 'localhost'
port = 5432
db_name = 'Naija_Population'


# In[15]:

# Establish a connection
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{db_name}', pool_size=10, max_overflow=20)


# In[ ]:


dbt1 = 'Pop2023'
dbt2 = 'PopForcast'
dbt3 = 'PopCity'


# Load Data into database tables

table1.to_sql(dbt1, engine, if_exists='replace', index=False)
table2.to_sql(dbt2, engine, if_exists='replace', index=False)
table3.to_sql(dbt3, engine, if_exists='replace', index=False)

# Close Connection
engine.dispose()





