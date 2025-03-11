from decimal import Decimal
from datetime import datetime

from bank_system.normal.domain.transaction_type import TransactionType


class Transaction:

    def __init__(self, client_name, transaction_type :TransactionType, transaction_amount :Decimal):
        self._client_name = client_name
        self._transaction_type = transaction_type
        self._transaction_amount = Decimal(transaction_amount).quantize(Decimal('0.01'))
        self._transaction_date = datetime.now()

    def __str__(self):
        return f"{self._transaction_date}\t{self._transaction_amount}\t{self._transaction_type}"

    def __repr__(self):
        return (f"Transaction(client_name={repr(self._client_name)}, "
                f"transaction_type={repr(self._transaction_type)}, "
                f"transaction_amount={repr(self._transaction_amount)}, "
                f"transaction_date={repr(self._transaction_date)})")