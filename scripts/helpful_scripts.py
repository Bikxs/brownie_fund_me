from brownie import MockV3Aggregator
from brownie import accounts, config, network
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    account = get_account()
    if len(MockV3Aggregator) <= 0:
        print(f"Deploying mocks...")
        print(f"\tDeploying MockV3Aggregator...")
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": account})
        print(f"Mocks deployed")

