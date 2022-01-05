from brownie import FundMe

from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def fund():
    if not FundMe:
        deploy_fund_me()
    fund_me = FundMe[-1]
    account = get_account()


def withdrawy():
    account = get_account()
    FundMe.deploy({"from": account})


def main():
    fund()
