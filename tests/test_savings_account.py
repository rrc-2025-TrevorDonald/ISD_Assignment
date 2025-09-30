""" Unit tests for Savings Account """
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import unittest
import datetime
from bank_account import *

class TestClient(unittest.TestCase):
    """
    Description:
        Class defined for holding all unit tests for SavingsAccount
        class.
    """
    def setUp(self):
        """
        Description:
            SetUp instance for more streamlined unit testing.
        """
        self.s_account = SavingsAccount(123, 404, 1050.50,
                                        datetime.date(2025, 9, 29), 150.00)
        self.faulty_account = SavingsAccount(123, 404, 1050.50,
                                        datetime.date(2025, 9, 29), "150.00")

    def test_init_valid(self):
        """
        Description:
            Test function for verifying the constructor is functioning
            as intended.
        """
        # Act & Assert
        self.assertEqual(123, self.s_account._BankAccount__account_number)
        self.assertEqual(404, self.s_account._BankAccount__client_number)
        self.assertEqual(1050.50, self.s_account._BankAccount__balance)
        self.assertEqual(datetime.date(2025, 9, 29),
                         self.s_account._date_created)
        self.assertEqual(150.00,
                         self.s_account._SavingsAccount__minimum_balance)
