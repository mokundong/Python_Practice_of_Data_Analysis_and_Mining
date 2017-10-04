#-*- coding: utf-8 -*-
import pandas as pd

filename = '../data/sales_data.xls'
data = pd.read_excel(filename,index_col=u'序号')
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data !=1] = -1
x = data.iloc[:,:3].astype(int)
y = data.iloc[:,3].astype(int)

from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC()
dtc.fit(x,y)

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open('../tmp/tree.dot','w') as f:
    f = export_graphviz(dtc,feature_names=x.columns,out_file=f)
