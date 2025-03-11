import uuid
from decimal import Decimal

from bank_system.normal.domain.transaction import Transaction
from bank_system.normal.domain.transaction_type import TransactionType
from bank_system.normal.exceptions.insufficient_balance_error import InsufficientBalanceError
from bank_system.normal.exceptions.negative_amount_error import NegativeAmountError


class Client:

    def __init__(self, name):
        self._uuid = uuid.uuid4()
        self._name: str = name
        self._balance = Decimal('0')
        self._transactions: [Transaction] = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: Decimal):
        if amount < 0:
            raise NegativeAmountError(amount)
        self._balance += amount
        self._transactions.append(Transaction(self._name, TransactionType.DEPOSIT, amount))

    def withdraw(self, amount: Decimal):
        if amount < 0:
            raise NegativeAmountError(amount)
        elif amount > self._balance:
            raise InsufficientBalanceError(self._balance, amount)
        self._balance -= amount
        self._transactions.append(Transaction(self._name, TransactionType.WITHDRAW, amount))

    def print_statement(self):
        print(f"\nTransaction statement for {self._name}:")
        print("Date\t\t\t\t\t\tAmount\tType")
        print("-" * 40)
        for transaction in self._transactions:
            print(transaction)

    def __eq__(self, other):
        if isinstance(other, Client):
            return self._uuid == other._uuid
        return False

    def __hash__(self):
        return hash(self._uuid)

    def __str__(self):
        return f"Client: {self._name} | {self._balance}"

    def __repr__(self):
        return (f"Client(uuid={repr(self._uuid)}, name={repr(self._name)}, "
                f"balance={repr(self._balance)}, transactions={repr(self._transactions)})")
