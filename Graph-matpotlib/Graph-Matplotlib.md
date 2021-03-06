---
marp: true
size: 16:9
class:
  - invert
  - lead
color: white
backgroundImage: url(bg-image.png)
paginate: true
footer: "Copyright by Jibo He"
---
# Scientific Graph with Python + Matplotlib

# 如何使用Python + Matplotlib绘制期刊论文发表标准的图？

## by Jibo He/何吉波

清华大学社会科学学院心理学系
hejibolaboratory@pku.org.cn
version:2022-05-22

---

# 画图重点与技巧

- 1. 显示中文
- 2. 标题或者y-label过长，换行显示
- 3. 如何以期刊要求的300DPI保存图片
- 4. 如何改变线条颜色与风格
- 5. 如何改变字体大小
- 6. 标注显著
- 7. 画图技巧 7. 去掉上方和右侧的边框/spines
  8. 如何增加左方和下方的padding，让图片完整可见？

---

# 画图重点与技巧 （您的思考题，下次再来找我继续学习）

- 8. 如何让y-axis断裂，不从0开始 [todo]
- 9. 如何设置xlim, ylim,坐标范围？[todo]
- 10. 如何绘制放在网上的可以交互的图[todo]
- 11. 如何对大数据（>5g）的数据画图 [todo]
- 12. Excel, SPSS,代码画图对比[todo]
- 13. ErrBar 带标准差的柱状图 [todo]
- 14. 如何去掉legend/图例的边框 [todo]

---

# 画图重点与技巧 （您的思考题，下次再来找我继续学习）

- 15. 如何改变xticklabel？[todo]
- 16. 如何绘制line plot with shaded error [todo]
- 17. 如何绘制violin plot with bar graph [todo]
- 18. 如何指定font style [todo]
- 19. 如何选择正确的图的类型 [todo]
- 20. 如何绘制可以动，可以强调的动效图 [todo]

---

# 为什么不用Excel画图？

- 确保图片是300DPI的清晰度
- 为了重用代码，不重复点击操作
- 为了确保图片的长宽比一致（aspect ratio）或者高度一致

---

# 期刊对图片的要求

## 以顶刊Accident Analysis and Prevention为例

### source: https://www.elsevier.com/journals/accident-analysis-and-prevention/0001-4575/guide-for-authors

TIFF (or JPG): Color or grayscale photographs (halftones): always use a `<span style="color:red;">` minimum of 300 dpi .
TIFF (or JPG): Bitmapped line drawings: use a minimum of 1000 dpi.
TIFF (or JPG): Combinations bitmapped line/half-tone (color or grayscale): a minimum of 500 dpi is required.
Please do not:
• Supply files that are optimized for screen use (e.g., GIF, BMP, PICT, WPG); the resolution is too low.

---

# package installation

pip install chineseize-matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

---

# Introduction to Matplotlib

“make easy things easy and hard things possible“

- create simple plots with just a few commands
- “emulate” MATLABs plotting capabilities

matplotlib is conceptually divided into three parts

- Pylab interface : MATLAB like plotting
- Matplotlib API : abstract interface
- Backends : managing the output

available at (including many examples)
		http://matplotlib.sourceforge.net/

---

# The Matplotlib Gallery

## http://matplotlib.sourceforge.net/gallery.html

![width:900px](matplotlib-gallery.png)

---

# Basic 2D - plotting

![width:900px](2d-plots.jpeg)

---

# Basic 2D - plotting

```python
import numpy as np 	# import numpy
import pylab as pl		# import pylab interface

times = np.arange ( 0, 5, 0.01 ) 	# define x-vector
fun  = lambda x : np.cos (20 *x) * np.exp (- pl.absolute(x) )
		# define some function fun (x)

pl.plot ( times, fun(times) ) 	# plot fun (t) vs. t
pl.xlabel ('time' ) 		# creating x-label
pl.ylabel ('position')		# creating y-label

pl.title ( 'damped oscillation') 	# setting the title
pl.show()				 # show the plot

```

---

# subplots

## subplot (2,1,1) :

 2 columns, 1 row
 choose first subplot
! Indexing starts with 1

![width:600px](subplots.png)

---

# subplots

```python
import numpy as np 	# import numpy
import pylab as pl		# import pylab interface

times = np.arange ( 0, 5, 0.01 ) 	# define x-vector

fun   = lambda x : np.cos (20 *x) * np.exp (- pl.absolute(x) )
fun2  = lambda x : np.sin (10 *x**2)  	# define two functions


pl.subplot (2,1,1)		# choose a subplot ( rows, colums, idx)
pl.plot ( times, fun(times) )	# plot fun(t)

pl.subplot (2,1,2)		# choose a subplot ( rows, colums, idx)
pl.plot ( times, fun2(times) ) 	# plot fun2(t)

pl.show()

```

---

# Subplots Exercise

How to make the figures side by side?

# Other basic plotting commands

pl.bar () 	     # box plot

pl.errorbar()	     # plot with errorbars

pl.loglog()	     # logarithmically scaled axis

