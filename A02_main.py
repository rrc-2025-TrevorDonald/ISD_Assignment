"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime

import datetime
from bank_account import *

# 2. Create an instance of a ChequingAccount with values of your
# choice including a balance which is below the overdraft limit.

my_chequing = ChequingAccount(123, 404, -247.65, datetime.date(1998, 11, 16), 
                              -100, 0.05)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.

print(my_chequing)
print(my_chequing.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.

my_chequing.deposit(1147.65)
print(my_chequing)
print(my_chequing.get_service_charges())

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your
# choice including a balance which is above the minimum balance.

my_savings = SavingsAccount(222, 404, 4820, datetime.date(1998, 11, 16), 100)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.

print(my_savings)
print(my_savings.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw
# enough money from the savings account to cause the balance to fall
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.

my_savings.withdraw(4770)
print(my_savings)
print(my_savings.get_service_charges())

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your
# choice including a date created within the last 10 years.

my_investment = InvestmentAccount(333, 404, 72435.91,
                                  datetime.date(2017, 6, 10), 1.99)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 8.

print(my_investment)
print(my_investment.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your
# choice including a date created prior to 10 years ago.

my_other_investment = InvestmentAccount(999, 404, 5473.11,
                                        datetime.date(2001, 9 , 11), 2.33)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 10.

print(my_other_investment)
print(my_other_investment.get_service_charges())

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10
# by using the withdraw method of the superclass and withdrawing
# the service charges determined by each instance invoking the
# polymorphic get_service_charges method.

my_chequing.withdraw(my_chequing.get_service_charges())
my_savings.withdraw(my_savings.get_service_charges())
my_investment.withdraw(my_investment.get_service_charges())
my_other_investment.withdraw(my_other_investment.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8
# and 10.

print(my_chequing)
print(my_savings)
print(my_investment)
print(my_other_investment)
