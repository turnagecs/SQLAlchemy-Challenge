#!/usr/bin/env python
# coding: utf-8

# In[130]:


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, desc
import matplotlib
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import pandas as pd


# In[131]:


hawaii_path = '/Users/connorturnage/Desktop/hawaii.sqlite'


# In[132]:


engine = create_engine(f"sqlite:///{hawaii_path}", echo=False)


# In[133]:


engine


# In[134]:


inspector.get_table_names()


# In[135]:


Base = automap_base()


# In[136]:


Base.prepare(engine, reflect=True)


# In[137]:


Base.classes.keys()


# In[138]:


mesure = Base.classes.measurement


# In[139]:


stat = Base.classes.station


# In[140]:


session = Session(engine)


# In[141]:


first_row = session.query(mesure).first()
first_row.__dict__


# In[142]:


session.query(mesure.date).order_by(mesure.date.desc()).first()


# In[143]:


data = session.query(mesure.prcp, mesure.date).    filter(mesure.date >= '2016-08-23').    order_by(mesure.date).all()


# In[144]:


rain = pd.DataFrame(data)
rain
rain.groupby(['date']).agg({'prcp': 'sum'})


# In[146]:


plt.bar(rain['date'], rain['prcp'])
plt.show()


# In[147]:


rain.describe()


# In[148]:


first_row = session.query(stat).first()
first_row.__dict__


# In[149]:


session.query(stat).group_by('id').count()


# In[152]:


data2 = session.query(mesure.station, mesure.tobs)
data2


# In[153]:


stations = pd.DataFrame(data2)
stations


# In[154]:


#Stations with the most observations
stations['station'].value_counts()


# In[159]:


data3 = session.query(mesure.tobs).    filter_by(station = 'USC00519281').    order_by(mesure.date).all()


# In[160]:


temp = pd.DataFrame(data3)
temp


# In[173]:


df = pd.cut(temp['tobs'], 7)
df.to_frame()


# In[177]:


df2 = df.value_counts()
df2.to_frame()


# In[178]:


df2.plot(kind='bar')


# In[ ]:




