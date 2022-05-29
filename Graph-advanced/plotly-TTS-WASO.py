'''
https://plotly.com/python/error-bars/
https://blog.csdn.net/qq_42761569/article/details/124179011?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_ecpm_v1~rank_v31_ecpm-2-124179011-null-null.pc_agg_new_rank&utm_term=plotly+%E7%94%BB%E5%8F%8C%E5%9D%90%E6%A0%87%E8%BD%B4&spm=1000.2123.3001.4430

'''

import plotly.graph_objects as go
import numpy as np
import pandas as pd


def fig_line(title, lx, dy):
    """绘制折线图
    :param title 标题
    :param lx x轴数据 []
    :param dy y轴数据 {fyt: [], syt: []}
    """
    if lx and dy:
        fyt = list(dy.keys())[0]
        syt = list(dy.keys())[1]
        line1 = go.Scatter(x=lx, y=dy[fyt], showlegend=True, line=dict(color='blue', width=1), connectgaps=True, mode='lines', opacity=0.9, name=fyt)
        line2 = go.Scatter(x=lx, y=dy[syt], showlegend=True, line=dict(color='red', width=1), connectgaps=True, mode='lines', opacity=0.9, name=syt, yaxis='y2')
        layout = go.Layout(
            # 设置标题
            # title=title,
            # 设置y轴label及范围
            yaxis=dict(title=fyt, range=[0, 2]),
            # 设置fig大小
            height=500,
            width=200,
            margin=dict(
                autoexpand=True,
                l=10,
                r=10,
                t=30,
                b=30,
            ),
            # 设置次y轴label及范围
            yaxis2=dict(title=syt, range=[0, 50], overlaying='y', side='right'),
            # 设置背景色
            # plot_bgcolor='gray',
            # 设置图例信息，x、y可以控制位置
            legend=dict(x=0.80, y=0.98, font=dict(size=12, color='black')))
        fig = go.Figure(data=[line1, line2], layout=layout)
        fig.show()


def main():
    """主函数"""
    lx = ['2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12']
    y1 = [0.919, 0.888, 0.163, 0.995, 0.723, 0.192, 0.069, 0.803, 0.645, 0.527, 0.675, 0.419]
    y2 = [20, 18, 15, 2, 8, 39, 26, 19, 26, 40, 5, 5]
    dy = {'应力(MPa)': y1, '温度(℃)': y2}
    title = '应力随温度变化情况'
    fig_line(title, lx, dy)


if __name__ == '__main__':
    main()
