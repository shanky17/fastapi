import pytest

from app.calculations import BankAccount, InsufficientFunds, add, div, modulo, mul, sub


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("input1, input2, output", [(2, 3, 5), (4, 5, 9), (12, 4, 16)])
def test_add(input1, input2, output):
    print("Testing add function")
    assert add(input1, input2) == output, "Add function failed"


def test_sub():
    assert sub(9, 4) == 5, "Sub function failed"


def test_mul():
    assert mul(2, 3) == 6, "Mul function failed"


def test_div():
    assert div(10, 5) == 2, "Div function failed"


def test_mod():
    assert modulo(5, 2) == 1, "Modulo function failed"


def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0


def test_bank_set_init_amount(bank_account):
    assert bank_account.balance == 50


def test_bank_deposit_amount(bank_account):
    bank_account.deposit(100)
    assert bank_account.balance == 150


def test_bank_withdraw_amount(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_bank_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize(
    "deposit, withdraw, balance",
    [(100, 20, 80), (50, 10, 40), (1000, 750, 250)],
)
def test_bank_transactions(zero_bank_account, deposit, withdraw, balance):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    zero_bank_account.balance == balance


def test_insufficient_fund(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
