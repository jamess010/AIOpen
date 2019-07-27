// 定义 web3 库

var Web3 = require('web3');

// 链接以太网络
web3 = new Web3( new Web3.providers.HttpProvider("http://localhost:9545") );

console.log("Account Tranaction!!!");

// 账号 0 转账到账号 1
web3.eth.getAccounts(function(error, accounts) {
	if(error) {
		console.log(error);
	}
	
	let txnObject = {from:accounts[0],to:accounts[1],value:web3.utils.toWei('3','ether')};

	web3.eth.sendTransaction(txnObject, function(error, result){
		if(error){
			console.log( "Transaction error" ,error);
		}
		else{
			var txn_hash = result; //Get transaction hash
			console.log("trans_hash:",txn_hash);
		}
	});
		

});

