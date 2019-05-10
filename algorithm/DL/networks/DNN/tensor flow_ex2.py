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

# + {"code_folding": [0]}
# 1->0 单层网络

import tensorflow as tf

x = tf.constant(1.0, dtype = tf.float32)
y = tf.constant(0.5, dtype = tf.float32)

w = tf.Variable(1.0,dtype=tf.float32)
b = tf.Variable(0.5,dtype=tf.float32)

l_net = w*x + b
l_out = tf.sigmoid(l_net)
# -

# # prefix

# $ loss = \frac{1}{2}*(y - l_{out})^2 \space\space(MSE) $

loss = .5*tf.square(y - l_out)

# ### 函数
# $ w = w - \eta*\frac{\partial E}{\partial w}, \space\space b = b - \eta*\frac{\partial E}{\partial b}$ 
#
# $ 其中：\eta = LearningRate $
#
# $ \eta*\frac{\partial E}{\partial w} 为梯度 $

LearningRate = 1
optimizer = tf.train.GradientDescentOptimizer(LearningRate)

# $ compute_gradients返回值为：(\eta*\frac{\partial E}{\partial w}, w)(\eta*\frac{\partial E}{\partial b}, b)$

# + {"code_folding": [0]}
# 计算梯度值，返回：w梯度，w，b梯度，b
# w梯度 = LearningRate*dE/dw
# b梯度 = LearningRate*dE/db
grad = optimizer.compute_gradients(loss,[w,b])
# -

# $ w = w - \eta*\frac{\partial E}{\partial w}, \space\space b = b - \eta*\frac{\partial E}{\partial b}$

# 将 w = w - w梯度， b = b - b梯度 计算出来，并应用到grad中
grad_delta = optimizer.apply_gradients(grad)

# +
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    sess.run(grad,feed_dict={x:1,y:0})
    sess.run(grad_delta, feed_dict={x:1,y:0})
    lost_value = sess.run(loss,feed_dict={x:1,y:0})
    print sess.run([w,b,l_out]), lost_value
    
