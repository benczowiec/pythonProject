from datetime import datetime
from decimal import Decimal
from dataclasses import dataclass, field
from bank_system.normal.domain.transaction_type import TransactionType

@dataclass
class Transaction:
    _client_name: str
    _transaction_type: TransactionType
    _transaction_amount: Decimal
    _transaction_date: datetime = field(init=False)

    def __post_init__(self):
        self.transaction_amount = self._transaction_amount.quantize(Decimal('0.01'))
        self.transaction_date = datetime.now()


    def __str__(self):
        return f"{self._transaction_date}\t{self._transaction_amount}\t{self._transaction_type}"

    # def __repr__(self):
    #     return (f"Transaction(client_name={repr(self._client_name)}, "
    #             f"transaction_type={repr(self._transaction_type)}, "
    #             f"transaction_amount={repr(self._transaction_amount)}, "
    #             f"transaction_date={repr(self._transaction_date)})")
