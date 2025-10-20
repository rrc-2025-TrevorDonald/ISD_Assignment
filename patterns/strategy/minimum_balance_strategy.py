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
