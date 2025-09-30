""" Savings Account """
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import datetime
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    Description:
        Child/Sub class of BankAccount that contains the functions of
        a Savings Account.
    """
    SERVICE_CHARGE_PREMIUM = 2.00
    def __init__(self, account_number:int, client_number:int, balance:float,
                date_created:datetime, minimum_balance:float):
        """
         Description:
            The constructor for the SavingsAccount class.

        Args:
            account_number(int): The account number assigned in
            corelation to client.
            client_number(int): The number assigned to the given client.
            balance(float): The balance of the account.
            date_created(date): The date that the account was created.
            minimum_balance(float): The minimum value a balance can be
            before further service charges are applied.

        Raises:
            ValueError(Account Number must be of a numeric type.): When
            the account_number entered is not a integer type.
            ValueError(Client Number must be of a numeric type.): When
            the  client_number entered is not a integer type.
            ValueError("Balance is not of a float type."): When the
            balance cannot be converted to a float if it is not already.
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(minimum_balance, (int, float)):
            self.__minimum_balance = minimum_balance
        else:
            self.__minimum_balance = 50.00

    def __str__(self):
        """
        """
        return (super().__str__() + "\nMinimum Balance: "
                + f"{self.__minimum_balance} Account Type: Savings")
