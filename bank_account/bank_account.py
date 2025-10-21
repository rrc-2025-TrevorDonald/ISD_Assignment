"""
This file holds the BankAccount class and functions.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from datetime import date
from abc import ABC,abstractmethod
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
    """
    Description:
        Class that will define all BankAccount functions, it's also the
        "Parent/Superclass" for ChequingAccount, InvestmentAccount and
        SavingsAccount.
    """
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    LOW_BALANCE_LEVEL = 50.0
    def __init__(self, account_number:int, client_number:int, balance:float,
                 date_created:date):
        """
        Description:
            The constructor for the BankAccount class.

        Args:
            account_number(int): The account number assigned in
            corelation to client.
            client_number(int): The number assigned to the given client.
            balance(float): The balance of the account.
            date_created(date): The date that the account was created.

        Raises:
            ValueError(Account Number must be of a numeric type.): When
            the account_number entered is not a integer type.
            ValueError(Client Number must be of a numeric type.): When
            the  client_number entered is not a integer type.
            ValueError("Balance is not of a float type."): When the
            balance cannot be converted to a float if it is not already.
        """
        super().__init__()

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be of a numeric type.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be of a numeric type.")

        if isinstance(balance, float):
            self.__balance = balance
        elif isinstance(balance, int):
            balance = float(balance)
            self.__balance = balance
        else:
            self.__balance = 0
            raise ValueError("Balance is not of a float type.")

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    def __str__(self) -> str:
        """
        Description:
            __str__ function for the BankAccount class, displays
            information in a human readable way.
        Returns:
             A human readable string representing the account_number,
             and balance of th initiated instance.
        """
        return(f"Account Number: {self.__account_number} Balance: "
               f"${self.__balance:,.2f}")

    @property
    def account_number(self) -> int:
        """
        Description:
            Accessor for private attribute account_number.

        Returns:
            self.__account_number(int): The account_number of the
            initiated instance.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Description:
            Accessor for private attribute client_number.

        Returns:
            self.__client_number(int): The client_number of the
            initiated instance.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Description:
            Accessor for private attribute balance.
        
        Returns:
            self.__balance(float): The balance of the initiated
            instance.
        """
        return self.__balance

    def update_balance(self, amount:float) -> None:
        """
        Description:
            Function define for updating the balance of the given
            account.

        Args:
            amount(float): The amount that will be used to update the
            account.

        Raises:
            ValueError(Amount must be of a numeric type.): When the
            amount entered is not of a numeric type.
        """
        if amount > BankAccount.LARGE_TRANSACTION_THRESHOLD:
            self.notify((f"Large transaction ${amount:,.2f}: on account "
                         + f"{self.__account_number}."))

        if isinstance(amount, float):
            self.__balance += amount
        elif isinstance(amount, int):
            amount = float(amount)
            self.__balance += amount
        else:
            raise ValueError("Amount must be of a numeric type.")

        if self.__balance < BankAccount.LOW_BALANCE_LEVEL:
            self.notify((f"Low balance warning {self.__balance:,.2f}: on "
                         + f"account {self.__account_number}."))

    def deposit(self, amount:float) -> None:
        """
        Description:
            Defined function for depositing from of the initiated
            instance.

        Args:
            amount(float): The amount that will be deposited into the
            given account.

        Raises:
            ValueError(Amount must be of a numeric type.): When the
            entered value is not of a numeric type.
            ValueError(Deposit amount: {amount} must be positive.): When
            the entered amount is not a positive number.
        """
        if isinstance(amount, float):
            if amount <= 0:
                raise ValueError(f"Deposit amount: {amount} must be positive.")
            self.__balance += amount
        elif isinstance(amount, int):
            if amount <= 0:
                raise ValueError(f"Deposit amount: {amount} must be positive.")
            amount = float(amount)
            self.__balance += amount
        else:
            raise ValueError("Amount must be of a numeric type.")


    def withdraw(self, amount:float) -> None:
        """
        Description:
            Defined function for withdrawing from of the initiated
            instance.

        Args:
            amount(float): The amount that will be withdraw'd from the
            given account.

        Raises:
            ValueError(Withdraw amount: {amount} must be numeric.): When
            the entered value is not of a numeric type.
            ValueError(Withdraw amount: {amount} must be positive.):
            When the entered amount is not a positive number.
            ValueError(Withdraw amount: {amount} must not exceed the
            account balance: {self.__balance}.): When the amount entered
            is more than the balance of the account.
        """
        if isinstance(amount, float):
            if amount <= 0:
                raise ValueError(f"Withdraw amount: {amount}" /
                                 " must be positive.")

            if amount > self.__balance:
                raise ValueError(f"Withdraw amount: {amount} must not exceed" /
                                f" the account balance: {self.__balance}.")
            self.__balance -= amount
        elif isinstance(amount, int):
            if amount <= 0:
                raise ValueError(f"Withdraw amount: {amount}" \
                                 f" must be positive.")

            if amount > self.__balance:
                raise ValueError(f"Withdraw amount: {amount} must not exceed" \
                                f" the account balance: {self.__balance}.")
            amount = float(amount)
            self.__balance -= amount
        else:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")

    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Description:
            Abstract method get_service_charges used by child/sub
            classes to perform calculations depending on type of
            account.

        Returns:
            Float: The service charge of the type of account.
        """
        pass

    def attach(self, observer:Observer) -> None:
        """
        Description:
            Attaches an observer to an account.

        Args:
            observer (Observer): The observer attached to the account.
        """
        self._observers.append(observer)

    def detach(self, observer:Observer) -> None:
        """
        Description:
            Detaches an observer from an account.

        Args:
            observer (Observer): The observer removed from an account.
        """
        self._observers.remove(observer)

    def notify(self, message:str) -> None:
        """
        Description:
            Notifies all observers of a change that has happened to the
            account they are observing.

        Args:
            message (str): The message relayed back to the observer.
        """
        for observer in self._observers:
            observer.update(message)
