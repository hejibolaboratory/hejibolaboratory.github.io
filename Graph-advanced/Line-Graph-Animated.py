#https://holypython.com/python-visualization-tutorial/guide-to-python-animations-animating-line-charts/
import random
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
#%matplotlib qt

l1 = [random.randint(-10,4)+(i**1.68)/(random.randint(13,14)) for i in range(0,160,2)]
l2 = [random.randint(0,4)+(i**1.5)/(random.randint(9,11)) for i in range(0,160,2)]
l3 = [random.randint(-10,10)-(i**1.3)/(random.randint(11,12)) for i in range(0,160,2)]
l4 = [random.randint(0,4)+(i**1.6)/(random.randint(10,13)) for i in range(0,160,2)]

fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (15,5))
axes.set_ylim(-100, 500)
axes.set_xlim(0, 250)
plt.style.use("ggplot")

x1,y1,y2,y3 = [], [], [], []
xval = count(0,3)
def animate(i):
    x1.append(next(xval))
    y1.append((l1[i]))
    y2.append((l2[i]))
    y3.append((l3[i]))

    axes.plot(x1,y1, color="red")
    axes.plot(x1,y2, color="gray", linewidth=0.5)
    axes.plot(x1,y3, color="blue")
    
anim = FuncAnimation(fig, animate, interval=30)
anim.save("anim.gif")
plt.show()