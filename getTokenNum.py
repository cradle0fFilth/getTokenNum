from web3 import Web3
import config
import time
import erc20

#连接bsc网络
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

#输入要买币种的余额
token = web3.toChecksumAddress("0x55d398326f99059ff775485246999027b3197955")

#输入要查询的地址
my = web3.toChecksumAddress(config.sender_addr)

#创建合约实体
erc_20_contract = web3.eth.contract(address = token, abi = erc20.contract) 

symbol = erc_20_contract.functions.symbol().call()
token_balance = erc_20_contract.functions.balanceOf(my).call()
token_balance = web3.fromWei(token_balance,'ether')
print(f"{my} have {token_balance} of {symbol} tokens")