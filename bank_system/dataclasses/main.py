from decimal import Decimal

from bank_system.dataclasses.domain.client import Client
from bank_system.dataclasses.domain.bank import Bank


bank = Bank()

client = Client("sds")

client1 = Client("Paweł")
client2 = Client("Gosia")
client3 = Client("Genowefa")
client4 = Client("Paweł")
client5 = Client("Roman")
client6 = Client("Tola")

client1.deposit(Decimal('1000'))
client1.withdraw(Decimal('550'))
client1.withdraw(Decimal('24.31'))

client2.deposit(Decimal('2500'))
client2.withdraw(Decimal('31'))
client2.withdraw(Decimal('24.37'))

client3.deposit(Decimal('1500'))
client3.withdraw(Decimal('300'))
client3.withdraw(Decimal('50.75'))

client4.deposit(Decimal('2000'))
client4.withdraw(Decimal('500'))
client4.withdraw(Decimal('100.25'))

client5.deposit(Decimal('3000'))
client5.withdraw(Decimal('750'))
client5.withdraw(Decimal('200.50'))

client6.deposit(Decimal('1200'))
client6.withdraw(Decimal('100'))
client6.withdraw(Decimal('60.75'))

client1.print_statement()
client2.print_statement()
client3.print_statement()
client4.print_statement()
client5.print_statement()
client6.print_statement()

bank.add_client(client1)
bank.add_client(client2)
bank.add_client(client3)
bank.add_client(client4)
bank.add_client(client5)
bank.add_client(client6)

bank.print_all_clients_balances()