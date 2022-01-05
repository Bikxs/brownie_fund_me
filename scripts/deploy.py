from brownie import FundMe, MockV3Aggregator, network, config


from scripts.helpful_scripts import get_account, deploy_mocks,LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_simple_storage():
    print("Deploying simple storage..")
    account = get_account()
    print(f"account: {account}")
    # need to pass the price feed address
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        mockV3Aggregator = MockV3Aggregator[-1]
        price_feed_address = mockV3Aggregator.address
    fund_me = FundMe.deploy(price_feed_address, {"from": account},
                            publish_source=config["networks"][network.show_active()].get("verify"))
    print("Contract:", fund_me)


def main():
    deploy_simple_storage()
