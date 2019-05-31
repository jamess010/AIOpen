# Librosa

### docker 目录
deepo docker：包含 librosa、python3.6、tensorflow、pytorch等。

### Tips

1. 机器学习第一步是特征提取，语音领域也不例外。目前使用最多的是FBank（Filter banks）和MFCC，两者整体相似，MFCC多了一步DCT（离散余弦变换）。 

2. 目前，用的多得是Fbank，因为fbank的信息比MFCC丰富（因为DCT只提取了频谱的包络信息，而损失了大量的声音细节），MFCC多了一步DCT，某种程度上是对语音信息的损变，而且因为多了一步，计算量更大。

3. FBank 适用于深度学习。因为，深度神经网络强大的特征提取能力使得我们只需要将信息更加丰富的Mel谱（或功率谱）信息直接送入神经网络进行训练，让神经网络提取更加鲁棒的特征。

4. MFCC 配合 GMM，HMM 声学模型比较合适。

5. 
