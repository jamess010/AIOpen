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

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
#
# # Librosa tutorial
#
# - Version: 0.6.3
# - Tutorial home: https://github.com/librosa/tutorial
# - Librosa home: http://librosa.github.io/
# - User forum: https://groups.google.com/forum/#!forum/librosa

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## 环境
#
# 假设已经安装了 [Anaconda](https://anaconda.org/).
#
# 如果没有环境，使用下面命令创建一个：
#
# ```bash
# conda create --name YOURNAME scipy jupyter ipython
# ```
# (使用 `YOURNAME` 来代替新的环境名)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# 然后使用下面命令来激活新的环境：
# ```bash
# source activate YOURNAME
# ```
#

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# ## 安装 librosa
# Librosa 使用下面命令进行安装 [🔗]:
#
# ```bash
# conda install -c conda-forge librosa
# ```
#
# 注意：Windows 需要单独安装音频解码库，这里推荐使用 [ffmpeg](http://ffmpeg.org/).

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## 测试

# + {"slideshow": {"slide_type": "-"}, "cell_type": "markdown"}
# 开始 Jupyter:
# ```bash
# jupyter notebook
# ```
# 然后打开一个notebook，执行下面命令：

# + {"slideshow": {"slide_type": "-"}}
import librosa
print(librosa.__version__)

# + {"slideshow": {"slide_type": "fragment"}}
y, sr = librosa.load(librosa.util.example_audio_file())
print(len(y), sr)
# -

# ### 注：上面的load的缺省sr=22050，如果需要原始的音频采样率sr=None

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # librosa文档!
#
#
# Librosa有大量的例子文档，请参阅：http://librosa.github.io/librosa/

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # 约定
#
# - 所有数据是基本的 `numpy` 类型
# - **Audio buffers**（音频数据缓存） 称为 `y`
# - **Sampling rate**（采样率）称为 `sr`
# - The last axis is time-like:
#         y[1000] 是第1001各样本
#         S[:, 100] 是第101的个S的帧
# - **Defaults** （缺省）`sr=22050`, `hop_length=512`

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # 今天要学习的内容
#
# - `librosa.core`
# - `librosa.feature`
# - `librosa.display`
# - `librosa.beat`
# - `librosa.segment`
# - `librosa.decompose`

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# # `librosa.core`
#
# - Low-level audio processes（底层的音频处理）
# - Unit conversion（单元转换）
# - Time-frequency representations（时间-频率变换）

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
#
# 使用原始采样率加载音频文件，使用 `sr=None`

# + {"slideshow": {"slide_type": "-"}}
y_orig, sr_orig = librosa.load(librosa.util.example_audio_file(),
                     sr=None)
print(len(y_orig), sr_orig)

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# Resampling is easy（重新采样非常容易）

# + {"slideshow": {"slide_type": "-"}}
sr = 22050

y = librosa.resample(y_orig, sr_orig, sr)

print(len(y), sr)

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# But what's that in seconds?（但是时间多长？）

# + {"slideshow": {"slide_type": "-"}}
print(librosa.samples_to_time(len(y), sr))

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## 频谱表示
#
# 短时傅立叶变换是信号处理的基础。
#
# `librosa.stft` 返回一个复数矩阵 `D`.
#
# `D[f, t]` 是：以频率 `f`, 时间（帧） `t` 的 FFT 值 .

# + {"slideshow": {"slide_type": "fragment"}}
D = librosa.stft(y)
print(D.shape, D.dtype)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# Often, we only care about the magnitude.（通常，我们比较关心幅值）
#
# `D` 包含幅值 *magnitude* `S` 和相角 *phase* $\phi$.
#
# $$
# D_{ft} = S_{ft} \exp\left(j \phi_{ft}\right)
# $$
# -

import numpy as np 

S, phase = librosa.magphase(D)
print(S.dtype, phase.dtype, np.allclose(D, S * phase))

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Constant-Q transforms (恒Q变换)
#
# CQT指中心频率按指数规律分布，滤波带宽不同、但中心频率与带宽比为常量Q的滤波器组。它与傅立叶变换不同的是，它频谱的横轴频率不是线性的，而是基于log2为底的，并且可以根据谱线频率的不同该改变滤波窗长度，以获得更好的性能。由于CQT与音阶频率的分布相同，所以通过计算音乐信号的CQT谱，可以直接得到音乐信号在各音符频率处的振幅值，对于音乐的信号处理来说简直完美。
#

# +
C = librosa.cqt(y, sr=sr)

print(C.shape, C.dtype)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## 练习 0
#
# - Load a different audio file （加载一个不同的音频文件）
# - Compute its STFT with a different hop length（使用不同的hop长度来计算它的STFS）

# + {"slideshow": {"slide_type": "subslide"}}
# Exercise 0 solution

y2, sr2 = librosa.load(   )

D = librosa.stft(y2, hop_length=   )

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # `librosa.feature`
#
# - Standard features:
#     - `librosa.feature.melspectrogram`
#     - `librosa.feature.mfcc`
#     - `librosa.feature.chroma`
#     - Lots more...
# - Feature manipulation:
#     - `librosa.feature.stack_memory`
#     - `librosa.feature.delta`

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# Most features work either with audio or STFT input

