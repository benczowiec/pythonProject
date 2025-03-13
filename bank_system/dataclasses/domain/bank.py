from bank_system.dataclasses.exceptions.client_not_found_error import ClientNotFoundError
from bank_system.dataclasses.domain.client import Client

from dataclasses import dataclass, field


@dataclass
class Bank:
    _clients: set[Client] = field(default_factory=set, init=False)

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

    @property
    def clients(self):
        return self._clients

    @clients.setter
    def clients(self, clients: set[Client]):
        self._clients = clients