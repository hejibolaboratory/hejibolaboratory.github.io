# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 10:44 PM
# @Author  : mingchun liu
# @Email   : psymingchun@gmail.com
# @File    : 中文论文图标可视化.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 上午11:45
# @Author  : mingchun liu
# @Email   : psymingchun@gmail.com
# @File    : 时间序列分析.py
# @Software: PyCharm
# @Resource: 设置数字标签 https://www.jianshu.com/p/5ae17ace7984
# @Resource: dpi和图片大小关系 https://stackoverflow.com/questions/47633546/relationship-between-dpi-and-figure-size

import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import sem
from matplotlib import rcParams
import seaborn as sns
from matplotlib.font_manager import FontProperties
myfont = FontProperties(fname=r'/Library/Fonts/AdobeFangsongStd-Regular.otf', size = 12)



def professor_rating_year_trend(src):
    df = pd.read_csv(src, usecols=['professor_name', 'school_name', 'department_name', 'year_since_first_review', 'star_rating'])
    df = df.drop_duplicates(['professor_name','school_name'], 'first', False)
    # 计算平均数，标准差，置信区间
    df_mean = df.groupby('year_since_first_review').star_rating.mean()
    df_se = df.groupby('year_since_first_review').star_rating.apply(sem).mul(1.96)
    count = df.groupby('year_since_first_review').professor_name.count()

    x = df_mean.index.astype(int)
    sum = count.astype(int)
    print(count.astype(int))

    # Plot
    fig, ax1 = plt.subplots(figsize = (10, 8))
    # plt.rcParams['font.family'] = 'Songti SC'
    plt.rcParams['font.family'] = ['Adobe Fangsong Std', 'sans-serif']

    fig.set_figwidth(10)
    fig.set_figheight(8)
    ax1.set_xlim([0, 19])

    ax1.set_ylabel("教授综合得分", fontproperties=myfont,size=20)
    ax1.plot(list(x), list(df_mean), color="black", lw=1)
    ax1.fill_between(x, df_mean - df_se, df_mean + df_se, color="#71c9de",lw=5) #显示标准区间
    plt.xlabel("教授教龄", fontsize=20, fontproperties=myfont,size=20)

    s, e = plt.gca().get_xlim()
    plt.xlim(s, e)
    plt.axvline(6)  # 助理教授，参考线
    plt.axvline(12) # 副教授， 参考线
    # Draw Horizontal Tick lines
    for y in range(3, 5, 1):
        plt.hlines(y, xmin=s, xmax=e, colors='black', alpha=0.3, linestyles="--", lw=2)

    ax1.text(2, 1.5, r"助理教授", fontsize=20)
    ax1.text(8, 1.5, r'副教授', fontsize=20)
    ax1.text(15,1.5, r'教授', fontsize=20)
    ax1.set_ylim([1, 5])

    # # 直方图，显示教授人数
    ax2 = ax1.twinx()
    plt.ylabel('教授数量', fontsize=20)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    plt.xticks(x[::2], [str(d) for d in x[::2]] , fontsize=20)
    # plt.title("Number of Professor by Teaching", fontsize=12)
    # plt.xlabel("教龄", fontsize=12)
    for a,b in zip(x,sum):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=14)

    ax2.set_ylim([1, 180000])
    ax1.set_xlim([0, 19])
    ax2.plot(list(x), list(sum), color="tomato") # 教授人数的变化趋势，代替柱状图

    fig.tight_layout()

    plt.show()
    # plt.draw()
    # plt.savefig('教师评分趋势.png',dpi=300)


