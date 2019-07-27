1) 启动 ganache
2）配置端口
3）将server hostname 设置为 0.0.0.0-All Interface

// 定义 web3 库

var Web3 = require('web3');

// 链接以太网络
web3 = new Web3( new Web3.providers.HttpProvider("http://localhost:9545") );


// 获取node信息
web3.eth.getNodeInfo().then((value)=>{console.log(value)});

