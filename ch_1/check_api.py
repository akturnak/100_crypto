from web3 import Web3
import os

infura_url = os.getenv("INFURA_URL")
client_web3 = Web3(Web3.HTTPProvider(infura_url))

print(client_web3.isConnected())
print(client_web3.eth.blockNumber)

balance = client_web3.eth.getBalance(os.getenv("ETH_ADDRESS"))
print(balance)
print(client_web3.toWei(balance, "ether"))
