# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# # %load draw_derivative.py
#!/usr/bin/env python2
"""
Created on Tue Nov  7 03:35:37 2017

@author: tjian
"""
import numpy as np
import matplotlib.pyplot as plt

# 在任意点的导数，画切线
def derivative(point):
    dx = np.arange(-1.5, 1.5, 0.1)
    dy = 2*point
    return [dx+point, dy*dx + point**2]

x = np.arange(-6,6,0.1)
y = x**2

x1, y1 = derivative(1)
plt.plot(x,y)
plt.plot(x1,y1, linewidth=3,linestyle='dashed')
plt.show()


# -

# 以下是画sigmoid函数
#
# 定义sigmoid函数：
# > $$ \sigma{(x)} = \frac{1}{1+e^{-x}}$$

def sigmoid(x):
    return 1/(1+np.exp(-x))


# 定义sigmoid的导数：
# > $$ \sigma^{'}(x) = \frac{\partial{\sigma}}{\partial{x}} = \sigma{(x)}*(1 - \sigma{(x)})$$

def sigmoid_derivative(x):
    y = 1/(1+np.exp(-x))
    return y*(1-y)


# 定义画sigmoid上某一点的切线函数：
# > 当已知斜率k和一点坐标$(x_1,y_1)$时，常用点斜式：$$ y - y_1 = k*(x - x_1)$$ 
# > 当已知斜率k和y轴截率b时，常用斜截式：$$y = k*x + b$$
# > 当已知两点坐标$(x_1,y_1)$和$(x_2,y_2)时，常用两点式：$$$\frac{x - x_1}{x_2 - x_1}=\frac{y - y_1}{y_2 - y_1}$$
#
# > 当已知所有截率a和b时，常用截距式：$$\frac{x}{a}+\frac{y}{b}=1$$
# > 矩阵：$X^m_n$ 是一个m*n矩阵，其中m=行（row）， n=列（column）
#
# > $\nabla{L}$   $\widehat{y}$  $\frac{\partial{x}}{\partial{y}}$   $\sigma{(x)}$

def draw_sigmoid_derivative(point):
    dx = np.arange(-1.0,1.0,0.1)
    dy = sigmoid_derivative(point) # 某点导数就是过这点的切线斜率
    tangent_line = dy*dx + sigmoid(point)# 切线公式 y = k*x + b 其中：k是斜率，b是截率    
    return [point + dx, tangent_line]


# 画在sigmoid x = 2, 0, -2 处的切线：

x1, y1 = draw_sigmoid_derivative(2)
y = sigmoid(x)
plt.plot(x, y)
plt.plot(x1,y1)
x2, y2 = draw_sigmoid_derivative(0)
plt.plot(x2,y2,'g')
x3, y3 = draw_sigmoid_derivative(-2)
plt.plot(x3,y3,'y')
plt.grid()
plt.show()