'''7.是否为了分数 与 学生对老师的评分'''
def violinplot_rating_greades():
    df = pd.read_csv(src)
    df = df.rename(index=str, columns={'for_credits': 'For Credits', 'student_star': 'Star Rating Given by Students', "attence":"Attendance", 'grades':'Student Grade'})
    print(df['Student Grade'].count()) # 1438024
    print(df['Student Grade'].value_counts()) # 每个分数的个数

    fig = plt.figure(figsize=(16, 8))
    # plt.setp(g.artists, edgecolor='w')
    # plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.family'] = ['Adobe Fangsong Std', 'sans-serif']

    # plt.ylabel("每个学生给予教授的评分", fontsize=12)
    # plt.xlabel("学生成绩", fontsize=12)
    # g = sns.despine(right=True, top=True)  # 去除顶部及右边的线
    plt.subplots_adjust(wspace=0.4)
    # plt.subplots(figsize=(5, 5))

    ax1 = plt.subplot(2, 3, 1)
    ax1.set_ylim([1.0, 5.0])
    g = sns.violinplot( x="Student Grade", y="Star Rating Given by Students", linewidth=0, width=1,heigth=1,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['A+', 'A', 'A-'],
                       color = '#71c9de')
    ax1.set_xlabel("学生成绩", fontsize=20)
    ax1.set_ylabel("教授综合得分", fontsize=20)

    ax2=plt.subplot(2, 3, 2)
    ax2.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['B+', 'B', 'B-'],
                       color = '#71c9de')
    ax2.set_xlabel("学生成绩", fontsize=20)
    ax2.set_ylabel("教授综合得分", fontsize=20)

    ax3 = plt.subplot(2, 3, 3)
    ax3.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['C+', 'C', 'C-'],
                       color = '#71c9de')
    ax3.set_xlabel("学生成绩", fontsize=20)
    ax3.set_ylabel("教授综合得分", fontsize=20)

    ax4 = plt.subplot(2, 3, 4)
    ax4.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['D+', 'D', 'D-'],
                       color = '#71c9de')
    ax4.set_xlabel("学生成绩", fontsize=20)
    ax4.set_ylabel("教授综合得分", fontsize=20)

    ax5 = plt.subplot(2, 3, 5)
    ax5.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]],
                       order=['F', 'WD', 'INC'],
                       color = '#71c9de')
    ax5.set_xticklabels(['F','Drop/Withdrawal', 'Incomplete'])
    ax5.set_xlabel("学生成绩", fontsize=20)
    ax5.set_ylabel("教授综合得分", fontsize=20)

    ax6 = plt.subplot(2, 3, 6)
    ax6.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Student Grade", y="Star Rating Given by Students", linewidth=0, width=0.8,
                       data=df[["Student Grade", "Star Rating Given by Students"]], order=['Not', 'Audit/No'],
                       color = '#71c9de')
    ax6.set_xticklabels(['Not sure yet','Audit/No Grade'])
    ax6.set_xlabel("学生成绩", fontsize=20)
    ax6.set_ylabel("教授综合得分", fontsize=20)

    fig.tight_layout()
    plt.show()
    # plt.draw()
    # plt.savefig('violinplot学生成绩.png', dpi=300)

'''6. 是否强制与学生给教授评分的关系'''
def violinplot_rating_mandatory():
    df = pd.read_csv(src)
    df = df.rename(index=str, columns={'for_credits':'For Credit','student_star': 'Star Rating Given by Students', "attence":"Attendance"})
    print(df.head())
    fig = plt.figure(figsize=(12, 6))
    ax = plt.gca()
    # plt.setp(g.artists, edgecolor='w')
    # plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.family'] = ['Adobe Fangsong Std', 'sans-serif']
    plt.subplots_adjust(wspace=0.4)
    # sns.set(font_scale=2)
    ax1 = plt.subplot(1, 2, 2)
    ax1.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="For Credit", y="Star Rating Given by Students", linewidth=0, width=0.8,
                       data=df[["For Credit", "Star Rating Given by Students"]], color = '#71c9de')
    ax1.set_xlabel("为了学分", fontsize=20)
    ax1.set_ylabel("教授综合得分", fontsize=20)

    ax2 = plt.subplot(1, 2, 1)
    ax2.set_ylim([1.0, 5.0])
    g = sns.violinplot(x="Attendance", y="Star Rating Given by Students", linewidth=0, width=0.8,
                       data=df[["Attendance", "Star Rating Given by Students"]],color = '#71c9de')
    ax2.set_xlabel("强制出勤", fontsize=20)
    ax2.set_ylabel("教授综合得分", fontsize=20)

    fig.tight_layout()
    plt.show()
    # plt.draw()
    # plt.savefig('violinplot为了学分.png', dpi=300)

