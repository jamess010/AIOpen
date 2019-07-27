// 定义 web3 库

var Web3 = require('web3');

// 链接以太网络
web3 = new Web3( new Web3.providers.HttpProvider("http://localhost:9545") );


// 获取node信息
web3.eth.getNodeInfo().then((value)=>{console.log(value)});

// var accounts;
// 获取所有账号到 accounts (list)
let accounts = web3.eth.getAccounts().then((value)=>{accounts=value;console.log(accounts)});

// 显示所有账号
web3.eth.getAccounts().then((value)=>{console.log(value[0])});

// 显示账号 0 的金额
web3.eth.getBalance(accounts[0]).then((value) => {console.log(value)});

// 显示账号 1 的金额
web3.eth.getBalance(accounts[1]).then((value) => {console.log(value)});

// 账号 0 转账到账号 1
web3.eth.sendTransaction({from:accounts[0],to:accounts[1],value:web3.utils.toWei('30','ether')}).then((value)=>{console.log(value)});