pl.semilogx ()   # x-axis logarithmically scaled

pl.semilogy ()  # y-axis logarithmically scaled

---

# Histograms

```python
import numpy as np 	# import numpy
import pylab as pl		# import pylab interface

data = 3. + 3. * np.random.randn (100000)
	# generate normally distributed randonnumbers

pl.subplot (2,1,1)
pl.hist (data, 100)	# make histogram with 100 bins

pl.subplot (2,1,2)
pl.hist ( data, bins = np.arange(3, 25, 0.1) ) 
		# make histogram with given bins

pl.axis ( (3, 15,0,2000 ))	 # specify axis (x1,x2,y1,y2)

pl.show()

```

---

# Histograms

(automatic) histogram with 100 bins

histogram for data between 3. and 25. with binsize 0.1
axis set to (3,15,0,2000)

![width:500px](histogram.png)

---

# 如何绘制柱状图bar graph

```python
import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'C':20, 'C++':15, 'Java':30,
		'Python':35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='maroon',
		width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

```

---

# 画图技巧 1. 显示中文

## chineseize-matplotlib 自动设置 matplotlib 中文字体

```python
import matplotlib.pyplot as plt
import chineseize_matplotlib

plt.plot([1, 2, 3, 4])
plt.xlabel('简单图表')
plt.show()

```

https://pypi.org/project/chineseize-matplotlib/

---

# 画图技巧 2.通过换行显示一个很长的title或者label

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
#plt.xlabel('I am a loooooooooooooooooooooooong title')
plt.xlabel('I am a loooooooooooo\noooooooooooong title')

plt.show()

```

---

# 画图技巧 3.如何以期刊要求的300DPI保存图片

```python
import numpy as np 	# import numpy
import pylab as pl		# import pylab interface
fig = pl.figure()
times = np.arange ( 0, 5, 0.01 ) 	# define x-vector
fun  = lambda x : np.cos (20 *x) * np.exp (- pl.absolute(x) )
		# define some function fun (x)
pl.plot ( times, fun(times) ) 	# plot fun (t) vs. t
pl.xlabel ('time' ) 		# creating x-label
pl.ylabel ('position')		# creating y-label
pl.title ( 'damped oscillation') 	# setting the title

fig.set_size_inches(30.,18.)
## ensuare the figure is saved in 300 dpi, high resolution enough for publication purposes.
pl.savefig('/Users/ucdlab/Desktop/Course /Python - 大数据 /清华Python 2022/Graph-matpotlib/300dpi.png', dpi=300)
pl.show()

```

---
## 画图技巧 4. 如何改变线条颜色与风格 - color参数的常用颜色缩写
| 颜色缩写 | 代表的颜色 | 英文全文 |
| -------- | ---------- | -------- |
| b        | 蓝色       |   <p style="background-color:blue;">blue </p>    |
| g        | 绿色       |   <p style="background-color:green;">green </p>   |
| r        | 红色       |    <p style="background-color:red;">red </p>  |
| c        | 青色       |   <p style="background-color:cyan;">cyan </p>   |
| m        | 品红       | <p style="background-color:magenta;">magenta </p>   |
| y        | 黄色       | <p style="background-color:yellow;">yellow </p>   |
| k        | 黑色       |   <p style="background-color:black;">black </p>   |
| w        | 白色       |   <p style="background-color:white;">white </p>   |

---

# 画图技巧 4. 如何改变线条颜色与风格

<div class="row">
  <div class="col-md-8" markdown="1">

```python
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

plt.plot(x, x + 4, linestyle='-')  # 实线
plt.plot(x, x + 5, linestyle='--') # 虚线
plt.plot(x, x + 6, linestyle='-.') # 长短点虚线
plt.plot(x, x + 7, linestyle=':');  # 点线
```

</div>

<div class="col-md-4" markdown="1">

<img align="right" width="300" height="300" src="Graph-with-different-line-style.jpg">
</div></div>

---

# 画图技巧 4. 如何改变线条颜色与风格

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4],color = 'black',linestyle="dashed")

plt.plot([ 3, 4,1, 2],color = 'black',linestyle="dotted")

#supported  values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

plt.ylabel('I am a ylabel')
plt.xlabel('I am a loooooooooooo\noooooooooooong title')

plt.show()

```

---

# 画图技巧 5. 如何改变字体大小

```python
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

```

---

# 画图技巧 6. 如何标注显著或者其它文字 （部分）

```python
import numpy as np
import matplotlib.pyplot as plt

def annotation_line( ax, xmin, xmax, y, text, ytext=0, linecolor='black', linewidth=1, fontsize=12 ):
 if ytext==0:
        ytext = y + ( ax.get_ylim()[1] - ax.get_ylim()[0] ) / 20

    ax.annotate( text, xy=(xcenter,ytext), ha='center', va='center', fontsize=fontsize)
    ax.annotate('', xy=(xmin, y), xytext=(xmax, y), xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|', 'color':linecolor, 'linewidth':linewidth})
    ax.annotate('', xy=(xmin, y), xytext=(xmax, y), xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '<->', 'color':linecolor, 'linewidth':linewidth})

    xcenter = xmin + (xmax-xmin)/2
```

