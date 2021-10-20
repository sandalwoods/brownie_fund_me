from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

FORK_LOCAL_ENVIORNMENTS = ["mainnet-fork-dev", "mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORK_LOCAL_ENVIORNMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        # MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from": get_account()})
        MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": get_account()})
    print("Mocks Deployed")