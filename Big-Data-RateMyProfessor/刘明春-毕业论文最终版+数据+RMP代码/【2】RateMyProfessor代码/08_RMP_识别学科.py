#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 23:48
# @File    : 识别学科.py
# @Software: PyCharm
# @Author  : liumingchun
# @Email   : liumingchun18@163.com
# @Website : www.zhiwiki.com


import pandas as pd
import re

file = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP.csv'
df = pd.read_csv(file,index_col=0)
print('1')
# print(df)
# name_onlines	name_not_onlines
subject_onlines = []
subject_not_onlines = []
onlines_course_level =[]
not_onlines_course_level=[]

#@ 识别学科，线上课程
for i in df['name_onlines']:
    if 'AEM' in str(i):
        subject_onlines.append('Engineering')
    elif 'PHY' in str(i):
        subject_onlines.append('Physics')
    elif 'CHEM' in str(i):
        subject_onlines.append('Chemistry')
    elif 'MATH' in str(i):
        subject_onlines.append('Math')
    elif 'CS' in str(i):
        subject_onlines.append('Computer Science')
    elif 'ACCT' in str(i):
        subject_onlines.append('Accounting')
    elif 'BUS' in str(i):
        subject_onlines.append('Business')
    elif 'ECON' in str(i):
        subject_onlines.append('Economics')
    elif 'SOC' in str(i):
        subject_onlines.append('Social science')
    elif 'PSY' in str(i):
        subject_onlines.append('Psychology')
    elif 'ART' in str(i):
        subject_onlines.append('Arts ')
    elif 'ENG' in str(i):
        subject_onlines.append('English')
    elif 'AEM' in str(i):
        subject_onlines.append('Engineering')
    elif 'LAW' in str(i):
        subject_onlines.append('Law')
    elif 'PHGY' in str(i):
        subject_onlines.append('Medicine')
    else:
        subject_onlines.append('NAN')

#  识别学科，线下课程
for i in df['name_not_onlines']:
    if 'AEM' in str(i):
        subject_not_onlines.append('Engineering')
    elif 'PHY' in str(i):
        subject_not_onlines.append('Physics')
    elif 'CHEM' in str(i):
        subject_not_onlines.append('Chemistry')
    elif 'MATH' in str(i):
        subject_not_onlines.append('Math')
    elif 'CS' in str(i):
        subject_not_onlines.append('Computer Science')
    elif 'ACCT' in str(i):
        subject_not_onlines.append('Accounting')
    elif 'BUS' in str(i):
        subject_not_onlines.append('Business')
    elif 'ECON' in str(i):
        subject_not_onlines.append('Economics')
    elif 'SOC' in str(i):
        subject_not_onlines.append('Social science')
    elif 'PSY' in str(i):
        subject_not_onlines.append('Psychology')
    elif 'ART' in str(i):
        subject_not_onlines.append('Arts ')
    elif 'ENG' in str(i):
        subject_not_onlines.append('English')
    elif 'AEM' in str(i):
        subject_not_onlines.append('Engineering')
    elif 'LAW' in str(i):
        subject_not_onlines.append('Law')
    elif 'PHGY' in str(i):
        subject_not_onlines.append('Medicine')
    else:
        subject_not_onlines.append('NAN')
# 课程难度
for i in df['name_onlines']:
    number = re.findall('\d+', str(i))
    if number:
       onlines_course_level.append(number[0])
    else:
        onlines_course_level.append(0)
for i in df['name_not_onlines']:
    number = re.findall('\d+', str(i))
    if number:
       not_onlines_course_level.append(number[0])
    else:
        not_onlines_course_level.append(0)

# print(subject_onlines)
# print(len(subject_onlines))
# print(subject_not_onlines)
# print(len(subject_not_onlines))
#
# print(onlines_course_level)
# print(len(onlines_course_level))
# print(not_onlines_course_level)
# print(len(not_onlines_course_level))

df['subject_onlines'] = subject_onlines
df['subject_onlines_level'] = onlines_course_level
df['subject_not_onlines'] = subject_not_onlines
df['subject_not_onlines_level'] = not_onlines_course_level
print(df.columns)

df.to_csv('/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_final_data.csv',index=False)
