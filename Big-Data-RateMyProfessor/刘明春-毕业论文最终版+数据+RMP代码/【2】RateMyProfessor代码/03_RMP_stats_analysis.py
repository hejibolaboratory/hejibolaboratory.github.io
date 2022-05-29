# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 8:54 下午
# @Author  : mingchun liu
# @Email   : psymingchun@gmail.com
# @File    : 03_RMP_stats_analysis.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from math import sqrt
import seaborn as sns
import re


# 提取tag，并计算tag个数，计算tag并封装成为dataframe
def extract_tag(df):
    new_list = []
    tag_list = []
    tag_number = []
    for i in df['tag_professor'].dropna().tolist(): #去除右括号
        pattern = re.split('\)', i.lower())
        new_list += pattern
    for i in [x.strip() for x in new_list if x != '']: #去除左括号，并保存为list
        pattern =re.split('\(', i)
        tag_list.append(pattern[0].strip().capitalize())
        tag_number.append(str(pattern[1]))

    info = {'tag':tag_list,'tag_number':tag_number}
    df = pd.DataFrame(info)
    df['tag'].value_counts().to_frame(name='tag_number')
    return df['tag'].value_counts().to_frame(name='tag_number')

'''1. 高分、低分教授tag提取、mannwhitneyu非参数检验、tag卡方检验'''
def High_low_professor_tag_analysis():
    df = pd.read_csv(src, usecols=['professor_name', 'school_name', 'department_name','star_rating', 'tag_professor'])
    high_rating_professor = df[(df['star_rating'] >= 3.5) & (df['star_rating'] <= 5.0)].drop_duplicates(['professor_name','school_name','department_name'], 'first', False) # 高分组3.5-5.0星
    low_rating_professor  = df[(df['star_rating'] <= 2.4) & (df['star_rating'] >= 1.0)].drop_duplicates(['professor_name','school_name','department_name'], 'first', False) # 低分组1.0-2.4星
    high_professor_number = high_rating_professor ['professor_name'].count()
    print('高分教授数量：', high_professor_number)
    low_professor_number = low_rating_professor ['professor_name'].count()
    print('低分教授数量：', low_professor_number)
    high_professor_tag_count = extract_tag(high_rating_professor) # 高分教授tag
    low_professor_tag_count  = extract_tag(low_rating_professor) # 低分教授tag
    high_professor_tag_count.to_csv('1-高分教授tag.csv')
    low_professor_tag_count.to_csv('2-低分教授tag.csv')

def high_low_mannwhitneyu():
    # 独立样本T检验的替代方法，检测两组
    df = pd.read_csv(src, usecols=['professor_name', 'school_name', 'department_name', 'star_rating', 'tag_professor'])
    df2 = df[(df['star_rating'] >= 3.5) & (df['star_rating'] <= 5.0)].drop_duplicates(['professor_name','school_name','department_name'], 'first', False)  # 高分组3.5-5.0星
    df3 = df[(df['star_rating'] <= 2.4) & (df['star_rating'] >= 1.0)].drop_duplicates(['professor_name','school_name','department_name'], 'first', False)  # 低分组1.0-2.4星

    yes_num = df2['star_rating'].count()  # 个数
    yes_mean = df2['star_rating'].mean()  # 平均数
    yes_std = df2['star_rating'].std()  # 标准差
    print('high教授个数',yes_num,'平均数：', yes_mean,'标准差：',yes_std)
    no_num = df3['star_rating'].count()  # 个数
    no_mean = df3['star_rating'].mean()  # 平均数
    no_std = df3['star_rating'].std()  # 标准差
    print('low教授个数', no_num, '平均数：', no_mean, '标准差：', no_std)

    # 非参数检验
    p = stats.mannwhitneyu(df2['star_rating'], df3['star_rating'], alternative='two-sided')
    print('mannwhitneyu', p)
    # 效应量, https://www.psychometrica.de/effect_size.html
    cohens_d = (yes_mean - no_mean) / (sqrt((yes_std ** 2 + no_std ** 2) / 2))
    print('cohens_d:', cohens_d)

