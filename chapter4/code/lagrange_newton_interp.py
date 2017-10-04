#-*- coding: utf-8 -*-
#拉格朗日
import pandas as pd
from scipy.interpolate import lagrange#导入拉格朗日插值函数

inputfile = '../data/catering_sale.xls'#销售数据路径
outputfile = '../tmp/sales.xls'#输出数据路径

data = pd.read_excel(inputfile)#读入数据
data2 = data.copy()
data2.loc[(data2[u'销量'] < 400) | (data2[u'销量'] > 5000)] = None #过滤异常值，将其变成空值

#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后数据的个数，默认为5
def ployinterp_column(s,n,k=5):
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]#取值
    y = y[y.notnull()]#剔除空值
    return lagrange(y.index,list(y))(n)#插值并返回插值结果

#逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:#如果为空则插值
            data[i][j] = ployinterp_column(data[i],j)

data.to_excel(outputfile)#输出结果，写入文件