'''教授综合得分 和  课程难度的关系 '''
def rating_difficulty_correlation():
    df = pd.read_csv(src, usecols=['professor_name','school_name', 'department_name','star_rating', 'diff_index'])
    data = df[(df['star_rating'] >= 1.0) & (df['diff_index'] >= 1.0)].drop_duplicates(['professor_name','school_name','department_name',], 'first', False)
    print(data.describe()) #计算平均数，标准差
    # g = sns.set("paper", font_scale =1.3)
    # print('1')
    # # 核密度图
    # print('4')
    # g = sns.set("paper", font_scale =1.3)
    g = sns.set_style("white", {"xtick.major.size": 4, "ytick.major.size": 4})
    plt.rcParams['font.family'] = ['Adobe Fangsong Std', 'sans-serif']
    # plt.rcParams["axes.labelsize"] = 30
    # plt.xlabel("课程难度", size=18)
    # plt.ylabel("每个学生给予教授的评分", size=18)
    data = data.rename(index=str, columns={'diff_index': '课程难度', 'star_rating': '教授综合得分'})
    g = sns.jointplot(x = '课程难度', y = '教授综合得分',data=data,height=8, ratio=6, kind="kde", xlim=(1,5), ylim=(1.0, 5.0),space=0,color = '#71c9de')
    g.set_axis_labels('课程难度','教授综合得分', fontsize=22)

    # g.ax_joint.legend_.remove()  # 去除相关和P值
    g = sns.regplot(data['课程难度'], data['教授综合得分'], scatter=False, ax=g.ax_joint,color='black')
    print('2')
    plt.text(-2.2, 1.5, r"Y=5.18-0.50X", fontsize=16)
    plt.text(-2.2, 1.2, r'$R^2$=0.20', fontsize=16)

    print('3')
    plt.show()
    # plt.draw()
    # plt.savefig('课程难度与评分关系1.png', dpi=300)


'''4。计算 [评分] 和 [是否再次选课] 的关系, 可视化'''
def rating_take_again_correlation():
    df = pd.read_csv(src, usecols=['professor_name', 'school_name','department_name','star_rating', 'diff_index','take_again'])
    df = df[(df['star_rating'] >= 1.0) & (df['diff_index'] >= 1.0)].drop_duplicates(['professor_name','school_name','department_name',], 'first', False)
    # df = df.replace(r'<span class="would-take-again">Would Take Again: <span class="response">N/A</span></span>\\r\\n                <span class="would-take-again">Would Take Again: <span class="response">N/A</span></span>\\r\\n                <span class="would-take-again">Would Take Again: <span class="response">N/A</span></span>\\r\\n                ',np.nan,regex=True)
    df['professor_take_again'] = df['take_again'].str.strip('%').astype(float) / 100  # 百分数转化成小数
    df = df.dropna()
    print(df.describe())  # 计算平均数，标准差
    g = sns.set("paper", font_scale=1.3)
    g = sns.set_style("white")
    # g = sns.set_style("white",{"xtick.major.size": 4, "ytick.major.size": 4})

    plt.rcParams['font.family'] = ['Adobe Fangsong Std', 'sans-serif']

    # 核密度图
    data = df.rename(index=str, columns={'professor_take_again': '再次选课', 'star_rating': '教授综合得分'})
    g = sns.jointplot(x = '教授综合得分',y = '再次选课', data=data, height=6, ratio=7, kind="kde", xlim=(1.0, 5.0),
                      ylim=(0.0, 1.0), space=0, color=r'#71c9de')
    g.set_axis_labels('教授综合得分', '再次选课', fontsize=20)
    # g.ax_joint.legend_.remove()# 去除相关和P值
    g = sns.regplot(data['教授综合得分'], data['再次选课'], scatter=False, ax=g.ax_joint, color='black')

    plt.text(-14.2, 0.2, r"Y=-0.30+0.26X", fontsize=16)
    plt.text(-14.2, 0.1, r'$R^2$=0.64', fontsize=16)
    plt.show()
    # plt.draw()
    # plt.savefig('评分+再次选课2.png', dpi=300)


if __name__ == "__main__":
    src = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP.csv'
    # professor_rating_year_trend(src)
    # violinplot_rating_greades()
    # violinplot_rating_mandatory()
    rating_difficulty_correlation()
    # rating_take_again_correlation()
