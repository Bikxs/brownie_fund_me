from brownie import FundMe

from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def fund():
    if not FundMe:
        deploy_fund_me()
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()+100
    print(f"entrance_fee: {entrance_fee}")
    print("Funding the account...")
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"Funds added: {entrance_fee}")


def withdraw():
    if not FundMe:
        deploy_fund_me()
    fund_me = FundMe[-1]
    account = get_account()
    print("With drawing account...")
    fund_me.withdraw({"from": account})
    print(f"Funds withdrawn")


def main():
    fund()
    withdraw()
