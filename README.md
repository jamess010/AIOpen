# 目录
* [AIOpen简介](#aiopen简介)
* [AI三要素](#ai三要素)
* [AI开源全栈图](#ai开源全栈图)
* [深度学习流程](#深度学习流程)
* [典型案例分享](#典型案例分享)
* [目录说明](#目录说明)
* [术语解释](#术语解释)
* [参考资料](#参考资料)
* [联系我们](#联系我们)

---

# AIOpen简介

AIOpen是一个按人工智能三要素（数据、算法、算力）进行AI开源项目分类的汇集项目，项目致力于跟踪目前人工智能（AI）的深度学习（DL）开源项目，并尽可能地罗列目前的开源项目，同时加入了一些曾经研究过的代码。通过这些开源项目，使初次接触AI的人们对人工智能（深度学习）有更清晰和更全面的了解。

AI（人工智能）包括目前比较热门的深度学习、机器学习和与机器智能相关的技术。总体来说，人工智能包含了机器学习，机器学习包含了（神经网络）深度学习。它们之间的关系如下图：</br>

<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/ai_dl.png" width="600" height="200" /></div>
</br>

----

# AI三要素

人工智能的三要素：数据（data）、算法（algorithm）和算力（computing power）；三者之间的关系如下图：</br>
<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/ai_3key.png" width="460" height="230"/></div>


- #### 数据（data）：包括了数据集、数据获取（数据爬虫、数据区块链等）、数据存储、数据集群等；数据按来源可以分为三种：
  - 来自政府、大公司（google、BAT等）自上而下的公共数据集，如：MNIST，ImageNet，Kaggle等。
  - 来自企业的非公开数据，属于数据孤岛。
  - 使用区块链技术的自下而上的数据，如个人病例数据，个人基因数据，小企业数据，如果这方面技术成熟，DataBC（data block chain：数据区块链）将是未来发展的方向。[区块链技术](http://www.ContentBC.com)

- #### 算法（algorithm）：包括了深度学习方法（DNN、CNN、RNN、LSTM、GAN等）、工具（TensorFlow、Theano、Keras、Caffe、Touch等）、模型（VGG、RestNet等）；

- #### 算力（computing power）：包括了基础设施（GPU、FPGA）、容器技术（Dockker、Kubernetes）、Openstack等；

---

# AI开源全栈图

#### 下图是AI开源全栈图，本项目依据此图进行分类，每个分类均有对此分类的说明，请仔细阅读。</br>

<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/ai_all.png" width="600" height="520" /></div>

</br>

---

# 深度学习流程

#### 下图是一个基于监督学习的深度学习流程：</br>
<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/ai_supervised.png" /></div>

# 典型案例分享

## 数据

* [BDCloud](https://github.com/jamess010/AIOpen/tree/master/data/bdcloud)</br>
BDCloud是使用Docker实现的Hadoop集群技术，目的是实现对终端设备的监控信息进行采集、处理、存储、分析。其流程是终端采集信息->django处理信息->Kafka->Flume->HDFS->Spark分析信息。

* [CDH](https://github.com/jamess010/AIOpen/tree/master/data/CDH)</br>
CDH是Cloudera最成型的发行版本，拥有最多的部署案例。提供强大的部署、管理和监控工具。Cloudera开发并贡献了可实时处理大数据的Impala项目。拥有强大的社区支持，当出现一个问题时，能够通过社区、论坛等网络资源快速获取解决方法。


* [HDP](https://github.com/jamess010/AIOpen/tree/master/data/CDH) </br>
HDP是Hortonworks公司的发行版，它使用了100%开源Apache Hadoop（不拥有任何私有、非开源代码）的唯一提供商。Hortonworks是第一家使用了Apache HCatalog的元数据服务特性的提供商。并且，它们的Stinger开创性地极大地优化了Hive项目。Hortonworks为入门提供了一个非常好的，易于使用的沙盒。Hortonworks开发了很多增强特性并提交至核心主干，这使得Apache Hadoop能够在包括Windows Server和Windows Azure在内的Microsft Windows平台上本地运行,相比于CDH只能运行在Linux系统中。

下图是CDH和HDP的特性比较：</br>
<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/cdh-hdp.png" /></div>

## 算法

* [EcoSystem](https://github.com/tensorflow/ecosystem)</br>
EcoSystem是Tensorflow的生态系统，通过ecosystem可以方便地使tensorflow与docker、hadoop、spark集成分布式计算。

* [Tensorflow on Yarn](https://github.com/linkedin/TonY)</br>
TonY(Tensorflow on Yarn)是LinkedIn的开源项目，允许用户在单个节点或大型 Hadoop 集群上构建基于 YARN 的 TensorFlow 应用程序解决方案。 TonY 的工作方式就像在 Hadoop 中的 MapReduce，执行 Pig 和 Hive 脚本的方法类似，为 TensorFlow 任务提供第一级支持。 TonY 由三个主要组件组成，客户端，ApplicationMaster 和 TaskExecutor。 它提供了 GPU 调度，精确资源请求，TensorBoard 支持和容错的四个主要功能。

* [Spark on Yarn](http://spark.apache.org/)</br>
一般的Spark部署模式是Spark的standalone运行模式。在Spark的生产环境中，主要部署在Hadoop集群中，是以Spark On YARN模式运行，依靠yarn来调度Spark，比默认的Spark运行模式性能要好的多。 Spark on Yarn分为client和cluster两种模式。


## 算力

* 算力中心：
  * 硬件：
    * GPU服务器: 20台高性能的GPU服务器，包含60张GPU卡，1280G内存，95T空间
    * 服务器机架：500台2U刀片服务器架
    * 高性能服务器：40台高性能服务器，2304G内存,207T的空间
    * 交换机：10个以上的万兆交换机

  * 软件：
    * 资源池虚拟化软件系统（OpenStack）
    * 网络管理系统
    * 监控软件系统
    
* 家用：
  * 硬件：
    * CPU：3.5 GHz Intel Core i7
    * 内存：128 GB HDDR 4 3000 MHz
    * 硬盘：3 TB Fusion Drive（1TB SSD + 2TB HDD）
    * GPU：4块 GTX 1080Ti
  * 软件：
    * Ubuntu16.04
    * anaconda2
    * tensorflow
    * keras

---
# 目录说明
- #### data：数据：数据集、数据区块链、Hadoop、Spark等。

- #### algorithm：算法：深度学习算法、训练框架、模型等。

- #### power：算力：GPU、TPU、OpenStack、K8S、docker等。

- #### applications：AI应用：各行业应用，如自动驾驶、人脸识别、声纹提取和识别、语音处理等。

- #### others：一些未分类的资源，学习资源（包括深度学习、区块链、node.js、go、python编程语言等）。
---

# 术语解释

### A

AGI：Artificial General Intelligence，通用人工智能。</br>
AI：Artificial Intelligence，人工智能。</br>
Algorithm：人工智能算法,目前最主流的是深度学习。</br>
ANN：Artificial Neural Networks，人工神经网络</br>
APU：Accelerated Processing Unit，加速处理器，是把CPU和GPU做到一块硅芯上。</br>
Awesome：在Github上寻找好资源的关键字。比如：awesome deep learning, awesome blockchain等。
Auto Encoder：自动编码器，一种无监督学习方法</br>

### B

BC：Block Chain，区块链，是一种在多方无需互信的环境下，通过密码学技术让系统所有参与方协作，共同记录和维护一个可靠的、不可撤销的分布式数据块链的技术。</br>
BDCloud：大数据云平台。https://github.com/bdcloud/data-django-kafka-hdfs-spark </br>
BPU：Brain Processing Unit, 大脑处理器。</br>
BOTs：虚拟（聊天）机器人，是一种通过自然语言来模拟人类对话的程序。</br>

### C

Caffe：Convolutional Architecture for Fast Feature Embedding，是一种常用的深度学习框架，在视频、图像处理方面应用较多</br>
CM：Cloudera Manager， 提供易用特性、易于升级和安装组件等最有价值的功能。CM也可以在几分钟之内建立集群主节点的高可用性（high availability）及其他功能，例如，Hive，Pig，Impala，Flume和Spark等。</br>
CNN：Convolutional Neural Networks，卷积神经网络</br>
CNTK：Computational Network Toolkit，微软开发的深度学习商业工具包。</br>

### D

DBN：Deep Belief Networks，深度置信网络</br>
DL：Deep Learnging，深度学习</br>
DNN：Deep Neural Networks，深度神经网络</br>
Docker：容器</br>
DPU：Deep learning Processing Unit, 深度学习处理器。</br>

### E

EcoSystem：Tensorflow的生态系统，通过ecosystem可以方便地使tensorflow与docker、hadoop、spark集成分布式计算。</br>

### F

Flume：一个分布式、可靠和高可用的海量日志聚合系统，支持在系统中定制各类数据发送方，用于收集数据；同时，Flume提供对数据进行简单处理，并写入各种数据接受方（可定制）的能力。</br>
FPGA：Field-Programmable Gate Array，现场可编程门阵列</br>

### G

GAN：Generative Adversarial Networks，生成式对抗网络，一种最具前景的无监督学习方法</br>
GMM：混合高斯模型</br>
GPU：Graphics Processing Unit，图形处理器</br>

### H

Hadoop：是一个山寨google的分布式文件系统</br>
HBase：建立在Hadoop文件系统之上的分布式面向列的数据库</br>
Hive：基于Hadoop的一个数据仓库工具</br>
HMM：隐马尔可夫模型</br>
Hue：提供了Fusion Insight HD应用的图形化用户Web界面。Hue支持展示多种组件，目前支持HDFS、YARN、Hive和Solr。</br>

### I

Impala：是基于HDFS的SQL工具，cloudera开发，现开源。</br>
IPFS：InterPlanetary File System，星际文件系统，是永久的、去中心化保存和共享文件的方法，这是一种内容可寻址、版本化、点对点超媒体的分布式协议。</br>
IPNS：InterPlanetary Named System，是一个分布式的命名系统，将难于记忆的数据哈希值映射为易于记忆的字符串。这可以类比于域名与IP地址的映射关系。</br>


### K

Kafka：A Distributed Streaming Platform，是一种高吞吐量的分布式发布-订阅消息系统</br>
K8S：Kubernetes</br>
Keras：是一款基于Tensorflow、Theano、CNTK为后端的深度学习高级框架</br>
KG：Knowledge Graph，知识图谱，旨在描述客观世界的概念、实体、事件及其之间的关系。</br>
Kubernetes：容器集群</br>

### L

LSTM：Long Short-Term Memory，长短期记忆网络</br>

### M

Matplotlib：基于Python的数据可视化工具</br>
MFCC：梅尔倒谱系数</br>
ML：Machine Learning，机器学习</br>
MLP：多层感知器</br>
MongoDB：NoSQL数据库</br>
MSE：均方误差</br>

### N

NLP： Natural Language Processing，自然语言处理，是人工智能(AI)的一个子领域。</br>
NPU：Neural network Processing Unit，神经网络处理器。</br>
Numpy：基于Python的基础数据工具</br>

### O

OpenStack：一个开源的云计算管理平台项目</br>
Oozie：提供了对开源Hadoop组件的任务编排、执行的功能。以Java Web应用程序的形式运行在Java servlet容器（如：Tomcat）中，并使用数据库来存储工作流定义、当前运行的工作流实例（含实例的状态和变量）。</br>

### P

PCA 主成分分析</br>
Pandas：Python Data Analysis Library，一个基于Python的数据处理工具</br>
PySpark：一种基于Python的Spark编程接口</br>
Python：一种解释型、面向对象、动态数据类型的高级程序设计语言</br>
PyTorch：一个基于Python的深度学习框架</br>

### R

RBM：Restricted Boltzmann Machines，受限玻尔兹曼机</br>
RL: Reinforcement Learning，强化学习</br>
RNN：Recurrent Neural Networks，循环神经网络</br>
ROS：Robot Operating System，是一个机器人软件平台</br>

### S

Scala：一种Spark编程语言</br>
Slim：Tensorflow的一个辅助工具</br>
Spark：基于内存的分布式计算引擎</br>
Solr：一个高性能，基于Lucene的全文检索服务器。Solr对Lucene进行了扩展，提供了比Lucene更为丰富的查询语言，同时实现了可配置、可扩展，并对查询性能进行了优化，并且提供了一个完善的功能管理界面，是一款非常优秀的全文检索引擎。</br>
Storm：基于流的分布式计算引擎</br>

### T

TF-Slim：Tensorflow的一个辅助工具</br>
Theano：用于深度学习的框架，基于Python</br>
Tensorflow：Google的一款用于深度学习的框架，基于Python</br>
TPU：Tensor Processing Unit，向量处理器，是google的一款高性能处理器</br>

### Y

Yann：集群管理工具</br>

### Z

zookeeper：集群管理工具</br>

---
# 参考资料

#### 人工智能

[Guide to Open Source AI: Projects, Insights, and Trends](https://pan.baidu.com/s/19vu8pzbop9C9ORjkismE5A)

[迁移学习简明手册](https://pan.baidu.com/s/16x7n834vEmL5swsZcgzpUw)

[人工智能标准化白皮书（2018）](https://pan.baidu.com/s/1_MzUDIJcX3b2_slsW5PdzQ)

[深度学习教程【李宏毅】](https://pan.baidu.com/s/1NpjdimyUYX93pZiPm6Y2oA)

[Natural Language Processing](https://github.com/jacobeisenstein/gt-nlp-class/tree/master/notes)

[“世界模型”代码，实现无监督方式快速训练](https://github.com/hardmaru/WorldModelsExperiments)

#### 区块链

[区块链技术](http://www.ContentBC.com)

[2018中国区块链产业白皮书](https://pan.baidu.com/s/17jGDJVDty0MNS-9o9s6ovA)

[企业以太坊客户端规范1.0](https://pan.baidu.com/s/1HVmeyml6VRHnGdzxQJUcag)

[以太坊（Ethereum）白皮书](https://github.com/ethereum/wiki/wiki/%5B%E4%B8%AD%E6%96%87%5D-%E4%BB%A5%E5%A4%AA%E5%9D%8A%E7%99%BD%E7%9A%AE%E4%B9%A6)

[超级账本Hyperledger白皮书](https://pan.baidu.com/s/1aHKtra7O-0FgywsCh5AbkQ)

[区块链行业词典](https://pan.baidu.com/s/1iYS28E49T2ts7kX3tzn1gA)

[区块链教程【黑马程序员120天全栈区块链开发开源教程】](https://github.com/itheima1/BlockChain)

#### 大数据

[大数据标准化白皮书（2018）](https://pan.baidu.com/s/1i5EGSjifQDScvWOOv6UfrA)

[2018年中国大数据发展调查报告](https://pan.baidu.com/s/1gW4WrgmFqjCkebaZdIYLGw)

#### 其它

[国密算法规范-SM2/SM3/SM4/SM9](https://pan.baidu.com/s/1kL2uAUdOfnDWuSD-JBeJDw)


---

# 联系我们

### 欢迎任何反馈、建议和贡献
- #### Website：http://www.aiopens.net
- #### E-mail：jamess@126.com
- #### 微信扫描下方二维码，关注“AIOpens”公众号
<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/aiopens_weixin.jpg" /></div>
