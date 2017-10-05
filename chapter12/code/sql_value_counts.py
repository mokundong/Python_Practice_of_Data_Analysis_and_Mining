#-*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
#建立与数据库连接
engie = create_engine('mysql://hive:123456@127.0.0.1:3306/python')
sql = pd.read_sql('all_gzdata',engie,chunksize=10000)#内存不够 分块读取

#网页类型分析
counts = [i['fullURLId'].value_counts() for i in sql]#逐块统计
counts = pd.concat(counts).groupby(level=0).sum()#合并统计结果，把相同的统计合并（按照index分组并求和）
counts = counts.reset_index()#重新设置index，将原来的index作为counts的一列
counts.columns = ['index','num']#重新设置列名，主要是第二列，默认为0
counts['type'] = counts['index'].str.extract('(\d{3})',expand=None)#提取前3个数字作为类别id
counts_ = counts[['type','num']].groupby('type').sum()#按类别合并
counts_.sort_values(by='num',ascending = False)#降序排列

#统计107类别的情况
def count107(i): #自定义统计函数
  j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy() #找出类别包含107的网址
  j['type'] = None #添加空列
  j['type'][j['fullURL'].str.contains('info/.+?/')] = u'知识首页'
  j['type'][j['fullURL'].str.contains('info/.+?/.+?')] = u'知识列表页'
  j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')] = u'知识内容页'
  return j['type'].value_counts()

sql = pd.read_sql('all_gzdata',engie,chunksize=10000)
counts2 = [count107(i) for i in sql] #逐块统计
counts2 = pd.concat(counts2).groupby(level=0).sum() #合并统计结果
print(counts2)

#统计点击次数
sql = pd.read_sql('all_gzdata',engie,chunksize=10000)
c = [i['realIP'].value_counts() for i in sql]#分块读取各个ip的出现次数
count3 = pd.concat(c).groupby(level = 0).sum() #合并统计结果，level=0表示按index分组
count3 = pd.DataFrame(count3) #Series转为DataFrame
count3[1] = 1 #添加一列，全为1
count3.groupby(0).sum() #统计各个“不同的点击次数”分别出现的次数
print(count3)