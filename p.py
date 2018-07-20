!pip install web3
from web3 import Web3, HTTPProvider 

w3 = Web3(HTTPProvider("https://sokol.poa.network"))

print(w3.eth.getBlock(w3.eth.blockNumber)) 
print(w3.eth.getBlock(w3.eth.blockNumber - 1)) 
print(w3.eth.getBlock(w3.eth.blockNumber - 2))
print(w3.eth.getBalance('0x2B3Dde79Cd603c43d2dCb472e29E31288B3c9311'))
