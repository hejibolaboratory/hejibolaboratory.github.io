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
from matplotlib import rcParams
from scipy.stats import sem

def professor_rating_year_trend(file):
    df = pd.read_csv(file)
    print('去重前教授个数',df['professor_name'].count()) # 9543998
    df = df.drop_duplicates(['professor_name','school_name','department_name'], 'first', False)
    print(df.describe())
    print('去重后教授个数',df['professor_name'].count()) # 919750

    # 计算平均数，标准误差，置信区间
    df_mean = df.groupby('year_since_first_review').star_rating.mean()
    df_se = df.groupby('year_since_first_review').star_rating.apply(sem).mul(1.96)
    count = df.groupby('year_since_first_review').professor_name.count()
    print('mean',df_mean)
    print('se',df_se)


    df_std = df.groupby('year_since_first_review').star_rating.std()
    print('标准差')
    print('std', df_std)


    x = df_mean.index.astype(int)
    sum = count.astype(int)
    print(count.astype(int))

    # Plot
    fig, ax1 = plt.subplots(figsize = (16, 8))
    rcParams['font.family'] = 'sans-serif'
    ax1.set_xlim([0, 19])
    ax1.set_ylabel("Average Star Rating", fontsize=14)
    ax1.plot(list(x), list(df_mean), color="black", lw=1)
    ax1.fill_between(x, df_mean - df_se, df_mean + df_se, color="#b7dafc",lw=5) #显示标准区间
    plt.xlabel("Year Since First Review", fontsize=14)
    plt.yticks(size=14)
    plt.xticks( size=14)

    # # # Decorations
    # # Lighten borders
    # plt.gca().spines["top"].set_alpha(0)
    # plt.gca().spines["bottom"].set_alpha(1)
    # plt.gca().spines["right"].set_alpha(0)
    # plt.gca().spines["left"].set_alpha(1)
    # plt.xticks(x[::1], [str(d) for d in x[::1]] , fontsize=10)
    # # plt.title("Star Rating by Teaching", fontsize=18)

    s, e = plt.gca().get_xlim()
    plt.xlim(s, e)
    plt.axvline(6)  # 助理教授，分割线
    plt.axvline(12) # 副教授， 分割线
    # Draw Horizontal Tick lines
    for y in range(3, 5, 1):
        plt.hlines(y, xmin=s, xmax=e, colors='black', alpha=0.3, linestyles="--", lw=2)

    ax1.text(1.5, 1.5, r"Assistant Professor", fontsize=14)
    ax1.text(8, 1.5, r'Associate Professor', fontsize=14)
    ax1.text(15,1.5, r'Full Professor', fontsize=14)
    ax1.set_ylim([1.0, 5.0])

    # 显示教授人数
    ax2 = ax1.twinx()
    plt.ylabel('The Number of Professor', fontsize=14)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    plt.xticks(x[::2], [str(d) for d in x[::2]] , fontsize=14)
    for a,b in zip(x,sum):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)

    ax2.set_ylim([1, 180000])
    ax2.plot(list(x), list(sum), color="tomato") # 教授人数的变化趋势，代替柱状图

    fig.tight_layout() #自动调整子图参数，使之填充整个图像区域 https://www.jianshu.com/p/91eb0d616adb
    plt.yticks(size=14)
    plt.show()
    plt.draw()
    plt.savefig('professor_year_review_trend.png', dpi=300)

if __name__ == "__main__":
    file = r'/Users/liumingchun/【1】科研+实验室/3-科研项目/RateMyProfessor/bigdata/RMP_big_data.csv'
    professor_rating_year_trend(file)