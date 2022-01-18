// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract Counter {
    int public count;

    // Function to get the current count
    function get() public view returns (int) {
        return count;
    }

    // Function to increment count by 1
    function inc() public {
        count += 1;
    }

    // Function to decrement count by 1
    function dec() public {
        count -= 1;
    }
}
