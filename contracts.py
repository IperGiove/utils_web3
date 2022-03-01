import pathlib
import json


class Contracts:
    path = pathlib.Path(__file__).parent.resolve()
    
    def __load_abi(self, token: str) -> json:
        with open(f'{self.path}/ABI/{token}_abi.json') as data:
            abi = json.load(data)
        return abi
        
    def chz(self) -> dict:
        """CHZ CONTRACT"""
        return {'address': '0x3506424F91fD33084466F402d5D97f05F8e3b4AF', 
                'abi': self.__load_abi('chz')}
        
    def dai(self) -> dict:
        """DAI CONTRACT"""
        return {'address': '0x6B175474E89094C44Da98b954EedeAC495271d0F', 
                'abi': self.__load_abi('dai')}
        
    def eurn(self) -> dict:
        """EURN CONTRACT"""
        return {'address': '0x9fcf418B971134625CdF38448B949C8640971671', 
                'abi': self.__load_abi('eurn')}
        
    def fdz(self) -> dict:
        """FDZ CONTRACT"""
        return {'address': '0x23352036E911A22Cfc692B5E2E196692658ADED9', 
                'abi': self.__load_abi('fdz')}
        
    def gusd(self) -> dict:
        """GUSD CONTRACT"""
        return {'address': '0x056Fd409E1d7A124BD7017459dFEa2F387b6d5Cd', 
                'abi': self.__load_abi('gusd')}
        
    def link(self) -> dict:
        """LINK CONTRACT"""
        return {'address': '0x514910771AF9Ca656af840dff83E8264EcF986CA', 
                'abi': self.__load_abi('link')}
        
    def mana(self) -> dict:
        """MANA CONTRACT"""
        return {'address': '0x0F5D2fB29fb7d3CFeE444a200298f468908cC942', 
                'abi': self.__load_abi('mana')}
        
    def noku(self) -> dict:
        """NOKU CONTRACT"""
        return {'address': '0x8167D3B1024cB51A2DD1B4d889ddf7023420796a', 
                'abi': self.__load_abi('noku')}
        
    def phi(self) -> dict:
        """PHI CONTRACT"""
        return {'address': '0x13C2fab6354d3790D8ece4f0f1a3280b4A25aD96', 
                'abi': self.__load_abi('phi')}
        
    def sand(self) -> dict:
        """SAND CONTRACT"""
        return {'address': '0x3845badAde8e6dFF049820680d1F14bD3903a5d0', 
                'abi': self.__load_abi('sand')}
        
    def seed(self) -> dict:
        """SEED CONTRACT"""
        return {'address': '0x5a30b9D5DF526E3Ff1517497A8FaE401Fb28a712', 
                'abi': self.__load_abi('seed')}
        
    def uni(self) -> dict:
        """UNI CONTRACT"""
        return {'address': '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984', 
                'abi': self.__load_abi('uni')}
        
    def usdc(self) -> dict:
        """USDC CONTRACT"""
        return {'address': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 
                'abi': self.__load_abi('usdc')}
        
    def usdt(self) -> dict:
        """USDT CONTRACT"""
        return {'address': '0xdAC17F958D2ee523a2206206994597C13D831ec7', 
                'abi': self.__load_abi('usdt')}
        
    
        
    
        
