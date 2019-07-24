# 本项目建立一个私有链，并使用浏览器查看区块链信息
运行步骤：

1) docker-compose up 
2) 在浏览器中输入：http://localhost:8000
3) 可以查看私有链信息
4) 运行 ./run_client.sh, 可以使用命令操作区块链

# 常用命令
1) 创建账号

personal.newAccount("123456")

personal.newAccount("123456")

2）解锁coinbase账号

web3.eth.coinbase 

web3.eth.accounts[0]

personal.unlockAccount(web3.eth.accounts[0],"123456")

3) 查看账号余额

web3.eth.getBalance(web3.eth.accounts[0])

web3.eth.getBalance(web3.eth.accounts[1])

4）开始挖矿

miner.start()

结束挖矿:

miner.stop()    

5）基本账号转账5个ether币给第二个账户

web3.eth.sendTransaction({from:web3.eth.accounts[0],to:web3.eth.accounts[1],value:web3.toWei(5,'ether')})

6) 区块链高度

eth.blockNumber

7) 返回0块信息

eth.getBlock(0)

8） 交易缓冲池

txpool

txpool.content

9) 查看是否挖矿

eth.mining 
