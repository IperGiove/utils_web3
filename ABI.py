from web3 import Web3
from contracts import contracts


class ABI(contracts):
    def __init__(self) -> None:
        self.initialized_stored_contracts()
        
    def __check_stored_contracts(self, token: str) -> None:
        if token not in self.__stored_contracts.keys():
            self.__stored_contracts[token] = self.__load_contract(
                getattr(self, token)()
            )
        
    def __load_contract(self, contract: dict) -> Web3:
        return self.w3.eth.contract(address=contract['address'], 
                                    abi=contract['abi'])
        
    def initialized_stored_contracts(self) -> None:
        self.__stored_contracts = {}
        
    def contract(self, token: str) -> None:
        self.__check_stored_contracts(token.lower())
        return self.__stored_contracts[token.lower()]
        
    
