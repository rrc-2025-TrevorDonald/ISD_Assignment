"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import unittest
from bank_account.bank_account import BankAccount

class TestClient(unittest.TestCase):
    """
    Description:
        This class defines all test functions for the BankAccount class.
    """
    def setUp(self):
        """
        Description:
            Setup for unittest's, it allows for more efficient code as
            well as less clutter
        """
        self.bank_account = BankAccount(404, 123, 93000)

    def test_init_valid(self):
        """
        Description:
            Test function for verifying that the constructor for
            BankAccount class is functioning properly.
        """
        # Act & Assert
        self.assertEqual(404, self.bank_account._BankAccount__account_number)
        self.assertEqual(123, self.bank_account._BankAccount__client_number)
        self.assertEqual(93000, self.bank_account._BankAccount__balance)
