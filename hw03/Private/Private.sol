/**
 *Submitted for verification at Etherscan.io on 2020-10-22
*/

// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract Private {
    string private flag;

    constructor (string memory _flag) {
        flag = _flag;
    }
}
