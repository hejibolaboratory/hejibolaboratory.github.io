import matplotlib.pyplot as plt

LegiableFontSize = 20
plt.rc('font', size=LegiableFontSize) #controls default text size
plt.rc('axes', titlesize=LegiableFontSize) #fontsize of the title
plt.rc('axes', labelsize=LegiableFontSize) #fontsize of the x and y labels
plt.rc('xtick', labelsize=LegiableFontSize) #fontsize of the x tick labels
plt.rc('ytick', labelsize=LegiableFontSize) #fontsize of the y tick labels
plt.rc('legend', fontsize=LegiableFontSize) #fontsize of the legend

plt.plot([1, 2, 3, 4])
plt.ylabel('I am a loooooooooooo\noooooooooooong title')
plt.xlabel('I am a loooooooooooo\noooooooooooong title')

plt.show()