def chisquare(): # 610152	110092
    df = pd.read_excel('高分+低分教授.xlsx',usecols='A:C')
    print(df)
    a = df['high_professor_tag'].tolist() # 平衡后的 比率 = tag个数/教授个数
    b = df['low_professor_tag'].tolist()
    cohen_w=[]
    for i in range(len(a)):
        # goodness of fit https://stackoverflow.com/questions/51894150/python-chi-square-goodness-of-fit-test-to-get-the-best-distribution
        obs = []
        obs.append(a[i])
        obs.append(b[i])
        # obs = [181556, 7786]
        exp = [610152, 110092]
        chi_chisquare = stats.chisquare(obs, exp)
        print('统计值：%s，P值：%s' % chi_chisquare)
        #计算效应量  科恩 w
        import numpy
        cohen_w.append(numpy.sqrt(chi_chisquare[0]/ (610152+110092)))
    print(cohen_w)

'''2. 三类教授教授tag提取、kruskal非参数检验、tag卡方检验'''
def professor_tenure_tag_analysis():
    df = pd.read_csv(src, usecols=['professor_name', 'school_name', 'department_name', 'year_since_first_review','star_rating', 'tag_professor']).drop_duplicates(['professor_name','school_name','department_name'], 'first', False)
    pd.set_option('display.max_rows', 100, 'display.max_columns', 1000, "display.max_colwidth", 1000, 'display.width',1000)
    assistant_professor = df[(df['year_since_first_review'] >= 0) & (df['year_since_first_review'] <= 6.0)]
    associate_professor  = df[(df['year_since_first_review'] <= 12.0) & (df['year_since_first_review'] > 6.0)]
    full_professor  = df[(df['year_since_first_review'] > 12.0) & (df['year_since_first_review'] <= 20.0)]

    #助理教授
    print('assistant_professor:')
    print(assistant_professor.describe())
    print(assistant_professor['professor_name'].count())
    assistant_professor_tag_count = extract_tag(assistant_professor)
    #副教授
    print('associate_professor:')
    print(associate_professor.describe())
    print(associate_professor['professor_name'].count())
    associate_professor_tag_count = extract_tag(associate_professor)
    #教授
    print('full_professor个数')
    print(full_professor.describe())
    print(full_professor['professor_name'].count())
    full_professor_tag_count = extract_tag(full_professor)

    #非参数检验
    # https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.kruskal.html
    h_test = stats.kruskal(assistant_professor['star_rating'],associate_professor['star_rating'],full_professor['star_rating'])
    h, p = h_test
    print('Kruskal-Wallis H', h_test)
    print('p',p)

    # 事后检验,https://github.com/maximtrp/scikit-posthocs
    assistant_professor['professor'] = 'assistant_professor'
    associate_professor['professor']   = 'associate_professor'
    full_professor['professor']   = 'full_professor'

    df = assistant_professor.append(associate_professor).append(full_professor)
    import scikit_posthocs as sp
    post_hoc = sp.posthoc_conover(df, val_col='star_rating', group_col='professor', p_adjust='holm')
    print(post_hoc)

    assistant_professor_tag_count.to_csv('4-助理教授.csv')
    associate_professor_tag_count.to_csv('4-副教授.csv')
    full_professor_tag_count.to_csv('4-教授.csv')

def tenure_chi_chisquare(): # 609863	260859	50373
    df = pd.read_excel('助理教授副教授教授.xlsx',usecols='A:D')
    As = df['assassistant professor'].tolist()
    Ao = df['associate professor'].tolist()
    Full = df['full professor'].tolist()
    print(df)
    cohen_w=[]
    for i in range(len(As)):
        # goodness of fit https://stackoverflow.com/questions/51894150/python-chi-square-goodness-of-fit-test-to-get-the-best-distribution
        obs = []
        obs.append(As[i])
        obs.append(Ao[i])
        obs.append(Full[i])

        # obs = [181556, 7786]
        exp = [609193, 26084, 50261]
        chi_chisquare = stats.chisquare(obs, exp)
        print('统计值：%s，P值：%s' % chi_chisquare)
        #计算效应量  科恩 w
        import numpy
        cohen_w.append(numpy.sqrt(chi_chisquare[0]/ (609193 + 26084 + 50261)))
    print(cohen_w)

