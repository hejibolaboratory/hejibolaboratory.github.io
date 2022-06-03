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
y1 = [295.0628307	,283.5892857,	288.1607143,	286.4821429	,291.4285714,	296	,299.75,	295.0535714	,298.125,	301.4464286	,295.4464286	,287.5535714,	293.875	,288.9814815]
error1=[26.26280602,	9.485361425,	9.806046996,	8.155384219,	11.14604817,	12.99096001,	13.37709559,	12.97533817	,14.4291378	,17.13885492,	13.41254936	,12.58217549,	12.75786347,	9.682384547]

# Plot the subplots
# Plot 1




ax1 = plt.subplot()

#plt.plot(x, y1, 'g')
ax1.errorbar(x, y1, yerr=error1, fmt='-k')
ax1.set(ylim=(0, 400))
ax1.set_ylabel("最优10%反应时（毫秒）") 
ax1.set_xticks(np.linspace(1, 14, 14),
 ['飞行前一天', '飞行前二天', '飞行前三天',
 '去程准备阶段', '去程起飞平飞后', '去程准备降落前','去程落地离机前',
 '返程准备阶段', '返程起飞平飞后', '返程准备降落前','返程落地离机前',
  '飞行后一天','飞行后二天', '飞行后三天', ],rotation=90) 

for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

fig.subplots_adjust(bottom = 0.5)
fig.subplots_adjust(left = 0.2)

#fig.subplots_adjust(top = 0.06)

ax1.annotate('(d)',xy=(2, 400),xytext=(1, 400))


plt.show()
plt.savefig('/Users/ucdlab/Documents/GitHub/hejibolaboratory.github.io/Graph-advanced/pvt-RT-1-300dpi.png', dpi=300)
