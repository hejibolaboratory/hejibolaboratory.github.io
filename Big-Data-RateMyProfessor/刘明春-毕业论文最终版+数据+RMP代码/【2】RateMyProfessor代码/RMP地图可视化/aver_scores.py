#!/usr/bin/env python
# coding: utf-8
#the content level of courses in each state (bases on the star_rating)
#the method is calculating the average scores of star_rating in each state and
#visualize it
# In[1]:

import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go


# In[2]:

src = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/ratemyprofessor.csv'
df = pd.read_csv(src, nrows= 100000)


# In[3]:

df.head(10)

# In[4]:

df = df.dropna(subset=['star_rating'])
#drop the empty data in star_rating

# In[5]:

df.count()

# In[6]:

df.head(10)

# In[7]:

df = df.groupby(["state_name"], as_index=False)['star_rating'].mean()
#calculating the average of scores in each state

# In[8]:

df

# In[9]:

fig = go.Figure(data=go.Choropleth(
    locations=df['state_name'].str.strip(), # Spatial coordinates
    z = df['star_rating'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "The average scores",
))

fig.update_layout(
    title_text = 'the comparison of scores in each state',
    geo_scope='usa', # limite map scope to USA
)

py.plot(fig)
#visualize the outcome