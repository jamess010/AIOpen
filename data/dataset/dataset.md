# 标签解释

### (经典)
这些是在 AI 领域中非常著名、众所周知的数据集。很少有研究者或工程师没有听说过它们。

### (有用) 
这些是更加接近现实世界的、精心设计的数据集。而且，这些数据集通常在产品和研发两方面都有用。

### (学术) 
这些是在机器学习和 AI 的学术研究中通常作为基准或基线使用的数据集。无论好坏，研究人员都使用这些数据集来验证算法。

### (陈旧) 
这些数据集，无论是否实用，已经有相当长历史了。

### (收费)
这些是收费数据集，用户可以根据情况决定是否购买使用。

# 计算机视觉

MNIST(学术、经典、陈旧):最常用的数据集，图像大小为28x28的手写数字，在 MNIST 上性能良好，并不意味着模型本身很好。</br>
地址：http://yann.lecun.com/exdb/mnist/

CIFAR 10 & CIFAR 100(经典、陈旧)：32x32的彩色图像数据集，虽然已经不常用，但也可以用作完整性检查。</br>
地址：https://www.cs.toronto.edu/~kriz/cifar.html

ImageNet(有用、学术、经典)：新算法实际上使用的图像数据集，很多图像 API 公司从其 REST 接口获取标签，这些标签被怀疑与 ImageNet 的下一级 WordNet 的 1000 个类很相似。</br>
地址：http://image-net.org/

LSUN：用于场景理解和多任务辅助（房间布局估计，显着性预测等）。</br>
地址：http://lsun.cs.princeton.edu/2016/

PASCAL VOC(学术)：一个通用的图像分割/分类数据集，对构建真实图像的注释用处不是特别大，但对于基线很有用。</br>
地址：http://host.robots.ox.ac.uk/pascal/VOC/

SVHN(学术)：数据来源于 Google 街景视图中的房屋数量，可以用作野外的周期性 MNIST。</br>
地址：http://ufldl.stanford.edu/housenumbers/

MS COCO：一个通用的图像理解/字幕数据集。</br>
地址：http://mscoco.org/

Visual Genome(有用)：非常详细的视觉知识数据集，包含约100K图像的深字母。</br>
地址：http://visualgenome.org/

Labeled Faces in the Wild(有用、学术、经典、陈旧)：使用名称标识符标记的面部区域数据集，常用于训练面部识别系统。</br>
地址：http://vis-www.cs.umass.edu/lfw/

# 自然语言处理

Text Classification Datasets(有用、学术)：一个文本分类数据集，包含8个可用于文本分类的子数据集，样本大小从120K到3.6M，问题范围从2级到14级，数据来源于 DBPedia、Amazon、Yelp、Yahoo!、Sogou 和 AG。</br>
地址：http://t.cn/RJDVxr4

WikiText(有用、学术)：由 Salesforce MetaMind 设计的大型语言建模语料库，来源于维基百科文章。</br>
地址：http://t.cn/RJDVSRy/

Question Pairs(有用)：第一个来源于 Quora 的包含重复/语义相似性标签的数据集。</br>
地址：https://data.quora.com/First-Quora-Dataset-Release-Question-Pairs

SQuAD(有用、学术)：斯坦福大学的问答数据集，广泛用于问题回答和阅读理解，其中每个问题和答案都是文本片段的形式。</br>
地址：https://rajpurkar.github.io/SQuAD-explorer/

CMU Q/A Dataset：人工生成的问题/答案对，难度评级来自维基百科文章。</br>
地址：http://www.cs.cmu.edu/~ark/QA-data/

Maluuba Datasets(有用)：用于状态性的自然语言理解研究的人工制作的精细数据集。</br>
地址：https://datasets.maluuba.com/

Billion Words(有用、学术)：一个大型、通用的语言建模数据集，常用于如 word2vec 或 Glove 的分布式词语表征。</br>
地址：http://www.statmt.org/lm-benchmark/

【有用、学术】Common Crawl：Petabyte 级规模的网络爬行数据集，常用于学习词嵌入。</br>
地址：http://commoncrawl.org/the-data/

【学术、经典】bAbi：来自 FAIR 的阅读理解和问答应答数据集。</br>
地址：https://research.fb.com/projects/babi/

【学术】The Children’s Book Test：从古登堡计划的童书中提取的（问题+上下文，答案）的基线，该数据集对问题回答、阅读理解和模拟陈述有用。</br>
地址：https://research.fb.com/projects/babi/

【学术、经典、陈旧】Stanford Sentiment Treebank：一个标准情感数据集，数据集中每个句子解析树的每个节点都有精细的情感注释。</br>
地址：http://nlp.stanford.edu/sentiment/code.html

【经典、陈旧】20 Newsgroups：一个文本分类的经典数据集，通常用于纯分类或作为任何 IR／索引算法的基准。</br>
地址：http://qwone.com/~jason/20Newsgroups/

【经典、陈旧】Reuters：一个较旧，完全基于分类的新闻文本数据集，常用于教程。</br>
地址：http://t.cn/RJDfi7T

【经典、陈旧】IMDB：一个比较旧，规模也相对较小的二院情感分类数据集。</br>
地址：http://ai.stanford.edu/~amaas/data/sentiment/

【经典、陈旧】UCI’s Spambase：这是一个年代较久远的、经典的垃圾电子邮件数据集，来源是著名的 UCI 机器学习库。由于该数据集在设计细节上的独特之处，可以用作学习个性化垃圾邮件过滤的一个有趣的基线。</br>
地址：https://archive.ics.uci.edu/ml/datasets/Spambase


