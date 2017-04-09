# Sliding window protocol
Implementation of sliding window protocol in python, for Computer Networks Assignment

## Requirements
1. Python 2.7
2. Git

## Installation
1. Clone the repo to a directory of your choice
```bash
git clone https://github.com/sidharthv96/Implementation-of-sliding-window-protocol
```
2. Open two shells to run server and client seperately
3. Run `python server.py` in first shell 
4. Run `python client.py` in second shell

## Noisy and Noiseless channels
Inorder to simulate a noisy channel, I have implemented a condition that has 20% chance of failure in both server and client.
So, only 80% of Data/ACK are being sent to simulate to packet loss in noisy channels.
To run the code in a Noiseless enviorment, Change `0.8` in `if random() < 0.8:` to `2` as it will ensure 100% success rate.


## Outputs
Both noisy and noiseless simulation have been done and the Outputs of server and client have been saved as shown



| Type | Client | Server |
| ---  | ------ | ------ |
| Noisy | client.log | server.log |
| Noiseless | noiseless_c.log | noiseless_s.log |

