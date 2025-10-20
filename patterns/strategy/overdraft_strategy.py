"""
File containing the "child/sub" class OverdraftStrategy of the
ServiceChargeStrategy "Parent/Super" class.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Description:
        The "Sub/child" class to ServiceChargeStrategy, responsible for
        containing the methods applying an overdraft to and account.
    """
    def __init__(self, overdraft_limit:float, overdraft_rate:float):
        """
        Description:
            Constructor for the OverdraftStrategy class.

        Args:
            overdraft_limit (float): The maximum amount a balance can be
            overdrawn(below 0.00).
            overdraft_rate (float): The rate to which overdraft fees
            will be applied.
        """
        self.___overdraft_limit = overdraft_limit
        self.___overdraft_rate = overdraft_rate