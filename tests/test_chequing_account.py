""" """
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from datetime import datetime, date
from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    """
    Description:
        Child/Sub class of BankAccount, that represents a contains the
        functions of a Chequing Account.
    """
    def __init__(self, account_number:int, client_number:int, balance:float,
                date_created:date, minimum_balance:float):
        """
        Description:
            The constructor for the BankAccount class.

        Args:
            account_number(int): The account number assigned in
            corelation to client.
            client_number(int): The number assigned to the given client.
            balance(float): The balance of the account.
            date_created(date): The date that the account was created.c
            BASE_SERVICE_CHARGE(float): The base service charge rate for
            all child classes

        Raises:
            ValueError(Account Number must be of a numeric type.): When
            the account_number entered is not a integer type.
            ValueError(Client Number must be of a numeric type.): When
            the  client_number entered is not a integer type.
            ValueError("Balance is not of a float type."): When the
            balance cannot be converted to a float if it is not already.
        """
        super().__init__(account_number, client_number, balance, date_created)