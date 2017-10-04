#-*- coding: utf-8 -*-
#构建CART决策树模型
import pandas as pd
from random import shuffle
import matplotlib.pyplot as plt

datafile = '../data/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)

p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]

from sklearn.tree import DecisionTreeClassifier
treefile = '../data/tree.pkl'#模型输出名字
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])
#保存模型
from sklearn.externals import joblib
joblib.dump(tree,treefile)
from cm_plot import *
cm_plot(train[:,3],tree.predict(train[:,:3])).show()

from sklearn.metrics import roc_curve#导入ROC曲线函数


fpr,tpr,thresholds = roc_curve(test[:,3],tree.predict_proba(test[:,:3])[:,1],pos_label=1)
plt.plot(fpr,tpr,linewidth=2,label='ROC of LM')#制作ROC曲线
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.xlim(0,1.05)
plt.ylim(0,1.05)
plt.legend(loc=4)
plt.show()