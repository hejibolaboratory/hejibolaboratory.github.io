#!/usr/bin/env python
# coding: utf-8
#the location distribution of professors in each state (bases on the 
# professor_name)
#the method is calculating the number of professors in each state after drop 
#the duplicated names and visualize it
# In[1]:

import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go


# In[2]:

src = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/ratemyprofessor.csv'
df = pd.read_csv(src)


# In[3]:

df = df.drop_duplicates(['professor_name','school_name'],'first', False)
#drop the duplicated professors'name

# In[4]:

df.head(10)


# In[5]:

df = df.groupby(["state_name"], as_index=False)['professor_name'].count()
#calculating the number of professors' names in each state 

# In[6]:

df

# In[7]:

fig = go.Figure(data=go.Choropleth(
    locations=df['state_name'].str.strip(), # Spatial coordinates
    z = df['professor_name'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "The number of professors",
))

fig.update_layout(
    title_text = 'the location distribution of professors',
    geo_scope='usa', # limite map scope to USA
)

py.plot(fig)
