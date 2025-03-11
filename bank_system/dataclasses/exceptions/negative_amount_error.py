class NegativeAmountError(Exception):
    def __init__(self, amount, message="Amount must be positive"):
        self.amount = amount
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.amount} -> {self.message}'