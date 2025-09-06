"""
This file holds the BankAccount class and functions.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

class BankAccount():
    """
    Description:
        Class that will define all BankAccount functions.
    """
    def __init__(self, account_number:int, client_number:int, balance:float):
        """
        Description:
            The constructor for the BankAccount class.

        Args:
            account_number(int): The account number assigned in corelation to
            client.
            client_number(int): The number assigned to the given client.
            balance(float): The balance of the account.

        Raises:
            ValueError(Account Number must be of a numeric type.): When the
            account_number entered is not a integer type.
            ValueError(Client Number must be of a numeric type.): When the
            client_number entered is not a integer type.
            ValueError("Balance is not of a float type."): When the balance
            cannot be converted to a float if it is not already.
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be of a numeric type.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be of a numeric type.")

        try:
            self.__balance = float(balance)
        except:
            self.__balance = 0
            raise ValueError("Balance is not of a float type.")
