"""
File containing the "Parent/Super" class for the strategy design pattern
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Description:
        "Parent/Super" class for Overdraft, MinimumBalance and
        ManagementFee classes within the strategy design pattern.
    """
    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account:BankAccount):
        """
        Description:
            Abstract method thats going to be implemented within the
            "Child/Sub" classes.
        """
        pass
