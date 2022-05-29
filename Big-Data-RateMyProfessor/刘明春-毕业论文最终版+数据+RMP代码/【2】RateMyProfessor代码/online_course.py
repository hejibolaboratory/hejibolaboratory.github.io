# -*- coding: utf-8 -*-
# @Time    : 2020/3/10 9:47 下午
# @Author  : mingchun liu
# @Email   : psymingchun@gmail.com
# @File    : online_course.py
# @Software: PyCharm

import pandas as pd
import researchpy as rp
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from math import sqrt

file = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_final_data2.csv'
# # 增加课程及教授
def add_course_level():
    df = pd.read_csv(file)
    print(df.columns)
    df['course_number'] = df['subject_onlines_level'] + df['subject_not_onlines_level']
    class_order = []
    for i in df['course_number']:
        class_order.append(str(i)[0])
    df['class_order'] = class_order
    professor = []
    for i in df['year_since_first_review']:
        if i >= 0 and i <= 6:
            professor.append('assistant')
        elif i >6 and i <= 12:
            professor.append('associate')
        elif i >12  and i <= 20:
            professor.append('full')
        else:
            professor.append('null')
    df['professor'] = professor
    print(df.columns)
    # df.to_csv(r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_final_data2.csv', index=False)

'''1。比较在线课程与线下课程的学生评分、课程难度'''
def online_offline_rating():
    df = pd.read_csv(file, usecols=['IsCourseOnline', 'student_star','student_difficult'])
    pd.set_option('display.max_columns', None)
    # print(df.columns)
    online_professor = df[(df['IsCourseOnline'] == 1)]
    offline_professor = df[(df['IsCourseOnline'] == 0)]

    print('评分差异--------------------')
    online_rating = rp.summary_cont(online_professor['student_star'])
    offline_rating = rp.summary_cont(offline_professor['student_star'])
    print('online评分', online_rating)
    print('offline评分', offline_rating)
    # # 非参数检验
    p = stats.mannwhitneyu(online_professor['student_star'], offline_professor ['student_star'], alternative='two-sided')
    print('mannwhitneyu:',p)
    # # 效应量, https://www.psychometrica.de/effect_size.html
    cohens_d = (offline_rating.Mean  - online_rating.Mean) / (sqrt((online_rating.SD ** 2 + offline_rating.SD ** 2) / 2))
    print('评分差异效应量, cohens_d:', cohens_d)

    print('课程难度差异--------------------')
    online_rating = rp.summary_cont(online_professor['student_difficult'])
    offline_rating = rp.summary_cont(offline_professor['student_difficult'])
    print('online课程难度', online_rating)
    print('offline课程难度', offline_rating)
    # # 非参数检验
    p = stats.mannwhitneyu(online_professor['student_difficult'], offline_professor['student_difficult'], alternative='two-sided')
    print('mannwhitneyu:', p)
    # # 效应量, https://www.psychometrica.de/effect_size.html
    cohens_d = (online_rating.Mean - offline_rating.Mean) / (sqrt((online_rating.SD ** 2 + offline_rating.SD ** 2) / 2))
    print('课程难度效应量, cohens_d:', cohens_d)

    # from numpy import median
    # g = sns.catplot(x="IsCourseOnline", y="student_star", hue="IsCourseOnline", kind="bar", data=df, ci='sd', color='grey')
    # plt.ylim([1, 5])
    # plt.ylabel("Students Rating", fontsize=12)
    # plt.xlabel("Student Grade", fontsize=12)
    # plt.show()

'''2。比较 不同学科，online offline  3*2 的 教授总评分'''
def subject_analysis():
    df= pd.read_csv(file, usecols=['student_star', 'student_difficult','IsCourseOnline','subject_onlines','subject_not_onlines'])
    subject = ['Accounting', 'Arts ', 'Business', 'Chemistry', 'Computer Science', 'Economics', 'English', 'Law', 'Math', 'Physics', 'Psychology', 'Social science']
    for i in subject:
        df2 = df[(df['IsCourseOnline'] == 1) & (df['subject_onlines'] == i)]  #在线课程
        df3 = df[(df['IsCourseOnline'] == 0) & (df['subject_not_onlines'] == i)]  #非在线课程
        # # 非参数检验
        # p = stats.mannwhitneyu(df2['student_star'], df3['student_star'],alternative='two-sided')
        p = stats.mannwhitneyu(df2['student_difficult'], df3['student_difficult'],alternative='two-sided')
        # print(i,'mannwhitneyu:', p)
        # # 效应量, https://www.psychometrica.de/effect_size.html
        # cohens_d = (df3['student_star'].mean() - df2['student_star'].mean() ) / (sqrt((df2['student_star'].std() ** 2 + df3['student_star'].std() ** 2) / 2))
        cohens_d = (df2['student_difficult'].mean() - df3['student_difficult'].mean() ) / (sqrt((df2['student_difficult'].std() ** 2 + df3['student_difficult'].std() ** 2) / 2))
        # print(i,'评分的效应量, cohens_d:', cohens_d)
        print(i,'mannwhitneyu:',p ,'课程难度效应量, cohens_d:', cohens_d)


# '''2。比较 不同教授 ，online offline  3*2 的 教授总评分'''
# # https://stats.stackexchange.com/questions/246719/friedman-test-and-post-hoc-test-for-python
# def professor_course():
#     df = pd.read_csv(file,nrows=1000, index_col=0)
#     print(df.columns)
#     df1 = df[(df['professor'] == 'assistant') & (df['IsCourseOnline'] == 0)]
#     df2 = df[(df['professor'] == 'assistant') & (df['IsCourseOnline'] == 1)]
#     print(df1)
#
#     # p = stats.friedmanchisquare(df1['star_rating'], )
#     # print('p:', p)
#
#     # g = sns.catplot(x="professor", y="star_rating", hue="IsCourseOnline", kind="bar", data=df, ci='sd',
#     #                 color='grey')
#     # plt.ylim([1, 5])
#     # plt.ylabel("professor", fontsize=12)
#     # plt.xlabel("star_rating", fontsize=12)
#     # plt.show()
# def course_level():
#     df = pd.read_csv(file, nrows=10000, index_col=0)
#     print(df.columns)
#     df = df[(df['class_order'] >= 1) & (df['class_order'] <= 4)]
#     g = sns.catplot(x="would_take_agains", y="star_rating", hue="IsCourseOnline", kind="bar", data=df, ci='sd',
#                     color='grey')
#     plt.ylim([1, 5])
#     plt.ylabel("professor", fontsize=12)
#     plt.xlabel("star_rating", fontsize=12)
#     plt.show()
#

def choose_class():
    # 根据已有数据探究“评分”与“是否选课”之间关系，并建立预测模型。
    # 是否选择课程，罗辑回归 https://blog.csdn.net/MsSpark/article/details/83964669
    from collections import OrderedDict
    import numpy as np
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings('ignore')
    # 2.创建数据（学习时间与是否通过考试）
    dataDf = pd.read_csv(file,nrows=10000,usecols=['student_star','would_take_agains'])
    dataDf  = dataDf.dropna()
    print(dataDf)
    exam_X = dataDf['student_star']
    exam_y = dataDf['would_take_agains']
    # # 绘制散点图
    # plt.scatter(exam_X, exam_y, color='b')
    # plt.legend(loc=2)
    # plt.xlabel('评分')
    # plt.ylabel('是否选课')
    # plt.show()

    # 1.拆分训练集和测试集
    import tensorflow as tf
    from sklearn.model_selection import train_test_split
    exam_X = exam_X.values.reshape(-1, 1)
    exam_y = exam_y.values.reshape(-1, 1)
    train_X, test_X, train_y, test_y = train_test_split(exam_X, exam_y, train_size=0.8)
    print('训练集数据大小为', train_X.size, train_y.size)
    print('测试集数据大小为', test_X.size, test_y.size)

    # # # 2.散点图观察
    # plt.scatter(train_X[:,0], train_y[:,0], color='b', label='train data')
    # plt.scatter(test_X[:,0], test_y[:,0], color='r',   label='test data')
    # # plt.plot(test_X,pred_y,color='r')
    # plt.legend(loc=2)
    # plt.xlabel('Hours')
    # plt.ylabel('Scores')
    # plt.show()

    from sklearn.linear_model import LogisticRegression
    modelLR = LogisticRegression()
    # 4.训练模型
    modelLR.fit(train_X[:,:], train_y[:,:])
    modelLR.score(test_X[:,:], test_y[:,:])
    # 先求出回归函数y=a+bx，再代入逻辑函数中pred_y=1/(1+np.exp(-y))
    b = modelLR.coef_
    a = modelLR.intercept_
    print('该模型对应的回归函数为:y= 1/(1+exp-(%f+%f*x))' % (a, b))

    # 画出相应的逻辑回归曲线
    plt.scatter(train_X[:,:], train_y[:,:], color='b', label='train data')
    plt.scatter(test_X[:,:], test_y[:,:], color='r', label='test data')
    plt.plot(test_X[:,:], 1 / (1 + np.exp(-(a + b * test_X[:,:]))), color='r')
    plt.plot(exam_X[:,:], 1 / (1 + np.exp(-(a + b * exam_X[:,:]))), color='y')
    plt.legend(loc=2)
    plt.xlabel('Hours')
    plt.ylabel('Scores')
    plt.show()

def setiment_analysis():
    pass
# https://blog.csdn.net/kilotwo/article/details/99418845



if __name__ == "__main__":
    df= pd.read_csv(file, usecols=['student_difficult','IsCourseOnline','subject_onlines','subject_not_onlines'])
    subject = ['Accounting', 'Arts ', 'Business', 'Chemistry', 'Computer Science', 'Economics', 'English', 'Law', 'Math', 'Physics', 'Psychology', 'Social science']
    pd.set_option('display.max_columns', None)
    df = df.groupby(['IsCourseOnline','subject_onlines','subject_not_onlines']).describe()
    print(df)
    df.to_csv('online_diff.csv')

    # # df2 = df[(df['class_order'] >= 1) & (df['class_order'] <= 4)]  # 在线课程
    # df2 = df[(df['IsCourseOnline'] == 1)]  # 在线课程
    # print(df2['comments'])
    # list = []
    # for i in df2['comments']:
    #     text = ''.join(i)
    #     list.append(text)
    # print(list)
    # df2['comments'].to_csv(r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/emotional_R.csv',index=False)
    # df2.to_csv('/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/emotional_R.csv')

    # online_offline_rating()
    # subject_analysis()




