import numpy as np
import matplotlib.pyplot as plt

def annotation_line( ax, xmin, xmax, y, text, ytext=0, linecolor='black', linewidth=1, fontsize=12 ):

    ax.annotate('', xy=(xmin, y), xytext=(xmax, y), xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|', 'color':linecolor, 'linewidth':linewidth})
    ax.annotate('', xy=(xmin, y), xytext=(xmax, y), xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '<->', 'color':linecolor, 'linewidth':linewidth})

    xcenter = xmin + (xmax-xmin)/2
    if ytext==0:
        ytext = y + ( ax.get_ylim()[1] - ax.get_ylim()[0] ) / 20

    ax.annotate( text, xy=(xcenter,ytext), ha='center', va='center', fontsize=fontsize)

# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,
		'Python':35}
courses = list(data.keys())
values = list(data.values())

#fig = plt.figure()
fig, ax = plt.subplots(1,1,figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='black',
		width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")

annotation_line( ax=ax, text='Significant', xmin=1, xmax=2, \
                    y=33, ytext=35, linewidth=2, linecolor='black', fontsize=18 )

plt.show()
