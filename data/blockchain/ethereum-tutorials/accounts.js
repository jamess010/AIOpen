// 定义 web3 库

var Web3 = require('web3');

// 链接以太网络
web3 = new Web3( new Web3.providers.HttpProvider("http://localhost:9545") );


// 获取node信息
web3.eth.getNodeInfo().then((value)=>{console.log(value)});

// 显示所有账号
web3.eth.getAccounts().then((value)=>{

        var accounts = value;
        
	console.log("All Accounts:", accounts);
});


