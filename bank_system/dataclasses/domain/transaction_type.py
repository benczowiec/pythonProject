from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"

    def __str__(self):
        return self.value