def three_professor_kruskal_effsize(): # 计算三组教授  H test 的效应量
    # https://rpkgs.datanovia.com/rstatix/reference/kruskal_effsize.html
    eta = (2570.4373908398707 - 3 + 1) / (919738- 3)
    print(eta)

'''3。计算 【评分】 和 【课程难度】的相关及可视化'''
def rating_difficulty_correlation():
    df = pd.read_csv(src, nrows=100000, usecols=['professor_name','school_name', 'department_name','star_rating', 'diff_index'])
    df = df[(df['star_rating'] >= 1.0) & (df['diff_index'] >= 1.0)].drop_duplicates(['professor_name','school_name','department_name',], 'first', False)
    print(df.describe()) #计算平均数，标准差

    # 计算评分和难度的回归方程
    data = df[['diff_index', 'star_rating']]
    # regression = stats.linregress(data)
    # print("R square：", regression[2] ** 2)
    # print('线性回归方程是 Y= %.3fX + %.3f,rvalue是%.3f,p-values是%s,标准误是%s' % regression)
    #
    g = sns.set("paper", font_scale =1.3)
    g = sns.set_style("white", {"xtick.major.size": 4, "ytick.major.size": 4})
    data = data.rename(index=str, columns={'diff_index': 'Difficulty Index', 'star_rating': 'Star Rating'})
    g = sns.jointplot(x = 'Difficulty Index', y = 'Star Rating', data=data,height=16, ratio=10, kind="kde",  cbar= True,cbar_kws = dict(use_gridspec=False,location="right"), xlim=(1,5), ylim=(1.0, 5.0),space=0,color='b')
    g.ax_joint.legend_.remove()  # 去除相关和P值
    g = sns.regplot(data['Difficulty Index'], data['Star Rating'], scatter=False, ax=g.ax_joint)


    plt.text(-20.8, 1.5, r"Y=-0.50X+5.18", fontsize=10)
    plt.text(-20.8, 1.2, r'$R^2$=0.20', fontsize=10)
    plt.show()
    # plt.draw()
    # plt.savefig('rating_take_again_correlation.png', dpi=300)


'''4。计算 [评分] 和 [是否再次选课] 的关系, 可视化'''
def rating_take_again_correlation():
    df = pd.read_csv(src, nrows=10000, usecols=['professor_name', 'school_name','department_name','star_rating', 'diff_index','take_again'])
    df = df[(df['star_rating'] >= 1.0) & (df['diff_index'] >= 1.0)].drop_duplicates(['professor_name','school_name','department_name',], 'first', False)
    # df = df.replace(r'<span class="would-take-again">Would Take Again: <span class="response">N/A</span></span>\\r\\n                <span class="would-take-again">Would Take Again: <span class="response">N/A</span></span>\\r\\n                <span class="would-take-again">Would Take Again: <span class="response">N/A</span></span>\\r\\n                ',np.nan,regex=True)
    df['professor_take_again'] = df['take_again'].str.strip('%').astype(float) / 100  # 百分数转化成小数
    df = df.dropna()
    print(df.describe())  # 计算平均数，标准差
    print(df.head())

    # 计算回归方程
    regression = stats.linregress(df[['star_rating','professor_take_again']])
    print("R square", regression[2] ** 2)
    # R_square = regression2[2] ** 2
    print('线性回归方程是 Y= %.3fX + %.3f,rvalue是%.3f,pvalus是%s,标准误是%s' % regression)

    # plt.rcParams['font.family'] = 'Adobe Fangsong Std'  # 中文
    g = sns.set("paper", font_scale=1.3)
    g = sns.set_style("white")
    # g = sns.set_style("white",{"xtick.major.size": 4, "ytick.major.size": 4})

    # 核密度图
    data = df.rename(index=str, columns={'professor_take_again': 'Would Take Again', 'star_rating': 'Star Rating'})
    g = sns.jointplot(x = 'Star Rating',y = 'Would Take Again', data=data, height=6, ratio=7, kind="kde", xlim=(1.0, 5.0),
                      ylim=(0.0, 1.0), space=0, palette= 'Blues',cbar= True,cbar_kws = dict(use_gridspec=False,location="right"))
    g.ax_joint.legend_.remove()# 去除相关和P值
    g = sns.regplot(data['Star Rating'], data['Would Take Again'], scatter=False, ax=g.ax_joint)

    plt.text(-14.2, 0.2, r"Y=0.26X-0.30", fontsize=12)
    plt.text(-14.2, 0.1, r'$R^2$=0.64', fontsize=12)

    plt.show()
    # plt.draw()
    # plt.savefig('rating_take_again_correlation.png', dpi=300)


