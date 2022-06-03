'''
精神警觉任务有5种因变量：中位数反应时，反应时倒数(1/RT)，失误次数(number of lapses) ，最优10%反应时(Optimum response time)和最慢10%反应时倒数(slowest 10% 1/RT)。
https://pythonguides.com/matplotlib-subplot-tutorial/

https://matplotlib.org/stable/gallery/statistics/errorbar_features.html#sphx-glr-gallery-statistics-errorbar-features-py

https://www.tutorialspoint.com/how-to-increase-the-spacing-between-subplots-in-matplotlib-with-subplot2grid#:~:text=How%20to%20increase%20the%20spacing%20between%20subplots%20in,To%20display%20the%20figure%2C%20use%20show%20%28%29%20method.

https://www.delftstack.com/howto/matplotlib/python-matplotlib-plot-superscript/

https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html
'''
import matplotlib.pyplot as plt
import numpy as np
import chineseize_matplotlib

fontsize =24
plt.rc('font', size=fontsize) #controls default text size
plt.rc('axes', titlesize=fontsize) #fontsize of the title
plt.rc('axes', labelsize=fontsize) #fontsize of the x and y labels
plt.rc('xtick', labelsize=fontsize) #fontsize of the x tick labels
plt.rc('ytick', labelsize=fontsize) #fontsize of the y tick labels
plt.rc('legend', fontsize=fontsize) #fontsize of the legend

fig = plt.figure(figsize=(8,6))

# Preparing the data to subplots
x = np.linspace(1, 14, 14) # 14 times, PVT test
#print(x )
y1 = [361.3101852,	339.2678571	,340.1785714,	347,	352.625	,350.5892857,	356.8392857,	353.2857143	,354.125,	365.125,	358.2142857	,348.9821429,	348.6607143	,345.1851852]
error1=[33.85750966,	11.55474985,	10.55487522,	11.76453595,	15.89516484,	17.09162867,	18.46985108	,15.77409045,	17.04813607,	23.26534649,	16.98571351,	19.0097397,	15.64256642	,15.73673719]

# Plot the subplots
# Plot 1




ax1 = plt.subplot()

#plt.plot(x, y1, 'g')
ax1.errorbar(x, y1, yerr=error1, fmt='-k')
ax1.set(ylim=(0, 500))
ax1.set_ylabel("反应时中位数（毫秒）")
#ax1.set_title("(a)反应时中位数")
ax1.set_xticks(np.linspace(1, 14, 14),
 ['飞行前一天', '飞行前二天', '飞行前三天',
 '去程准备阶段', '去程起飞平飞后', '去程准备降落前','去程落地离机前',
 '返程准备阶段', '返程起飞平飞后', '返程准备降落前','返程落地离机前',
  '飞行后一天','飞行后二天', '飞行后三天', ],rotation=90) 

for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

fig.subplots_adjust(bottom = 0.5)
#fig.subplots_adjust(top = 0.06)

ax1.annotate('(a)',xy=(2, 1),xytext=(1, 500))


plt.show()
plt.savefig('/Users/ucdlab/Documents/GitHub/hejibolaboratory.github.io/Graph-advanced/pvt-RT-1-300dpi.png', dpi=300)
