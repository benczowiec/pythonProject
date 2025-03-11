class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount ,message="InsufficientBalance"):
        self.balance = balance
        self.amount = amount
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Balance: {self.balance} | Amount: {self.amount} -> {self.message}'