'''5.不同教授给学生评分 显示百分比'''
def professor_student_grade():
    df = pd.read_csv(src)
    df = df.rename(index=str, columns={'grades': 'Student Grade', 'student_star': 'Star Rating'})
    ncount = df['Student Grade'].value_counts().sum()
    print('成绩总个数：',ncount)

    fig, ax1 = plt.subplots(figsize=(18, 8), ) #dpi=300
    fig.set_figwidth(10)
    fig.set_figheight(8)
    # 教授对学生的评分
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'WD', 'INC','Not', 'Audit/No','P']
    graph = sns.countplot(ax=ax1, x='Student Grade', data=df, palette=sns.color_palette('Blues'),order=grades)

    graph.set_xticklabels(graph.get_xticklabels())
    for p in graph.patches: # 显示柱状图个数
        # print(p)
        height = p.get_height()
        # print(height)
        graph.text(p.get_x() + p.get_width() / 2., height + 20, height, ha="center", fontsize=12) #rotation=40

        x = p.get_bbox().get_points()[:, 0]
        y = p.get_bbox().get_points()[1, 1]
        ax1.annotate('({:.2f}%)'.format(100. * y / ncount), (x.mean(), y),ha='center', va='top', fontsize=10)  # set the alignment of the text


    ax1.set_ylabel("The Number of Students Reciving Grade", fontsize=12)
    ax1.set_xlabel("Student Grade", fontsize=12)


    plt.ylim([0, 700000])
    g = sns.despine(right=True, top=True)  # 去除顶部及右边的线
    plt.rcParams['font.family'] = 'sans-serif'
    # plt.legend(loc='upper right')
    plt.show()
    # plt.draw()
    # plt.savefig('professor_student_grade.png', dpi=300)


'''6. 是否强制与学生给教授评分的关系'''
def violinplot_rating_mandatory():
    df = pd.read_csv(src)
    df = df.rename(index=str, columns={'for_credits':'For Credit','student_star': 'Star Rating Given by Students', "attence":"Attendance"})
    print(df.head())
    fig = plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # plt.setp(g.artists, edgecolor='w')
    # plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.family'] = 'calibri'
    plt.subplots_adjust(wspace=0.4)

    ax1 = plt.subplot(1, 2, 2)
    ax1.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="For Credit", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["For Credit", "Star Rating Given by Students"]], palette=sns.color_palette('Blues'))
    ax1.set_xlabel("For Credit", fontsize=14)
    ax1.set_ylabel("Star Rating Given by Students", fontsize=14)

    ax2 = plt.subplot(1, 2, 1)
    ax2.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Attendance", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["Attendance", "Star Rating Given by Students"]],palette=sns.color_palette('Blues'))
    ax2.set_xlabel("Attendance", fontsize=14)
    ax2.set_ylabel("Star Rating Given by Students", fontsize=14)

    fig.tight_layout()
    # plt.show()
    plt.draw()
    plt.savefig('violinplot_rating_mandator.png', dpi=300)


