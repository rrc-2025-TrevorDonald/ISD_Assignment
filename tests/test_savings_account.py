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

    def test_minimum_balance_non_numeric_invalid(self):
        """
        Description:
            Test function for testing to make sure that when you enter
            the improper type, it sets the minimum_balance to 50.00.
        """
        self.assertEqual(50.00,
                         self.faulty_account._SavingsAccount__minimum_balance)

    def test_get_service_charges_greater_than_minimum_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a amount greater than the
            minimum_balance is entered.
        """
        actual = self.s_account.get_service_charges()

        self.assertEqual(0.50, actual)

    def test_get_service_charges_equal_to_minimum_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a amount equal to the
            minimum_balance is entered.
        """
        equal_balance = SavingsAccount(123, 404, 150,
                                       datetime.date(2025, 9, 29), 150)

        actual = equal_balance.get_service_charges()

        self.assertEqual(0.50, actual)

    def test_get_service_charges_less_than_minimum_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a amount less than the
            minimum_balance is entered.
        """
        equal_balance = SavingsAccount(123, 404, 100,
                                       datetime.date(2025, 9, 29), 150)

        actual = equal_balance.get_service_charges()

        self.assertEqual(1, actual)

    def test_str_valid(self):
        """
        Description:
            Test function for ensuring he __str__ method is functioning
            as intended.
        """
        expected = ("Account Number: 123 Balance: $1,050.50\nMinimum Balance: "
                    + "$150.00 Account Type: Savings")

        self.assertEqual(expected, str(self.s_account))
