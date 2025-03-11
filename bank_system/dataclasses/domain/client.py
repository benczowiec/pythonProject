import uuid
from dataclasses import field
from decimal import Decimal

from bank_system.dataclasses.domain.transaction_type import TransactionType
from bank_system.dataclasses.exceptions.insufficient_balance_error import InsufficientBalanceError
from bank_system.dataclasses.exceptions.negative_amount_error import NegativeAmountError
from bank_system.normal.domain.transaction import Transaction


class Client:
    _uuid: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
    _name: str
    _balance: Decimal = field(default_factory=lambda: Decimal('0'), init=False)
    _transactions: list[Transaction] = field(default_factory=list, init=False)

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

    def __str__(self):
        return f"Client: {self._name} | {self._balance}"
