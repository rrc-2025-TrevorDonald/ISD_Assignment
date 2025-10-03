""" Investment Account """
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import datetime
from datetime import date
from bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """
    Description:
        Child/Sub class of BankAccount that contains the functions of
        a Investment Account.
    """
    TEN_YEARS_AGO = datetime.date.today() - datetime.timedelta(days=10*365.25)
    def __init__(self, account_number:int, client_number:int, balance:float,
                date_created:date, management_fee:float):
        """
         Description:
            The constructor for the InvestmentAccount class.

        Args:
            account_number(int): The account number assigned in
            corelation to client.
            client_number(int): The number assigned to the given client.
            balance(float): The balance of the account.
            date_created(date): The date that the account was created.
            management_fee(float): Is the flat rate fee that the bank
            charges for managing the Investment Account.


        Raises:
            ValueError(Account Number must be of a numeric type.): When
            the account_number entered is not a integer type.
            ValueError(Client Number must be of a numeric type.): When
            the  client_number entered is not a integer type.
            ValueError("Balance is not of a float type."): When the
            balance cannot be converted to a float if it is not already.
        """
        super().__init__(account_number, client_number, balance, date_created)

        if isinstance(management_fee, (int, float)):
            self.__management_fee = float(management_fee)
        else:
            self.__management_fee = 2.55

    def __str__(self) -> str:
        """
        Description:
            Human readable output of the InvestmentAccount class.

        Returns:
            String: A readout of the values of the InvestmentAccount
            class.
        """
        if self._date_created < InvestmentAccount.TEN_YEARS_AGO:
            self.__management_fee = 0
            m_fee = "Waived"
        else:
            m_fee = f"${self.__management_fee:,.2f}"

        return (super().__str__() + f"\nDate Created: {self._date_created} "
                + f"Management Fee: {m_fee} Account Type: Investment")

    def get_service_charges(self) -> float:
        """
        Description:
            Function for calculate the service charges of the initiated
            Investment Account.

        Returns:
            service_charges(float): The service charge of the initiated
            Investment Account.
        """
        if self._date_created < InvestmentAccount.TEN_YEARS_AGO:
            service_charges = BankAccount.BASE_SERVICE_CHARGES + 0
        else:
            service_charges = (BankAccount.BASE_SERVICE_CHARGES +
                                self.__management_fee)

        return service_charges
