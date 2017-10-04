#-*- coding: utf-8 -*-
#使用Apriori算法挖掘菜品订单的关联规则
from __future__ import print_function
import pandas as pd
from apriori import * #自己编写的apriori算法

inputfile = '../data/menu_orders.xls'
outputfile = '../tmp/apriori_rules.xls'
data = pd.read_excel(inputfile)

print(u'\n转换原始数据至0-1矩阵')
ct = lambda x:pd.Series(1,index=x[pd.notnull(x)])#转换0-1矩阵的过渡函数
b = map(ct,data.as_matrix())#用map的方式执行
data = pd.DataFrame(list(b)).fillna(0)#实现矩阵转换用0填充
print(u'\n转换完毕')
del b#删除中间变量

suppot = 0.2#最小支持度
confidence = 0.5#最小置信度
ms = '---'#连接符，默认’--‘,用来区分不同元素，如A--B。需要保证原始表格中不含有该字符
find_rule(data,suppot,confidence,ms).to_excel(outputfile)

