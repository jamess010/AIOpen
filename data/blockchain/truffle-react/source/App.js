import React, { Component } from "react";
import SimpleStorageContract from "./contracts/SimpleStorage.json";
import getWeb3 from "./utils/getWeb3";

import "./App.css";

class App extends Component {
  state = { storageValue: 0, web3: null, accounts: null, contract: null };

  componentDidMount = async () => {
    try {
      // Get network provider and web3 instance.
      const web3 = await getWeb3();

      // Use web3 to get the user's accounts.
      const accounts = await web3.eth.getAccounts();

      // Get the contract instance.
      const networkId = await web3.eth.net.getId();
      const deployedNetwork = SimpleStorageContract.networks[networkId];
      const instance = new web3.eth.Contract(
        SimpleStorageContract.abi,
        deployedNetwork && deployedNetwork.address,
      );

      // Set web3, accounts, and contract to the state, and then proceed with an
      // example of interacting with the contract's methods.
      this.setState({ web3, accounts, contract: instance }, this.runExample);
    } catch (error) {
      // Catch any errors for any of the above operations.
      alert(
        `Failed to load web3, accounts, or contract. Check console for details.`,
      );
      console.error(error);
    }
  };

  runExample = async () => {
    const { accounts, contract } = this.state;
    console.log({ from: accounts[0] });
    console.log(contract);
    // Stores a given value, 5 by default.
//    await contract.methods.set(333).send({ from: accounts[0] }).then(()=>{console.log("+++++")})
//    await contract.methods.set(333).send({ from: "0xdCEbFFc0C60589e9d42135b4Ee58030585581677" }).then(()=>{console.log("+++++")})
// 0xde560d0fac79e7d35e58bbf3bb2f138586975ecc
    // Get the value from the contract to prove it worked.
    const response = await contract.methods.get().call();

    // Update state with the result.
    this.setState({ storageValue: response });


  };

  render() {
    if (!this.state.web3) {
      return <div>Loading Web3, accounts, and contract...</div>;
    }
    return (

      <div className="App">
        <h1>Good to Go!</h1>
        <p>Your Truffle Box is installed and ready.</p>
        <h2>Smart Contract Example</h2>
        <p>
          If your contracts compiled and migrated successfully, below will show
          a stored value of 5 (by default).
        </p>
        <p>
          Try changing the value stored on <strong>line 40</strong> of App.js.
        </p>
        <div>The stored value is: {this.state.storageValue}</div>

        <input
          ref="dataInput"
          style={{width:200,height:30}}/>

        <button
          onClick={()=>{
            var value = this.refs.dataInput.value;
            const { accounts, contract } = this.state;
            var account = accounts;

  //          contract.methods.set(Number(value)).send({ from: "0xdCEbFFc0C60589e9d42135b4Ee58030585581677" }).then((value)=>{
              contract.methods.set(Number(value)).send({ from: accounts[0] }).then((value)=>{
              console.log("数据修改成功", value);
              contract.methods.get().call().then((value)=>{
                console.log("修改后数据",value)
                this.setState({ storageValue: value })

              });

          })

        }}

          style={{width:100,height:30}}>修改</button>

      </div>


    );
  }
}

export default App;
