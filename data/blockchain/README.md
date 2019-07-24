# 本地文件说明
[ethereum-explorer](https://github.com/jamess010/ethereum-explorer)：一个docker实现的ehereum私有链，并通过浏览器查看区块链</br>
bc_ex2.ipynb：6步使用python玩转区块链</br>
encrypt.ipynb：使用PyCrypto库实现的MD5、SHA-256、SHA-512、RIPEMD160.
pycrypto：安装了PyCrypto库的docker，包括MD5、SHA-1、SHA-2、RIPEMD-160、DES、AES、RSA等。</br>
CryptoJS：javascript实现的前端哈希算法，包括：MD5、SHA-256、SHA-512、RIPEMD167.</br>

---

# 区块链资源列表

PyCrypto：一个极好的信息安全python库，包括MD5、SHA-1、SHA-2、RIPEMD-160、DES、AES、RSA等。</br>
地址：https://github.com/dlitz/pycrypto

CryptoJS：一个javascript前端加密库，包括：MD5、SHA2、SHA3、RIPEMD160等。</br>
地址：https://code.google.com/archive/p/crypto-js/downloads


ipfs：A peer-to-peer hypermedia protocol to make the web faster, safer, and more open.</br>
地址：https://github.com/ipfs/ipfs

gx：ipfs的可用于所有软件的带版本的包管理器。</br>
地址：https://github.com/whyrusleeping/gx

Sia：是一个去中心化的云存储平台，文件被切成小块，加密存储到分布式的网络里面。</br>
地址：https://github.com/NebulousLabs/Sia

把区块链技术，智能合约和机器学习结合在一起的代码。</br>
地址：https://github.com/thoschm/START-Summit-2017-Blockchain-Machine-Learning-Workshop

danku：是Algorithmia公司推出基于区块链的机器学习合约。是一个可以评估被提交模型的神经网络，以太币奖励获胜者。</br>
地址：https://github.com/algorithmiaio/danku

收集所有区块链(BlockChain)技术开发相关资料，包括Fabric和Ethereum开发资料。</br>
地址：https://github.com/chaozh/awesome-blockchain-cn

blockchain：一个比较全的区块链中文资源列表。</br>
地址：https://github.com/LiuBoyu/blockchain

区块链指南：https://github.com/yeasy/blockchain_guide

Hyperledger 源码分析之 Fabric。</br>
地址：https://github.com/yeasy/hyperledger_code_fabric

cello：Blockchain Management Platform。区块链管理平台。</br>
地址：https://github.com/hyperledger/cello

## 主流区块链技术

#### 区块链1.0

BitCoin：比特币区块链的核心技术框架采用C++语言开发，共识算法采用POW算法，工作量（挖矿）证明获得记账权，容错50%，实现全网记账，公网性能TPS<7。</br>
地址：https://github.com/bitcoin/bitcoin

---

#### 区块链2.0

ETH：以太坊是一个图灵完备的区块链一站式开发平台，采用多种编程语言实现协议，采用GO语言写的客户端作为默认客户端（即与以太坊网络交互的方法, 支持其他多种语言的客户端）。基于以太坊平台之上的应用是智能合约，这是以太坊的核心。智能合约配合友好的界面和外加一些额外的小支持，可以让用户基于合约搭建各种千变万化的DApp应用，这样使得开发人员开发区块链应用的门槛大大降低。TPS<25。</br>
地址：https://github.com/ethereum/

Hyperledger fabric：是IBM力推的区块链开发平台，主要用于联盟链的开发，是目前普及度最高的联盟链开发平台。TPS<100k。</br>
地址：https://github.com/hyperledger/fabric

---

## 其它

Elements：是Blockstream的开源侧链项目，同样使用比特币双向挂钩技术，除了智能合约外，他还给比特币快速带来许多创新技术，包括私密交易、证据分离、相对锁定时间、新操作码、签名覆盖金额等等特性。核心技术框架采用C++语言开发。</br>
地址：https://github.com/ElementsProject/elements

Factom：利用比特币的区块链技术来革新商业社会和政府部门的数据管理和数据记录方式，也可以被理解为是一个不可撤销的发布系统，系统中的数据一经发布，便不可撤销，提供了一份准确、可验证、且无法篡改的审计跟踪记录。利用区块链技术帮助各种各样应用程序的开发，包括审计系统，医疗信息记录，供应链管理，投票系统，财产契据，法律应用，金融系统等。GO开发，TPS：27。</br>
地址：https://github.com/FactomProject/FactomCode

Ripple：是世界上第一个开放的支付网络，是基于区块连的点到点全球支付网络。通过这个支付网络，使你轻松、廉价并安全的把你的金钱转账到互联网上的任何一个人，无论他在世界的哪个地方，他可以转账任意一种货币，包括美元、欧元、人民币、日元或者比特币，简便易行快捷，交易确认在几秒以内完成，交易费用几乎是零，没有所谓的跨行异地以及跨国支付费用。C++开发，TPS<100。</br>
地址：https://github.com/ripple/rippled

Nxt、Nextcoin：是第二代去中心化虚拟货币，它使用全新的代码编写，不是比特币的山寨币。它第一个采用100%的股权证明POS算法，有资产交易、任意消息、去中心化域名、帐户租赁等多种功能，部分实现了透明锻造功能。JAVA开发，TPS<1000。</br>
地址：https://bitbucket.org/JeanLucPicard/nxt/overview

Sawtooth Lake：目前是用于建造、部署和运行分布式账本的高度模块化平台，重点领域在数字资产，在锯齿湖的数据模型和交易事务语言中，是由称为“transaction family”的体系来实现的, 給用户可以有开箱即用的功能齐全的市场数字资产管理体系。采用PoET和Quorum Voting两种共识算法，框架核心开发语言Python。</br>
地址：https://github.com/intelledger

布比区块链，目前采用的是对联盟链内定向开源，共识算法采用自研发的Pool验证池，可以集成Byzantine Paxos、Byzantine、Raft等商用共识算法，实现免Gas费用的秒级共识验证，框架核心开发语言是C++，应用场景比较广泛。</br>

小蚁区块链：采用改进的拜占庭容错算法-dBFT共识算法，支持智能合约，目前重点领域在数字资产应用，框架核心开发语言C#。</br>
地址：https://github.com/antshares/antshares

Neblio 是给企业或者机构提供区块链解决方案的技术平台。</br>
地址：https://nebl.io/

Zilliqa：是一个新的区块链平台，每秒可处理数千个交易，并且内置分片。通过分片，Zilliqa 可以匹配传统支付方式（如VISA和MasterCard）设置的吞吐量基准。更重要的是，Zilliqa 的交易吞吐量随其网络规模（大致）线性增加。</br>
地址：https://github.com/Zilliqa/Zilliqa

Storj：是基于 blockchain 技术和点对点协议来提供最安全，私有和加密的云存储。 </br>
地址：https://github.com/storj

RChain：是一个去中心化的、经济的、抵制审查的公共计算基础设施和区块链。它将主持并执行通常被称为“智能合约”的计划。这将是可信的、可扩展的、并行的，具有POS共识和内容交付。</br>
地址：https://github.com/rchain/rchain

BCOS：BlockChainOpenSource，是一个完全开源的区块链底层技术平台，由深圳前海微众银行股份有限公司、上海万向区块链股份公司、矩阵元技术（深圳）有限公司三方共同研发。</br>
地址：https://github.com/bcosorg/bcos

一个非常简单，不大安全，不太完整的用Python编写的加密货币区块链实现。</br>
地址：https://github.com/cosme12/SimpleCoin

python编写的区块链解析器Blockchain parser。</br>
地址：https://pypi.org/project/blockchain-parser/

区块链的简单理解以及python的简单实现(https://blog.csdn.net/luokezhen/article/details/79436942)。</br>
地址：https://github.com/luokezhen/lkz/tree/master/%E5%8C%BA%E5%9D%97%E9%93%BE 

AI+区块链写码全过程。</br>
地址：https://github.com/llSourcell/blockchain_consensus

基于区块链的积分系统。</br>
地址：https://github.com/echplus/bc_pointsplatform

以太坊python实现。</br>
地址：https://github.com/ethereum/pyethapp

超块链：是一种区块链技术，支持多币多账本，无基础币，不依赖特定账本，对跨链交易、非金融业务有更好的支持。 </br>
地址：https://github.com/HyperBlockChain

----
#### 几大主流开源技术的比较：
<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/bc-compare.png" width="700" height="350" /></div>
</br>

#### 共识机制比较：
<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/bt_compare2.png" width="700" height="350" /></div>
</br>

---

#### 区块链思维导图
<div align=center><img src="https://github.com/jamess010/AIOpen/blob/master/pic/bc-2.jpg" width="700" height="350" /></div>
</br>

