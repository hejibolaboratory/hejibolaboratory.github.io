# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 10:44 下午
# @Author  : mingchun liu
# @Email   : psymingchun@gmail.com
# @File    : 不同学科难度与课程的关系.py
# @Software: PyCharm


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from math import sqrt
import seaborn as sns
import re


file = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_final_data2.csv'

df = pd.read_csv(file, nrows=1000)
df['subject'] = df['subject_onlines'] + df['subject_not_onlines']
print(df.columns)

fig = plt.figure(figsize=(16, 8))
# plt.setp(g.artists, edgecolor='w')
plt.rcParams['font.family'] = 'sans-serif'

plt.ylabel("Star Rating Given by Students", fontsize=12)
plt.xlabel("Student Grade", fontsize=12)
# g = sns.despine(right=True, top=True)  # 去除顶部及右边的线
plt.subplots_adjust(wspace=0.4)
# plt.subplots(figsize=(5, 5))

ax1 = plt.subplot(2, 3, 1)
ax1.set_ylim([1.0, 5.0])
# g = sns.pairplot(df[['student_star', 'student_difficult','subject']], hue='subject')
g = sns.jointplot( x="student_difficult", y="student_star", linewidth=0.5, width=0.8, kind="kde",
                   data=df[["student_difficult", "student_star"]],hue='subject',
                   palette=sns.color_palette('Blues'))
ax1.set_xlabel("Student Grade", fontsize=14)
ax1.set_ylabel("Star Rating Given by Students", fontsize=14)


plt.show()