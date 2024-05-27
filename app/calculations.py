def add(num1: int, num2: int):
    return num1 + num2


def sub(num1: int, num2: int):
    return num1 - num2


def mul(num1: int, num2: int):
    return num1 * num2


def div(num1: int, num2: int):
    return num1 / num2


def modulo(num1: int, num2: int):
    return num1 % num2


class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, starting_balance: float = 0.0):
        self.balance = starting_balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds in the account")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1  # 10% interest
