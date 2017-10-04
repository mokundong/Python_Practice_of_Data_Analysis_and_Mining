#-*- coding: utf-8 -*-
#线损率属性构造
import pandas as pd

inputfile = '../data/electricity_data.xls'
outputfile = '../tmp/electricity_data.xls'

data = pd.read_excel(inputfile)
data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量'])/data[u'供入电量']

data.to_excel(outputfile,index=False)