from decimal import Decimal

import pytest

from bank_system.dataclasses.domain.client import Client
from bank_system.dataclasses.domain.transaction_type import TransactionType


class TestClient:

    @pytest.fixture
    def setup_client(self):
        return Client('Paweł')

    def test_deposit(self, setup_client):
        #when
        setup_client.deposit(Decimal('2500'))

        #then
        result_transactions = setup_client.transactions
        assert setup_client.balance == Decimal('2500')
        assert len(result_transactions) == 1
        assert result_transactions[0]._client_name == "Paweł"
        assert result_transactions[0]._transaction_type == TransactionType.DEPOSIT
        assert result_transactions[0]._transaction_amount == Decimal('2500.00')

    def test_withdraw(self, setup_client):
        #given
        setup_client.deposit(Decimal('2500.51'))

        #when
        setup_client.withdraw(Decimal('1000'))

        #then
        result_transactions = setup_client.transactions
        assert setup_client.balance == Decimal('1500.51')
        assert len(result_transactions) == 2
        assert result_transactions[1]._client_name == "Paweł"
        assert result_transactions[1]._transaction_type == TransactionType.WITHDRAW
        assert result_transactions[1]._transaction_amount == Decimal('1000.00')
