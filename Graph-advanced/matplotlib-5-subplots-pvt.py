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

plt.figure(figsize=(12,24))

# Preparing the data to subplots
x = np.linspace(1, 14, 14) # 14 times, PVT test
#print(x )
y1 = [361.3101852,	339.2678571	,340.1785714,	347,	352.625	,350.5892857,	356.8392857,	353.2857143	,354.125,	365.125,	358.2142857	,348.9821429,	348.6607143	,345.1851852]
error1=[33.85750966,	11.55474985,	10.55487522,	11.76453595,	15.89516484,	17.09162867,	18.46985108	,15.77409045,	17.04813607,	23.26534649,	16.98571351,	19.0097397,	15.64256642	,15.73673719]

y2 = [0.002886622,	0.002972958	,0.0029596,	0.002904532,	0.002871369,	0.002896478,	0.002846182	,0.002868196,	0.00286367,	0.002798599,	0.002831486,	0.002916896,	0.002906391,	0.002934586]
error2 =[0.000162357,	0.000107002,	9.18786E-05,	9.56932E-05,	0.000113825,	0.00013081,	0.000124547	,0.000122094,	0.000121534,	0.000139579,	0.000121282,	0.000137068,	0.000122806,	0.00011536]
y3 =[0.002891886552,	0.002972958	,0.0029596,	0.002904532,	0.002871369	,0.002896478	,0.002846182,	0.002868196,	0.00286367,	0.002798599,	0.002831486	,0.002916896,	0.002906391,	0.002934586]
error3=[0.000107002,0.000107002,	9.18786E-05,	9.56932E-05,	0.000113825,	0.00013081,	0.000124547	,0.000122094,	0.000121534	,0.000139579,	0.000121282	,0.000137068,	0.000122806,	0.00011536]
y4 = [295.0628307	,283.5892857,	288.1607143,	286.4821429	,291.4285714,	296	,299.75,	295.0535714	,298.125,	301.4464286	,295.4464286	,287.5535714,	293.875	,288.9814815]
error4=[26.26280602,	9.485361425,	9.806046996,	8.155384219,	11.14604817,	12.99096001,	13.37709559,	12.97533817	,14.4291378	,17.13885492,	13.41254936	,12.58217549,	12.75786347,	9.682384547]
y5=[1.939684008	,2.023599933,	2.109410697	,1.96264136	,1.9474808,	2.033877467,	1.975709063,	2.052389005,	1.923437135,	1.961563998,	1.91756035,	2.099922243	,1.998014779,	2.051840488]
error5=[0.211870802	,0.160449297,	0.127659399,	0.172497406,	0.149582233,	0.176574141	,0.173069903,	0.180571025,	0.16096102,	0.158590398,	0.144469159,	0.186442112,	0.218925954	,0.178113607]
# Plot the subplots
# Plot 1

ax = plt.GridSpec(3, 2)
ax.update(wspace=0.2, hspace=0.5)

#fig,(ax1,ax2,ax3,ax4,ax5,ax6) =plt.subplots(6, sharex=True)


ax1 = plt.subplot(ax[0, :])

#plt.plot(x, y1, 'g')
ax1.errorbar(x, y1, yerr=error1, fmt='-k')
ax1.set(ylim=(0, 500))
ax1.set_ylabel("反应时中位数（毫秒）")
ax1.set_title("(a)反应时中位数")
ax1.set_xticks(np.linspace(1, 14, 14),
 ['飞行\n前一天', '飞行\n前二天', '飞行\n前三天',
 '去程\n准备阶段', '去程起飞\n平飞后', '去程准备\n降落前','去程落地\n离机前',
 '返程\n准备阶段', '返程起飞\n平飞后', '返程准备\n降落前','返程落地\n离机前',
  '飞行\n后一天','飞行\n后二天', '飞行\n后三天', ],rotation=90) 

for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

# Plot 2
ax2 = plt.subplot(ax[1, 0])
ax2.errorbar(x, y2, yerr=error2, fmt='-k')
ax2.set(ylim=(0, 0.004))
ax2.set_ylabel("反应时倒数($msec^{-1}$）") 
# make superscript . https://www.tutorialspoint.com/how-do-i-make-sans-serif-superscript-or-subscript-text-in-matplotlib
ax2.set_title("(b)反应时倒数")
ax2.set_xticks(np.linspace(1, 14, 14),
 ['飞行\n前一天', '飞行\n前二天', '飞行\n前三天',
 '去程\n准备阶段', '去程起飞\n平飞后', '去程准备\n降落前','去程落地\n离机前',
 '返程\n准备阶段', '返程起飞\n平飞后', '返程准备\n降落前','返程落地\n离机前',
  '飞行\n后一天','飞行\n后二天', '飞行\n后三天', ],rotation=90) 

for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

# Plot 3
ax3 = plt.subplot(ax[1, 1])
ax3.errorbar(x, y3, yerr=error3, fmt='-k')
ax3.set(ylim=(0, 0.004))
ax3.set_ylabel("失误次数") 
ax3.set_title("(c)失误次数")
ax3.set_xticks(np.linspace(1, 14, 14),
 ['飞行\n前一天', '飞行\n前二天', '飞行\n前三天',
 '去程\n准备阶段', '去程起飞\n平飞后', '去程准备\n降落前','去程落地\n离机前',
 '返程\n准备阶段', '返程起飞\n平飞后', '返程准备\n降落前','返程落地\n离机前',
  '飞行\n后一天','飞行\n后二天', '飞行\n后三天', ],rotation=90) 

for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)


# Plot 4
ax4 = plt.subplot(ax[2, 0])
ax4.errorbar(x, y4, yerr=error4, fmt='-k')
ax4.set(ylim=(0, 400))
ax4.set_ylabel("最优10%反应时（毫秒）") 
ax4.set_title("(d)最优10%反应时")
ax4.set_xticks(np.linspace(1, 14, 14),
 ['飞行\n前一天', '飞行\n前二天', '飞行\n前三天',
 '去程\n准备阶段', '去程起飞\n平飞后', '去程准备\n降落前','去程落地\n离机前',
 '返程\n准备阶段', '返程起飞\n平飞后', '返程准备\n降落前','返程落地\n离机前',
  '飞行\n后一天','飞行\n后二天', '飞行\n后三天', ],rotation=90) 

for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)


# Plot 5
ax5 = plt.subplot(ax[2, 1])
ax5.errorbar(x, y5, yerr=error5, fmt='-k')
ax5.set(ylim=(0, 3))
ax5.set_ylabel("最慢10%反应时倒数($msec^{-1}$）") 
ax5.set_title("(e)最慢10%反应时倒数")
ax5.set_xticks(np.linspace(1, 14, 14),
 ['飞行\n前一天', '飞行\n前二天', '飞行\n前三天',
 '去程\n准备阶段', '去程起飞\n平飞后', '去程准备\n降落前','去程落地\n离机前',
 '返程\n准备阶段', '返程起飞\n平飞后', '返程准备\n降落前','返程落地\n离机前',
  '飞行\n后一天','飞行\n后二天', '飞行\n后三天', ],rotation=90) 

for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

plt.show()
plt.savefig('/Users/ucdlab/Documents/GitHub/hejibolaboratory.github.io/Graph-advanced/pvt-300dpi.png', dpi=1000)
