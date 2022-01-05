from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def test_can_deploy_fund_and_withdraw():
    account = get_account()
    # deploy
    fund_me = deploy_fund_me()
    assert fund_me # assert that is object

    # funding
    entrance_fee = fund_me.getEntranceFee() + 100
    tx_fund = fund_me.fund({"from": account, "value": entrance_fee})
    tx_fund.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee #check that the funds have been added

    # withdrawing
    tx_withdraw = fund_me.withdraw({"from": account})
    tx_withdraw.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0  # that all funds haev been withdrawn
