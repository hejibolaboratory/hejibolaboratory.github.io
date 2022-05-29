#!/usr/bin/env python
# coding: utf-8
#the popularity of courses in each state (based on the would_take_again)
#since the number of valid data in each state is different, this method 
#calculats the percentage of positive anwsers in would_take_again of each
#state and compare the percentage
# In[1]:

import pandas as pd
import plotly.offline as py
import plotly.graph_objects as go


# In[2]:

src = r'F:\何老师课题组\merged.csv'
df = pd.read_csv(src, nrows= 100000)


# In[3]:

df.head(10)


# In[4]:

df = df.dropna(subset=['would_take_agains'])
#drop the Nan data in the would_take_agains

# In[5]:

df.head(10)


# In[6]:

snum = df.groupby(["state_name"], as_index=False)['would_take_agains'].count()
#calculate the total number of valid data in each state

# In[7]:

snum

# In[8]:

df['would_take_agains'] = df['would_take_agains'].map({'Yes': 1, 'No': 0}) 
#change the answer which is yes or no into 0 or 1, so that the positive answer
#can be easier calculated

# In[9]:

df.head(10)

# In[10]:

tnum = df.groupby(["state_name"], as_index=False)['would_take_agains'].sum()
#calculate the number of positive answer in each state using sum

# In[11]:

tnum

# In[12]:

tnum['would_take_agains'] = tnum['would_take_agains']/snum['would_take_agains']
#calculate the percentage of would_take_agains in each state

# In[13]:

fig = go.Figure(data=go.Choropleth(
    locations=tnum['state_name'].str.strip(), # Spatial coordinates
    z = tnum['would_take_agains'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Blues',
    colorbar_title = "The percentage of would_take_again",
))

fig.update_layout(
    title_text = 'the location distribution of welcome professors and courses',
    geo_scope='usa', # limite map scope to USA
)

py.plot(fig)
#visualize the outcome