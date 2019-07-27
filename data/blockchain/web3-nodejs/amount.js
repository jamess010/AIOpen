// 定义 web3 库

var Web3 = require('web3');

// 链接以太网络
web3 = new Web3( new Web3.providers.HttpProvider("http://localhost:9545") );

console.log("Dispaly Account Msg!!!");

// 获取所有账号
web3.eth.getAccounts(function(error, accounts) {
	if(error) {
		console.log(error);
	}
	// 显示账号 0 的金额
	web3.eth.getBalance(accounts[0]).then(function(result){
		console.log( "Account 0 Balance : " ,web3.utils.fromWei(result, 'ether'));
	});
	
	// 显示账号 1 的金额
	web3.eth.getBalance(accounts[1]).then(function(result){
		console.log( "Account 1 Balance : " ,web3.utils.fromWei(result, 'ether'));
	});

});

