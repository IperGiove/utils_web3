# Utils for Web3
Python library to manage some fuctions of web3

# Functins
- Eth balance for single address
- Token balance for single address

### Example
```python
from manager_web3 import ManagerWeb3
manager_w3 = ManagerWeb3(provider='https://mainnet.infura.io/v3/xxxx')

print(eth balance: ', manager_w3.get_balance_eth('0xdAC17F958D2ee523a2206206994597C13D831ec7'))
print('usdt balance: ', manager_w3.get_balance_token('usdt','0xdAC17F958D2ee523a2206206994597C13D831ec7'))
```

