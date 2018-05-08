#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: a.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年05月07日 星期一 19时39分56秒
########################################################################
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

n = 1000
X = np.linspace(-2,3,n)
Y = X*0.8
Z = X*X*Y

ax = plt.subplot(111, projection='3d')
ax.scatter(X,Y,Z)
X += np.random.rand(n)
Y += np.random.rand(n)
Z += np.random.rand(n)
ax.scatter(X,Y,Z,c='r')

plt.show()

_X = np.expand_dims(X,1)
_Y = np.expand_dims(Y,1)
_Z = np.expand_dims(Z,1)
data = np.hstack((_X,_Y,_Z))
np.savetxt('mydata.txt', data, fmt='%.4f', delimiter=',')
