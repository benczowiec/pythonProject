from bank_system.normal.domain.client import Client
from bank_system.normal.exceptions.client_not_found_error import ClientNotFoundError


class Bank:

    def __init__(self):
        self._clients :set[Client] = set()

    def add_client(self, client :Client):
        self._clients.add(client)

    def remove_client(self, client :Client):
        self._clients.remove(client)

    def get_client(self, client: Client):
        if client in self._clients:
            return client
        else:
            raise ClientNotFoundError(client)

    def print_all_clients_balances(self):
        for client in self._clients:
            print(client)