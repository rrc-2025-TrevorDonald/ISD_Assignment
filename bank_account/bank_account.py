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
            account_number(int): The account number assigned in
            corelation to client.
            client_number(int): The number assigned to the given client.
            balance(float): The balance of the account.

        Raises:
            ValueError(Account Number must be of a numeric type.): When
            the account_number entered is not a integer type.
            ValueError(Client Number must be of a numeric type.): When
            the  client_number entered is not a integer type.
            ValueError("Balance is not of a float type."): When the
            balance
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

    @property
    def account_number(self) -> int:
        """
        Description:
            Accessor for private attribute account_number.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Description:
            Accessor for private attribute client_number.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Description:
            Accessor for private attribute balance.
        """
        return self.__balance

    def update_balance(self, amount:float) -> float:
        """
        Description:
            Function define for updating the balance of the given
            account.

        Args:
            amount(float): The amount that will be used to update the
            account with, wether that be addition or subtracting.

        Returns:
            balance(float): The updated balance amount after the
            addition or subtraction has been made

        Raises:
            ValueError(Amount must be of a numeric type.): When the
            amount entered is not of a numeric type.
        """
        try:
            amount = float(amount)

            if amount < 0:
                self.deposit(amount)
            else:
                self.withdraw(amount)
        except:
            raise ValueError("Deposit amount: {amount} must be numeric.")

    def deposit(self, deposit_amount:float) -> float:
        """
        Description:
        Args:
        Returns:
        Raises:
        """
        if not isinstance(deposit_amount, float):
            raise ValueError("Amount must be of a numeric type.")

        if deposit_amount <= 0:
            raise ValueError("Deposit amount: {formatted amount}" \
                            "must be positive.")

        self.__balance += deposit_amount

