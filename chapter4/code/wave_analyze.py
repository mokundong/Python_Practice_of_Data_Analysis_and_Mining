#-*- coding: utf-8 -*-
#利用小波变换分析进行特征分析
import pandas as pd

inputfile = '../data/leleccum.mat'

from scipy.io import loadmat
mat = loadmat(inputfile)
singal = mat['leleccum'][0]

import pywt
coeffs = pywt.wavedec(singal,'bior3.7',level=5)
#返回结果为level + 1 个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组