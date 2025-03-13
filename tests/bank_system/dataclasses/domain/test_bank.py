import pytest

from bank_system.dataclasses.domain.bank import Bank
from bank_system.dataclasses.domain.client import Client
from bank_system.dataclasses.exceptions.client_not_found_error import ClientNotFoundError


class TestBank:

    @pytest.fixture
    def setup_bank(self):
        bank = Bank()
        client1 = Client("Lola")
        client2 = Client("Tola")
        bank.clients = {client1, client2}
        return bank

    def test_add_client(self, setup_bank):
        # given
        client = Client("Paweł")

        # when
        setup_bank.add_client(client)

        # then
        assert len(setup_bank.clients) == 3
        assert client in setup_bank.clients

    def test_remove_client(self, setup_bank):
        # given
        client = Client("Paweł")
        setup_bank.add_client(client)

        # when
        setup_bank.remove_client(client)

        # then
        assert len(setup_bank.clients) == 2
        assert client not in setup_bank.clients

    def test_get_client(self, setup_bank):
        # given
        client = Client("Paweł")
        setup_bank.add_client(client)

        # when
        result_client = setup_bank.get_client(client)

        # then
        assert result_client == client
        assert len(setup_bank.clients) == 3
        assert client in setup_bank.clients

    def test_get_client_error(self, setup_bank):
        # given
        client = Client("Paweł")

        # when + then
        with pytest.raises(ClientNotFoundError):
            setup_bank.get_client(client)

    def test_print_all_clients_balances(self, setup_bank, capfd):
        # when
        setup_bank.print_all_clients_balances()

        # then
        captured = capfd.readouterr()
        assert "Client: Tola | 0.00" in captured.out
        assert "Client: Lola | 0.00" in captured.out