References: https://stackoverflow.com/questions/38677467/how-to-annotate-a-range-of-the-x-axis-in-matplotlib

---

# 画图技巧 6. 如何标注显著或者其它文字

```python
import numpy as np
import matplotlib.pyplot as plt

def annotation_line( ax, xmin, xmax, y, text, ytext=0, linecolor='black', linewidth=1, fontsize=12 ):
 if ytext==0:
        ytext = y + ( ax.get_ylim()[1] - ax.get_ylim()[0] ) / 20

    ax.annotate( text, xy=(xcenter,ytext), ha='center', va='center', fontsize=fontsize)
    ax.annotate('', xy=(xmin, y), xytext=(xmax, y), xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '|-|', 'color':linecolor, 'linewidth':linewidth})
    ax.annotate('', xy=(xmin, y), xytext=(xmax, y), xycoords='data', textcoords='data',
            arrowprops={'arrowstyle': '<->', 'color':linecolor, 'linewidth':linewidth})

    xcenter = xmin + (xmax-xmin)/2
   

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

```

---

# 画图技巧 6. 如何标注显著或者其它文字 （效果图）

![width:1000px](Annotate-Significance.png)

---

# 画图技巧 7. 去掉上方和右侧的边框/spines

使用plt.gca().spines["top"].set_visible(False)去掉上方的边框

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('I am a ylabel')
plt.xlabel('I am a loooooooooooo\noooooooooooong title')

# Iterating over all the axes in the figure
# and make the Spines Visibility as False
for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

plt.show()
```

---

# 画图技巧 7. 去掉上方和右侧的边框/spines (效果图)

![width:800px](RemoveUpperRightFrame-demo.png)

---

# 画图技巧 8.如何增加左方和下方的padding，让图片完整可见？

```python
# raised and solved by Li Ming 2022
import colorsys
import numpy as np
import matplotlib.pyplot as plt

#data from National Bureau of Statistics
# http://www.stats.gov.cn/

year=[1970,1980,1990,2000,2010,2020]
add_value={
    'agriculture':[793.3,1359.5,5017.2,14717.4,38430.8,78030.9],
    'industry':[918.1,2204.7,7744.1,45663.7,191626.5,383562.4],
    'service industry':[568.3,1023.4,6111.6,39899.1,182061.9,551973.7]
}
fig,ax=plt.subplots()
ax.stackplot(year,add_value.values(),
         
             labels=add_value.keys(),colors=['k','0.8','0.3'])
ax.legend(loc='upper left')
ax.set_title('The added value of the three industries')
ax.set_xlabel('Year')
ax.set_ylabel('The added value(billion)')
plt.savefig('HW5.png',dpi=300)
plt.show()
```

---

# 画图技巧 8.如何增加左方和下方的padding，让图片完整可见？

![width:800px](issue-y-label-not-visiable.png)

---

# 画图技巧 8.如何增加左方和下方的padding，让图片完整可见？(解决方案)

通过以下的subplots_adjust函数，在下方和左方增加空格间隙padding

```python
fig.subplots_adjust(bottom = 0.1)
fig.subplots_adjust(left = 0.2)
```

---

# 画图技巧 8.如何增加左方和下方的padding，让图片完整可见？(效果图)

```python
#作业五：做一张可发表的图(中国三大产业增加值变化)

import colorsys
import numpy as np
import matplotlib.pyplot as plt
year=[1970,1980,1990,2000,2010,2020]
add_value={
    'agriculture':[793.3,1359.5,5017.2,14717.4,38430.8,78030.9],
    'industry':[918.1,2204.7,7744.1,45663.7,191626.5,383562.4],
    'service industry':[568.3,1023.4,6111.6,39899.1,182061.9,551973.7]
}
fig,ax=plt.subplots()
fig.subplots_adjust(bottom = 0.1)
fig.subplots_adjust(left = 0.2)
ax.stackplot(year,add_value.values(),
             labels=add_value.keys(),colors=['k','0.8','0.3'])
ax.legend(loc='upper left')
ax.set_title('The added value of the three industries')
ax.set_xlabel('Year')
ax.set_ylabel('The added value(billion)')
plt.savefig('HW5.png',dpi=300)
plt.show()
```

---

# 画图技巧 8.如何增加左方和下方的padding，让图片完整可见？(效果图)

![width:600px](issue8-solution-y-label-not-visiable.png)

---

# References for Matplotlib-2

![width:500px](matplotlib-reference-manual-2.jpeg)

---

# References for Matplotlib-3

![width:500px](matplotlib-reference-manual-3.jpeg)

---

# References for Matplotlib-4

![width:500px](matplotlib-reference-manual-4.jpeg)

---

# useful websites:

https://blog.csdn.net/weixin_52797843/article/details/125038128?spm=1000.2115.3001.6382&utm_medium=distribute.pc_feed_v2.none-task-blog-hot-8-125038128-null-null.pc_personrec&depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot-8-125038128-null-null.pc_personrec
