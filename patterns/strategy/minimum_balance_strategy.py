"""
File containing the "child/sub" class MinimumBalanceStrategy of the
ServiceChargeStrategy "Parent/Super" class.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Description:
        The "Sub/child" class to ServiceChargeStrategy, responsible for
        containing the methods to apply a fee to an account if the
        balance is less than the minimum balance.
    """
    SERVICE_CHARGE_PREMIUM = 2.00
    def __init__(self, minimum_balance:float):
        """
        Description:
            The constructor for the MinimumBalanceStrategy class

        Args:
            minimum_balance (float): he minimum value a balance can be
            before further service charges are applied.
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account:BankAccount) -> float:
        """
        Description:
            The method used for calculating the fee applied to an
            account below the minimum balance.

        Args:
            account (float): The bank account used to apply the
            minimum balance fee charge to.
        """
        if account.balance >= self.__minimum_balance:
            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE *
                            MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM)

        return service_charge