'''7.是否为了分数 与 学生对老师的评分'''
def violinplot_rating_greades():
    df = pd.read_csv(src)
    df = df.rename(index=str, columns={'for_credits': 'For Credits', 'student_star': 'Star Rating Given by Students', "attence":"Attendance", 'grades':'Student Grade'})
    print(df['Student Grade'].count()) # 1438024
    print(df['Student Grade'].value_counts()) # 每个分数的个数

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
    g = sns.violinplot( x="Student Grade", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['A+', 'A', 'A-'],
                       palette=sns.color_palette('Blues'))
    ax1.set_xlabel("Student Grade", fontsize=14)
    ax1.set_ylabel("Star Rating Given by Students", fontsize=14)

    ax2=plt.subplot(2, 3, 2)
    ax2.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['B+', 'B', 'B-'],
                       palette=sns.color_palette('Blues'))
    ax2.set_xlabel("Student Grade", fontsize=14)
    ax2.set_ylabel("Star Rating Given by Students", fontsize=14)

    ax3 = plt.subplot(2, 3, 3)
    ax3.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['C+', 'C', 'C-'],
                       palette=sns.color_palette('Blues'))
    ax3.set_xlabel("Student Grade", fontsize=14)
    ax3.set_ylabel("Star Rating Given by Students", fontsize=14)

    ax4 = plt.subplot(2, 3, 4)
    ax4.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['D+', 'D', 'D-'],
                       palette=sns.color_palette('Blues'))
    ax4.set_xlabel("Student Grade", fontsize=14)
    ax4.set_ylabel("Star Rating Given by Students", fontsize=14)

    ax5 = plt.subplot(2, 3, 5)
    ax5.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]],
                       order=['F', 'WD', 'INC'],
                       palette=sns.color_palette('Blues'))
    ax5.set_xticklabels(['F','Drop/Withdrawal', 'Incomplete'])
    ax5.set_xlabel("Student Grade", fontsize=14)
    ax5.set_ylabel("Star Rating Given by Students", fontsize=14)

    ax6 = plt.subplot(2, 3, 6)
    ax6.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0.5, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['Not', 'Audit/No'],
                       palette=sns.color_palette('Blues'))
    ax6.set_xticklabels(['Not sure yet','Audit/No Grade'])
    ax6.set_xlabel("Student Grade", fontsize=14)
    ax6.set_ylabel("Star Rating Given by Students", fontsize=14)

    fig.tight_layout()
    # plt.show()
    plt.draw()
    plt.savefig('violinplot_rating_greades.png', dpi=300)

'''8. Would Take Again和Grades Received 的图。这是reciprocity的 '''
def would_take_agein_grade(): # 结合excel 作图
    df = pd.read_csv(src,nrows=10000)
    fig, ax1 = plt.subplots(figsize=(10, 8))
    fig.set_figwidth(10)
    fig.set_figheight(8)
    df2 = df.rename(index=str, columns={'grades': 'Student Grade', 'would_take_agains': 'would take again'})
    order=['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'WD', 'INC',
                                 'Not', 'Audit/No','P']
    graph = sns.countplot(ax=ax1, x='Student Grade',hue='would take again', data=df2, palette=sns.color_palette('Blues'),
                          order=order)
    graph.set_xticklabels(graph.get_xticklabels())
    for p in graph.patches:
        height = p.get_height()
        graph.text(p.get_x() + p.get_width() / 2., height + 0.3, height, ha="center", fontsize=8, rotation=40)
    plt.show()

# 是否为了分数, 强制进行非参数检验
def Mandatory_mannwhitneyu():
    from math import sqrt
    df = pd.read_csv(src, usecols=['student_star', 'for_credits','attence'])
    print('manteniU检验，是不是强制～～～～～～～～～～')
    # 检验是否强制
    df2 = df[(df['attence'] == 'Mandatory') & (df['student_star'] >= 1.0)]  #  强制组
    df3 = df[(df['attence'] == 'Not Mandatory') & (df['student_star'] >= 1.0)]  # 非强制组
    p = stats.mannwhitneyu(df2['student_star'],df3['student_star'],alternative='two-sided')
    print('是否强制mannwhitneyu:',p)
    yes_num = df2['student_star'].count()  # 个数
    yes_mean = df2['student_star'].mean()  # 平均数
    yes_std = df2['student_star'].std()  # 标准差
    print('强制组学生个数',yes_num,'平均数：', yes_mean,'标准差：',yes_std)
    no_num = df3['student_star'].count()  # 个数
    no_mean = df3['student_star'].mean()  # 平均数
    no_std = df3['student_star'].std()  # 标准差
    print('非强制组学生个数',no_num,'平均数：', no_mean,'标准差：',no_std)
    #test conditions
    cohens_d = (yes_mean - no_mean) / (sqrt((yes_std ** 2 + no_std ** 2) / 2))
    print('cohens_d:',cohens_d)

