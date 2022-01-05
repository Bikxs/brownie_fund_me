from brownie import FundMe

from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()


def withdrawy():
    account = get_account()
    FundMe.deploy({"from": account})


def main():
    fund()
