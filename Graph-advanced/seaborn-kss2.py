
#http://seaborn.pydata.org/examples/pointplot_anova.html
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import chineseize_matplotlib
fig, ax = plt.subplots()

file = "/Users/ucdlab/Documents/GitHub/hejibolaboratory.github.io/Graph-advanced/kss-score.xlsx"
data = pd.read_excel(file) #reading file
 
print(data)

data.head()

g=sns.lineplot(x= "time", y="kss",estimator=np.mean, ci=95, data=data)


g.set(ylim=(0, 9))

ax.tick_params(axis='x', labelrotation = 90)
fig.set_size_inches(12, 14)
plt.ylabel('主观疲劳（KSS）')
plt.xlabel('时间')

# Iterating over all the axes in the figure
# and make the Spines Visibility as False
for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

fontsize = 16
plt.rc('font', size=fontsize) #controls default text size
plt.rc('axes', titlesize=fontsize) #fontsize of the title
plt.rc('axes', labelsize=fontsize) #fontsize of the x and y labels
plt.rc('xtick', labelsize=fontsize) #fontsize of the x tick labels
plt.rc('ytick', labelsize=fontsize) #fontsize of the y tick labels
plt.rc('legend', fontsize=fontsize) #fontsize of the legend

#add more margins at the bottom to make it visiable for xlabel
fig.subplots_adjust(bottom = 0.5)
plt.savefig('/Users/ucdlab/Documents/GitHub/hejibolaboratory.github.io/Graph-advanced/kss-score-300dpi.png', dpi=300)
plt.show()

