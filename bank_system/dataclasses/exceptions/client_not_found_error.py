class ClientNotFoundError(Exception):
    def __init__(self, client, message="Client not found"):
        self.client = client
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.client} -> {self.message}'