import pytest
from brownie import network, accounts, exceptions

from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_deploy_fund_and_withdraw():
    account = get_account()
    # deploy
    fund_me = deploy_fund_me()
    assert fund_me  # assert that is object

    # funding
    entrance_fee = fund_me.getEntranceFee() + 100
    tx_fund = fund_me.fund({"from": account, "value": entrance_fee})
    tx_fund.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee  # check that the funds have been added

    # withdrawing
    tx_withdraw = fund_me.withdraw({"from": account})
    tx_withdraw.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0  # that all funds haev been withdrawn


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local environment testing")
    fund_me = deploy_fund_me()  # deployed from: account = get_account()
    assert fund_me  # assert that is object

    # attemp withdrawal
    bad_actor = accounts.add()
    # expect an exception

    with pytest.raises(ValueError):
        fund_me.withdraw({"from": bad_actor})
