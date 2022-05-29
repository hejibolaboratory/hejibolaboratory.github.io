
#http://seaborn.pydata.org/examples/pointplot_anova.html

import seaborn as sns
sns.set_theme(style="whitegrid")

import numpy as np
import pandas as pd

# Setting a random seed for reproducibility
np.random.seed(3)

# Numpy Arrays for means and standard deviations
# for each day (variable x)
mus_x = np.array([21.1, 29.9, 36.1])
sd_x = np.array([2.1, 1.94, 2.01])

# Numpy Arrays for means and standard deviations
# for each day (variable y)
mus_y = np.array([64.3, 78.4, 81.1])
sd_y = np.array([2.2, 2.3, 2.39])

# Simulating data for the x and y response variables
x = np.random.normal(mus_x, sd_x, (30, 3))
y = np.random.normal(mus_y, sd_y, (30, 3))

# Creating the "days"
day= ['d1']*30 + ['d2']*30 + ['d3']*30

# Creating a DataFrame from a Dictionary
df = pd.DataFrame({'Day':day, 'x':np.reshape(x, 90, order='F'),
                  'y':np.reshape(y, 90, order='F')})
print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt

fig = plt.gcf()
g=sns.lineplot(x= "x", y="y", 
               
                data=df)

fig.set_size_inches(12, 8)
plt.show()