# +
melspec = librosa.feature.melspectrogram(y=y, sr=sr)

# Melspec assumes power, not energy as input
melspec_stft = librosa.feature.melspectrogram(S=S**2, sr=sr)

print(np.allclose(melspec, melspec_stft))

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # `librosa.display`
#
# - Plotting routines for spectra and waveforms
#
# - **Note**: major overhaul coming in 0.5

# + {"slideshow": {"slide_type": "subslide"}}
# Displays are built with matplotlib 
import matplotlib.pyplot as plt

# Let's make plots pretty
import matplotlib.style as ms
ms.use('seaborn-muted')

# Render figures interactively in the notebook
# %matplotlib nbagg

# IPython gives us an audio widget for playback
from IPython.display import Audio

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Waveform display

# + {"slideshow": {"slide_type": "-"}}
plt.figure()
librosa.display.waveplot(y=y, sr=sr)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## A basic spectrogram display
# -

plt.figure()
librosa.display.specshow(melspec, y_axis='mel', x_axis='time')
plt.colorbar()

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Exercise 1
#
# * Pick a feature extractor from the `librosa.feature` submodule and plot the output with `librosa.display.specshow`
#
#
# * **Bonus**: Customize the plot using either `specshow` arguments or `pyplot` functions

# + {"slideshow": {"slide_type": "subslide"}}
# Exercise 1 solution

X = librosa.feature.XX()

plt.figure()

librosa.display.specshow(    )

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # `librosa.beat`
#
# - Beat tracking and tempo estimation

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# The beat tracker returns the estimated tempo and beat positions (measured in frames)

# + {"slideshow": {"slide_type": "fragment"}}
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
print(tempo)
print(beats)

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# Let's sonify it!

# + {"slideshow": {"slide_type": "-"}}
clicks = librosa.clicks(frames=beats, sr=sr, length=len(y))

Audio(data=y + clicks, rate=sr)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# Beats can be used to downsample features
# -

chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
chroma_sync = librosa.feature.sync(chroma, beats)

# + {"slideshow": {"slide_type": "fragment"}}
plt.figure(figsize=(6, 3))
plt.subplot(2, 1, 1)
librosa.display.specshow(chroma, y_axis='chroma')
plt.ylabel('Full resolution')
plt.subplot(2, 1, 2)
librosa.display.specshow(chroma_sync, y_axis='chroma')
plt.ylabel('Beat sync')

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # `librosa.segment`
#
# - Self-similarity / recurrence
# - Segmentation

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# Recurrence matrices encode self-similarity
#
#     R[i, j] = similarity between frames (i, j)
#     
# Librosa computes recurrence between `k`-nearest neighbors.

# + {"slideshow": {"slide_type": "-"}}
R = librosa.segment.recurrence_matrix(chroma_sync)

# + {"slideshow": {"slide_type": "fragment"}}
plt.figure(figsize=(4, 4))
librosa.display.specshow(R)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# We can include affinity weights for each link as well.

# + {"slideshow": {"slide_type": "-"}}
R2 = librosa.segment.recurrence_matrix(chroma_sync,
                                       mode='affinity',
                                       sym=True)

# + {"slideshow": {"slide_type": "fragment"}}
plt.figure(figsize=(5, 4))
librosa.display.specshow(R2)
plt.colorbar()

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Exercise 2
#
# * Plot a recurrence matrix using different  features
# * **Bonus**: Use a custom distance metric

# + {"slideshow": {"slide_type": "subslide"}}
# Exercise 2 solution

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # `librosa.decompose`
#
# - `hpss`: Harmonic-percussive source separation
# - `nn_filter`: Nearest-neighbor filtering, non-local means, Repet-SIM
# - `decompose`: NMF, PCA and friends

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# Separating harmonics from percussives is easy

# +
D_harm, D_perc = librosa.decompose.hpss(D)

y_harm = librosa.istft(D_harm)

y_perc = librosa.istft(D_perc)

# + {"slideshow": {"slide_type": "fragment"}}
Audio(data=y_harm, rate=sr)
# -

Audio(data=y_perc, rate=sr)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# NMF is pretty easy also!
# -

# Fit the model
W, H = librosa.decompose.decompose(S, n_components=16, sort=True)

plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1), plt.title('W')
librosa.display.specshow(librosa.logamplitude(W**2), y_axis='log')
plt.subplot(1, 2, 2), plt.title('H')
librosa.display.specshow(H, x_axis='time')

# + {"slideshow": {"slide_type": "subslide"}}
# Reconstruct the signal using only the first component
S_rec = W[:, :1].dot(H[:1, :])

y_rec = librosa.istft(S_rec * phase)

# + {"slideshow": {"slide_type": "-"}}
Audio(data=y_rec, rate=sr)

# + {"slideshow": {"slide_type": "subslide"}, "cell_type": "markdown"}
# ## Exercise 3
#
# - Compute a chromagram using only the harmonic component
# - **Bonus**: run the beat tracker using only the percussive component

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Wrapping up
#
# - This was just a brief intro, but there's lots more!
#
# - Read the docs: http://librosa.github.io/librosa/
# - And the example gallery: http://librosa.github.io/librosa_gallery/
# - We'll be sprinting all day.  Get involved! https://github.com/librosa/librosa/issues/395
