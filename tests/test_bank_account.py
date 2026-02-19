import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)

def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_initial_balance_negative():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-10)

def test_deposit_negative_or_zero(start_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        start_account.deposit(-20)

def test_withdraw_success(start_account):
    start_account.withdraw(40)
    assert start_account.balance == 60

def test_withdraw_insufficient_funds(start_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        start_account.withdraw(200)

def test_withdraw_negative_or_zero(start_account):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        start_account.withdraw(-10)

def test_transfer_success(start_account):
    target = BankAccount(0)
    start_account.transfer_to(target, 50)
    assert start_account.balance == 50
    assert target.balance == 50

def test_transfer_invalid_target(start_account):
    with pytest.raises(ValueError, match="Target must be a BankAccount"):
        start_account.transfer_to("not an account", 30)
