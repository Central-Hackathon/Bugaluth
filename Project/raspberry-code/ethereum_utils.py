from web3 import Web3, HTTPProvider
from pprint import pprint
import json

WEB3_PROVIDER_URL = 'http://localhost:7545'
# WEB3_PROVIDER_URL = 'http://192.168.223.93:7545'

class BlockchainManager:

    def __init__(self):
        # make a connection with a node
        self.web3 = Web3(HTTPProvider(WEB3_PROVIDER_URL))

        # test the connection
        pprint(self.web3.eth.accounts)
        with open('EcoChainTokenDemo.json', 'r') as f:
            artifacts = json.load(f)
            # print(artifacts['abi'])
            self.myContract = self.web3.eth.contract(
            address=self.web3.toChecksumAddress("0x5b8a8f7118e5b96ccf79c7bff4e1ba5aada5a243"),
            abi=artifacts['abi'])
            # print(self.myContract.functions.totalSupply().call())

    def reward(self, address, number_of_items):
        address = self.web3.toChecksumAddress(address)
        self.myContract.functions.reward(address, number_of_items).transact({'from': self.web3.eth.accounts[0]})
        # print(self.myContract.functions.balanceOf(address).call())

if __name__=="__main__":
    bManager = BlockchainManager()
    # print(bManager.web3.eth.accounts[4])
    bManager.reward(bManager.web3.eth.accounts[4], 10)
