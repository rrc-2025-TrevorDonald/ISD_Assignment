""" Chequing Account """
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from datetime import date
from bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    Description:
        Child/Sub class of BankAccount that contains the functions of
        a Chequing Account.
    """
    def __init__(self, account_number:int, client_number:int, balance:float,
                date_created:date, overdraft_limit:float,
                overdraft_rate:float):
        """
         Description:
            The constructor for the ChequingAccount class.

        Args:
            account_number(int): The account number assigned in
            corelation to client.
            client_number(int): The number assigned to the given client.
            balance(float): The balance of the account.
            date_created(date): The date that the account was created.
            overdraft_limit(float): The maximum amount a balance can be
            overdrawn(below 0.00) before overdraft fees are applied.
            overdraft_rate(float): The rate to which overdraft fees will
            be applied.

        Raises:
            ValueError(Account Number must be of a numeric type.): When
            the account_number entered is not a integer type.
            ValueError(Client Number must be of a numeric type.): When
            the  client_number entered is not a integer type.
            ValueError("Balance is not of a float type."): When the
            balance cannot be converted to a float if it is not already.
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(overdraft_limit, (int,float)):
            self.__overdraft_limit = overdraft_limit
        else:
            self.__overdraft_limit = -100.00

        if isinstance(overdraft_rate, (int, float)):
            self.__overdraft_rate = float(overdraft_rate)
        else:
            self.__overdraft_rate = 0.05

        self.__strategy = OverdraftStrategy(self.__overdraft_limit,
                                            self.__overdraft_rate)

    def __str__(self) -> str:
        """
        Description:
            Human readable output of the ChequingAccount class.

        Returns:
            String: A readout of the values of the ChequingAccount
            class.
        """
        return (super().__str__() + "\nOverdraft Limit: "
                + f"${self.__overdraft_limit:,.2f} Overdraft Rate: "
                + f"{self.__overdraft_rate:.2%} Account Type: Chequing")

    def get_service_charges(self) -> float:
        """
        Description:
            Function for calculate the service charges of the initiated
            Chequing Account.

        Returns:
            service_charges(float): The service charge of the initiated
            Chequing Account.
        """
        return self.__strategy.calculate_service_charges(self)
