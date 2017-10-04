#-*- coding: utf-8 -*-
#数据规范化
import pandas as pd
datafile = '../data/discretization_data.xls'
data = pd.read_excel(datafile)
data = data[u'肝气郁结证型系数'].copy()

k = 4

d1 = pd.cut(data,k,labels=range(k))

#等频率离散化
w = [1.0*i/k for i in range(k+1)]
w = data.describe(percentiles = w)[4:4+k+1]#取出百分位数段
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(data,w,labels=range(k))

from sklearn.cluster import KMeans
kmodel = KMeans(n_clusters=k)
kmodel.fit(data.values.reshape((len(data),1)))
c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)#输出聚类中心，并且排序
#w = pd.rolling_mean(c,2).iloc[1:]#相邻两项求中点，作为边界线
w = pd.DataFrame.rolling(c,center = False,window = 2).mean().iloc[1:]#iloc通过行号读取行数据
w = [0] + list(w[0]) + [data.max()]#加上首末边界
d3 = pd.cut(data,w,labels=range(k))

def cluster_plot(d,k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']#用于正常显示中文
    plt.rcParams['axes.unicode_minus'] = False#用于正常显示负号

    plt.figure(figsize=(8,3))
    for j in range(0,k):
        plt.plot(data[d==j],[i for i in d[d==j]],'o')

    plt.ylim(-0.5,k-0.5)
    return plt

cluster_plot(d1,k).show()
cluster_plot(d2,k).show()
cluster_plot(d3,k).show()