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

# 在统计与机器学习领域权衡 Bias  与 Variance 是一项重要的任务，因为他可以使得用有限训练数据训练得到的模型更好的范化到更多的数据集上，监督学习中的误差来源主要为 Bias 与 Variance，接下来来看误差来源的推导。
#
# 我们知道，同样的算法在不同的数据集上得到的模型结果很可能不同，尽管数据集来自于同一个分部。对于观测数据 $X$ 以及待预测的变量 $Y$ ，假设两者服从 $Y = f(X) + \varepsilon$ ，$\varepsilon$ 为噪声，其服从的$N(0,\delta_{\varepsilon }^2)$ ，预测任务中需要得到 $Y$ 值，首先在数据集 $D$ 上通过算法学习一个近似 $f(X)$ 的模型 $\hat{f}(X)$ 来预测得到 $X$ 的输出。给定 $X$ 一个观测值 $x$ ，待预测变量 $y = f(x) +\varepsilon$ 。
#
# 对于样本数量相同的不同训练集模型 $\hat{f}(x)$ 的期望输出为： $E\hat{f}(x)$
# 对于样本数量相同的不同训练集模型产生的方差为：$E[\hat{f}(x) - E\hat{f}(x)]^2$
# 将模型的误差分解，采用均方损失，模型 $\hat{f}(X)$ 在点 $x$ 的整体预测误差为真实值与模型预测值之间的误差：$Err(x) = E[(y - \hat{f}(x))^2]$这个式子其实等价于：
#
# $Err(x) = [E \hat{f}(x) –f(x)]^2 +E[\hat{f}(x) - E\hat{f}(x)]^2 + \delta_{\varepsilon }^2$

# 这里为推倒过程，先回忆几个公式 ：$Var[X] = E[X^2]-E^2[X]$ ， 且由于函数 $f(X)$ 是确定的，所以 $E[f(x)] = f(x)$，且有 $\varepsilon \sim N(0,\delta_{\varepsilon }^2)$ ，再结合 $y = f(x)  + \varepsilon$ 可以得到：
#
# \[E[y] = E[f(x) + \varepsilon] = E[f(x)]+0 =E[f(x)] \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \tag{1} \]
#
# \[Var[y] = E[(y-E[y])^2] = E[(f(x) + \varepsilon –f(x))^2] = E[\varepsilon^2] = \delta_{\varepsilon }^2  \tag{2}\]
#
# \begin{aligned}
# Err(x) &= E[(y - \hat{f}(x))^2] \\
# &= E[y^2 - 2y \hat{f}(x) + \hat{f}^2(x)] \\
# &= E[y^2] - E[2y \hat{f}(x)] + E[\hat{f}^2(x)] \\
# &= E[y^2] \mathbf{- E^2[y] +E^2[y]} - 2E[y]E[\hat{f}(x)] + E[\hat{f}^2(x)] \mathbf{ -E^2[\hat{f}(x)]+ E^2[\hat{f}(x)]} \\
# & \ \ \ \ \ \ \mathbf{Combined \ with\ the\ above\ equations \ (1) \ (2).} \\
# &= \color{Blue} {E^2[\hat{f}(x)] - 2f(x)E[\hat{f}(x)] +f^2(x)} +\color{Green} {E[\hat{f}^2(x)] -E^2[\hat{f}(x)]} + \color{Red} {E[y^2] - E^2[y]} \\
# & \ \ \ \ \ \ \mathbf{The \ last\ two \ terms \ based \ on }: Var[X] = E[X^2] -E^2[X] \\
# &= [E[\hat{f}(x)]-f(x)]^2+E[(\hat{f}(x)-E\hat{f}(x))^2]+Var[y] \\
# &= E^2[\hat{f}(x)] +Var[\hat{f}(x)] +\delta_{\varepsilon}^2 \\
# \end{aligned}

# $E \hat{f}(x) –f(x)$ 即为 Bias ，$E[\hat{f}(x) - E\hat{f}(x)]^2$ 为 Variance ， $\delta_{\varepsilon}^2$  即为模型无法避免的 Noise ，也可称为 Irreducible  Error ，所以现在对于一个预测模型的误差可以 分为如下几部分：
#
# $Error = Bias^2 +Variance + Noise $
#
# 对于预测模型问题，如果我们能够获得所有可能的数据集合，并在这个数据集合上将 Error 最小化，这样学习到的模型就可以称之为“真实模型”，当然，我们是无论如何都不能获得并训练所有可能的数据的，所以“真实模型”肯定存在，但无法获得，我们的最终目标就是去学习一个模型使其更加接近这个真实模型。为了在有限的训练数据集上达到这个目标，就要使 Error 最小了，Error 分为 Bias 、 Variance 与 Noise ：
#
# Bias：度量了学习算法的期望输出与真实结果的偏离程度, 刻画了算法的拟合能力，Bias 偏高表示预测函数与真实结果差异很大。
# Variance：则代表“同样大小的不同的训练数据集训练出的模型”与“这些模型的期望输出值”之间的差异。训练集变化导致性能变化， Variance 偏高表示模型很不稳定。
# Noise：刻画了当前任务任何算法所能达到的期望泛化误差的下界，即刻画了问题本身的难度。
# 由于 Bias 是无法避免的 所以要得到好的模型，就需要低 Bias 与低 Variance 下图给出一个 Bias 与 Variance 的示意图，明显可以看到低 Bias 与低 Variance 次次会命中靶心，而低 Bias 高 Variance 取均值后才会大多命中靶心，其他情况全打歪了。

#
