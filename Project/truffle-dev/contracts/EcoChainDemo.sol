pragma solidity ^0.4.19;


import "./StandardToken.sol";


contract EcoChainTokenDemo is StandardToken {

    address[] private users;
    mapping(address => bool) isRegistered;

    constructor () public {
      balances[msg.sender] = 10000;
      totalSupply_ = totalSupply_ + 10000;
    }

    function getUsers() public view returns (address[]) {
        return users;
    }

    function reward(address _to, uint256 _items) public returns(bool) {

        uint256 numberOfTokens = _items*10;

        if (transfer(_to, numberOfTokens) == true) {

            if(!isRegistered[_to])
              users.push(_to);

           return true;
        }

        return false;
    }

    function getBalanceOf(address _to) public view returns (uint, address) {
      uint bal = balanceOf(_to);
      return (bal, _to);
    }
}