def for_crdeit_mannwhitneyu():
    from math import sqrt
    df = pd.read_csv(src, usecols=['student_star', 'for_credits', 'attence'])
    print(df['for_credits'])
    print('manteniU检验，是不是为了学分～～～～～～～～～～')
    for_credit = df[(df['for_credits'] == 'Yes') & (df['student_star'] >= 1.0)]  # 为了学分组
    not_for_credit = df[(df['for_credits'] == 'No') & (df['student_star'] >= 1.0)]  # 不是为了学分组
    p2 = stats.mannwhitneyu(for_credit['student_star'], not_for_credit['student_star'], alternative='two-sided')
    print('是否为了学分mannwhitneyu:', p2)
    for_credit_num = for_credit['student_star'].count()  # 个数
    for_credit_mean = for_credit['student_star'].mean()  # 平均数
    for_credit_std = for_credit['student_star'].std()  # 标准差
    print('为了学分学生个数', for_credit_num, '平均数：', for_credit_mean, '标准差：', for_credit_std)
    not_for_credit_num = not_for_credit['student_star'].count()  # 个数
    not_for_credit_mean = not_for_credit['student_star'].mean()  # 平均数
    not_for_credit_std = not_for_credit['student_star'].std()  # 标准差
    print('不是为了学分学生个数', not_for_credit_num, '平均数：', not_for_credit_mean, '标准差：', not_for_credit_std)
    # test conditions
    cohens_d2 = (for_credit_mean - not_for_credit_mean) / (sqrt((for_credit_std ** 2 + not_for_credit_std ** 2) / 2))
    print('cohens_d:', cohens_d2)



# 学生分数检验，自变量学生分数，因变量学生给教授的分数，需要事后检验
def student_grade_describe():
    df = pd.read_csv(src,  usecols=['student_star', 'grades'])
    df2 = df.groupby('grades').student_star.mean()
    df3 = df.groupby('grades').student_star.std()
    df4 = df.groupby('grades').student_star.count()
    print(df2)
    print(df3)
    print(df4)


