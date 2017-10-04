#-*- coding: utf-8 -*-
#数据规范化
import pandas as pd
import numpy as np

datafile = '../data/normalization_data.xls'
data = pd.read_excel(datafile,header=None)

(data - data.min()) / (data.max() - data.min())#最大最小规范化
(data - data.mean()) / data.std()#零-均值规范化
data/10**np.ceil(np.log10(data.abs().max()))#小数定标规范化