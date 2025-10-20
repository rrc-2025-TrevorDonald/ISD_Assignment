"""
File containing the "child/sub" class ManagementFeeStrategy of the
ServiceChargeStrategy "Parent/Super" class.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import datetime
from datetime import date
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Description:
        The "Sub/child" class to ServiceChargeStrategy, responsible for
        containing the methods to apply a management fee to an account.
    """
    TEN_YEARS_AGO = datetime.date.today() - datetime.timedelta(days=10*365.25)
    def __init__(self, date_created:date, management_fee:float):
        """
        Description:
            The constructor for the ManagementFeeStrategy class.

        Args:
            date_created (date): The date that the account was created.
            management_fee (float): Is the flat rate fee that the bank
            charges for managing the Investment Account.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee
