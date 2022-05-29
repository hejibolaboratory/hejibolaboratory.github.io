# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 10:34 上午
# @Author  : mingchun liu
# @Email   : psymingchun@gmail.com
# @File    : 根据姓名判断性别及种族.py
# @Software: PyCharm
#https://ethnicolr.readthedocs.io/ethnicolr.html

import pandas as pd
import gender_guesser.detector as gender
# from ethnicolr import census_ln, pred_census_ln, pred_wiki_name, pred_fl_reg_ln

file= r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP.csv'
# df2['new_gender'] = df1['new_gender']
# print(df2)
# print(df2.head())
# df2.to_csv(r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_merge.csv', index=False)


'''性别'''
# file = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_dataset.csv'

#
# df = pd.read_csv(file,nrows=1000, index_col=0)
#
# gender_list = []
# d = gender.Detector()
# for i in df['professor_name']:
#     print(i,i.split(' ')[-1], d.get_gender(i.split(' ')[-1]))
#     gender_list.append(d.get_gender(i.split(' ')[-1]))
#
# df['gender'] =  gender_list
# print(df)
# # df.to_csv(r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP__big_data_add_gender.csv', index=False)



'''识别种族'''
# file = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_dataset.csv'
# # file = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP.csv'
# df = pd.read_csv(file, index_col=0)
#
# gives_good_feedback = []
# caring = []
# respected = []
# participation_matters =[]
# clear_grading_criteria =[]
# skip_class =[]
# amazing_lectures=[]
# inspirational=[]
# tough_grader=[]
# hilarious=[]
# get_ready_to_read=[]
# lots_of_homework=[]
# accessible_outside_class=[]
# lecture_heavy=[]
# extra_credit=[]
# graded_by_few_things=[]
# group_projects=[]
# test_heavy=[]
# so_many_papers=[]
# beware_of_pop_quizzes=[]
#
# for i in df['tag_professor']:
#     item = str(i).lower()
#     print(item)
#     if 'Gives good feedback'.lower() in item:
#         gives_good_feedback.append(1)
#     else:
#         gives_good_feedback.append(0)
#
#     if 'Caring'.lower() in item:
#         caring.append(1)
#     else:
#         caring.append(0)
#
#     if 'Respected'.lower() in item:
#         respected.append(1)
#     else:
#         respected.append(0)
#
#     if 'Participation matters'.lower() in item:
#         participation_matters.append(1)
#     else:
#         participation_matters.append(0)
#
#     if 'Clear grading criteria'.lower() in item:
#         clear_grading_criteria.append(1)
#     else:
#         clear_grading_criteria.append(0)
#
#     if 'Skip class'.lower() in item:
#         skip_class.append(1)
#     else:
#         skip_class.append(0)
#
#     if 'Amazing lectures'.lower() in item:
#         amazing_lectures.append(1)
#     else:
#         amazing_lectures.append(0)
#
#     if 'Inspirational'.lower() in item:
#         inspirational.append(1)
#     else:
#         inspirational.append(0)
#
#     if 'Tough grader'.lower() in item:
#         tough_grader.append(1)
#     else:
#         tough_grader.append(0)
#
#     if 'Get ready to read'.lower() in item:
#         get_ready_to_read.append(1)
#     else:
#         get_ready_to_read.append(0)
#
#     if 'Hilarious'.lower() in item:
#         hilarious.append(1)
#     else:
#         hilarious.append(0)
#
#     if 'Lots of homework'.lower() in item:
#         lots_of_homework.append(1)
#     else:
#         lots_of_homework.append(0)
#
#     if 'Accessible outside'.lower() in item:
#         accessible_outside_class.append(1)
#     else:
#         accessible_outside_class.append(0)
#
#     if 'Lecture heavy'.lower() in item:
#         lecture_heavy.append(1)
#     else:
#         lecture_heavy.append(0)
#
#     if 'Extra credit'.lower() in item:
#         extra_credit.append(1)
#     else:
#         extra_credit.append(0)
#
#     if 'Graded by few things'.lower() in item:
#         graded_by_few_things.append(1)
#     else:
#         graded_by_few_things.append(0)
#
#     if 'Group projects'.lower() in item:
#         group_projects.append(1)
#     else:
#         group_projects.append(0)
#
#     if 'Test heavy'.lower() in item:
#         test_heavy.append(1)
#     else:
#         test_heavy.append(0)
#
#     if 'So many papers'.lower() in item:
#         so_many_papers.append(1)
#     else:
#         so_many_papers.append(0)
#
#     if 'Beware of pop quizzes'.lower() in item:
#         beware_of_pop_quizzes.append(1)
#     else:
#         beware_of_pop_quizzes.append(0)
#
# df['gives_good_feedback'] = gives_good_feedback
# df['caring'] = caring
# df['respected'] = respected
# df['participation_matters'] = participation_matters
# df['clear_grading_criteria'] = clear_grading_criteria
# df['skip_class'] = skip_class
# df['amazing_lectures'] =amazing_lectures
# df['inspirational'] = inspirational
# df['tough_grader'] = tough_grader
# df['hilarious'] = hilarious
# df['get_ready_to_read'] = get_ready_to_read
# df['lots_of_homework'] = lots_of_homework
# df['accessible_outside_class'] = accessible_outside_class
# df['lecture_heavy'] = lecture_heavy
# df['extra_credit'] = extra_credit
# df['graded_by_few_things'] =graded_by_few_things
# df['group_projects'] = group_projects
# df['test_heavy'] = test_heavy
# df['so_many_papers'] =so_many_papers
# df['beware_of_pop_quizzes'] = beware_of_pop_quizzes
#
#
# print(df)
# df.to_csv(r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_DATASET.csv')
