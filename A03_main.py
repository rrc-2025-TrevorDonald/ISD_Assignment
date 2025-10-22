"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

import datetime
from bank_account import *
from client.client import Client

# 2. Create a Client object with data of your choice.

client_01 = Client(404, "Trevor", "Donald", "Trevor.r.donald@academic.rrc.ca")

# 3a. Create a ChequingAccount object with data of your choice, using
# the client_number of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the
# client_number of the client created in step 2.

chequing_01 = ChequingAccount(123, 404, 89546.00, datetime.date(1998, 11, 16),
                              -200.00, 0.025)
savings_01 = SavingsAccount(321, 404, 250.00, datetime.date(2001, 12, 11), 10)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject'
# objects. The Client object is an 'Observer' object.
# 4a.  Attach the Client object (created in step 1) to the
# ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the
# SavingsAccount object (created in step 2).

chequing_01.attach(client_01)
savings_01.attach(client_01)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the
# client_number of the client created in this step.

client_02 = Client(890, "Homer", "Simpson", "hsimpson@gmail.com")
savings_02 = SavingsAccount(763, 890, 78.00, datetime.date(1993, 11, 11), 10)
savings_02.attach(client_02)

# 6. Use the ChequingAccount and SavingsAccount objects created
# in steps 3 and 5 above to perform transactions (deposits and
# withdraws) which would cause the Subject (BankAccount) to notify the
# Observer (Client) as well as transactions that would not cause the
# Subject to notify the Observer. Ensure each BankAccount object
# performs at least 3 transactions. REMINDER: the deposit() and
# withdraw() methods can raise exceptions ensure the methods are invoked
# using proper exception handling such that any exception messages are
# printed to the console.

# Account 1
# Deposit (Notify)
try:
    chequing_01.deposit(10000.00)
except Exception as e:
    print(e)
try:
    savings_01.deposit(15000.00)
except Exception as e:
    print(e)

# Withdraw (Notify)
try:
    chequing_01.withdraw(99500.00)
except Exception as e:
    print(e)
try:
    savings_01.withdraw(15225.00)
except Exception as e:
    print(e)

# Deposit (W/O Notify)
try:
    chequing_01.deposit(1000.00)
except Exception as e:
    print(e)
try:
    savings_01.deposit(1000.00)
except Exception as e:
    print(e)

# Withdraw (W/O Notify)
try:
    chequing_01.withdraw(500.00)
except Exception as e:
    print(e)
try:
    savings_01.withdraw(500.00)
except Exception as e:
    print(e)

# Account 2
# Deposit (Notify)
try:
    savings_02.deposit(100000)
except Exception as e:
    print(e)

# Withdraw (Notify)
try:
    savings_02.withdraw(100070)
except Exception as e:
    print(e)

# Deposit (W/O Notify)
try:
    savings_02.deposit(322)
except Exception as e:
    print(e)

# Withdraw (W/O Notify)
try:
    savings_02.withdraw(7.78)
except Exception as e:
    print(e)