def student_grade_test():
    df = pd.read_csv(src,  usecols=['student_star', 'grades'])
    # df = df.dropna(axis=0)
    student_grade =['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'WD', 'INC', 'Not','Audit/No']

    df_A = df[(df['grades'] == 'A+') & (df['student_star'] >= 1.0)]
    df_A2 = df[(df['grades'] == 'A') & (df['student_star'] >= 1.0)]
    df_A3 = df[(df['grades'] == 'A-') & (df['student_star'] >= 1.0)]

    df_B = df[(df['grades'] == 'B+') & (df['student_star'] >= 1.0)]
    df_B2 = df[(df['grades'] == 'B') & (df['student_star'] >= 1.0)]
    df_B3 = df[(df['grades'] == 'B-') & (df['student_star'] >= 1.0)]

    df_C = df[(df['grades'] == 'C+') & (df['student_star'] >= 1.0)]
    df_C2 = df[(df['grades'] == 'C') & (df['student_star'] >= 1.0)]
    df_C3 = df[(df['grades'] == 'C-') & (df['student_star'] >= 1.0)]

    df_D = df[(df['grades'] == 'D+') & (df['student_star'] >= 1.0)]
    df_D2 = df[(df['grades'] == 'D') & (df['student_star'] >= 1.0)]
    df_D3 = df[(df['grades'] == 'D-') & (df['student_star'] >= 1.0)]

    df_F = df[(df['grades'] == 'F') & (df['student_star'] >= 1.0)]
    df_WD = df[(df['grades'] == 'WD') & (df['student_star'] >= 1.0)]
    df_INC = df[(df['grades'] == 'INC') & (df['student_star'] >= 1.0)]
    df_Not = df[(df['grades'] == 'Not') & (df['student_star'] >= 1.0)]
    df_Audit = df[(df['grades'] == 'Audit/No') & (df['student_star'] >= 1.0)]
    # df_P = df[(df['grades'] == 'P') & (df['student_star'] >= 1.0)]

    h_test = stats.kruskal(df_A['student_star'] ,df_A2['student_star'], df_A3['student_star'],
                                    df_B['student_star'], df_B2['student_star'], df_B3['student_star'],
                                    df_C['student_star'], df_C2['student_star'], df_C3['student_star'],
                                    df_D['student_star'], df_D2['student_star'], df_D3['student_star'],
                                    df_F['student_star'], df_WD['student_star'], df_INC['student_star'],
                                    df_Not['student_star'], df_Audit['student_star'])
    print('Kruskal-Wallis H',h_test)

    df2 = df_A.append(df_A2).append(df_A3).append(df_B).append(df_B2).append(df_B3).append(df_C).append(df_C2).append(df_C3).append(df_D).append(df_D2).append(df_D3).append(df_F).append(df_WD).append(df_INC).append(df_Not).append(df_Audit)
    print(df2.describe())
    # import scikit_posthocs as sp
    # post_hoc = sp.posthoc_conover(df2, val_col='student_star', group_col='grades', p_adjust='holm')
    # # print('事后检验')
    # # print(post_hoc)
    # # post_hoc.to_csv('事后检验.csv')

def kruskal_effsize(): # 计算成绩的 H test 的效应量
    # Kruskal-Wallis H 384846.4308588387, pvalue=0.0)
    # https://rpkgs.datanovia.com/rstatix/reference/kruskal_effsize.html
    eta = (384846.4308588387 - 17 + 1) / (1951433 - 17)
    print(eta)

################## 成绩分析 结束  ######################
################### 评论分析 开始 ##########
def word_mannwhitneyu():
    # 独立样本T检验的替代方法，检测两组
    df = pd.read_csv(src)
    df2 = df[(df['star_rating'] >= 3.5) & (df['star_rating'] <= 5.0)]  # 高分组3.5-5.0星
    df3 = df[(df['star_rating'] <= 2.4) & (df['star_rating'] >= 1.0)]  # 低分组1.0-2.4星

    yes_num = df2['word_comment'].count()  # 个数
    yes_mean = df2['word_comment'].mean()  # 平均数
    yes_std = df2['word_comment'].std()  # 标准差
    print('高分教授学生个数',yes_num,'平均数：', yes_mean,'标准差：',yes_std)
    no_num = df3['word_comment'].count()  # 个数
    no_mean = df3['word_comment'].mean()  # 平均数
    no_std = df3['word_comment'].std()  # 标准差
    print('低分教授学生个数', no_num, '平均数：', no_mean, '标准差：', no_std)

    # 非参数检验
    p = stats.mannwhitneyu(df2['star_rating'], df3['star_rating'], alternative='two-sided')
    print('mannwhitneyu', p)
    # 效应量, https://www.psychometrica.de/effect_size.html
    cohens_d = (no_mean - yes_mean) / (sqrt((yes_std ** 2 + no_std ** 2) / 2))
    print('cohens_d:', cohens_d) # conen 为负说明，https://trendingsideways.com/the-cohens-d-formula

################### 评论分析 结束 ##########
if __name__ == '__main__':
    src = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP.csv'

    # High_low_professor_tag_analysis() #高分低分教授tag输出

    # professor_tenure_tag_analysis()  # 三类教授tag分析
    # tenure_chi_chisquare() # 三类教授tag卡方检验
    # three_professor_kruskal_effsize() # 计算三组教授  H test 的效应量

    # rating_difficulty_correlation()
    rating_take_again_correlation()

    # High_low_professor_tag_analysis()
    # professor_tenure_tag_analysis()
    # three_professor_kruskal_effsize() # 计算三组教授  H test 的效应量

    # student_grade_test()
    # kruskal_effsize()
    # violinplot_rating_greades()  # 是否为了分数 与 学生对老师的评分
    # violinplot_rating_mandatory() # 是否强制与学生给教授评分的关系

