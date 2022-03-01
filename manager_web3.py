from web3 import Web3
from ABI import ABI

class ManagerWeb3(ABI):
    def __init__(self, provider):
        self.__save_provider(provider)
        self.__connection()
        self.initialized_stored_contracts()
                
    def __save_provider(self, provider) -> None:
        self.__check_provider(provider)
        self.provider = provider

    def __check_provider(self, provider) -> None:
        assert 'http' not in provider or 'ws' not in provider, "set a provider equal to 'http' or 'ws'" 
             
    def __connection(self) -> None:
        if 'http' in self.provider:
            self.w3 = Web3(Web3.HTTPProvider(self.provider))
        elif 'ws' in self.provider == 'ws':
            self.w3 = Web3(Web3.WebsocketProvider(self.provider))
    
    def check_connection(self) -> None:
        print(self.w3.isConnected())
        
    def check_sum_address(self, address:str) -> str:
        return self.w3.toChecksumAddress(address)
        
    def get_balance_eth(self, address) -> float:
        address_checked = self.check_sum_address(address)
        return self.w3.fromWei(self.w3.eth.get_balance(address_checked), 'ether')
         
    def get_balance_token(self, token:str, address:str) -> float:
        address_checked = self.check_sum_address(address)
        return self.contract(token).functions.balanceOf(address_checked).call() /\
               10 ** self.contract(token).functions.decimals().call()
        

if __name__ == '__main__':
    manager_w3 = ManagerWeb3(provider='https://mainnet.infura.io/v3/xxxx')
    
    print(manager_w3.get_balance_eth('address'))
    print(manager_w3.get_balance_token('usdt','address'))
