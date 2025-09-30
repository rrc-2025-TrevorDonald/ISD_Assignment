""" Unit tests for Investment Account"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import unittest
import datetime
from bank_account import *

class TestClient(unittest.TestCase):
    """
    Description:
        Class defined for holding all unit tests for InvestmentAccount
        class.
    """
    def setUp(self):
        """
        Description:
            SetUp instance for more streamlined unit testing.
        """
        self.i_account = InvestmentAccount(123, 404, 1050.50,
                                           datetime.date(2025, 9, 29), 3.99)
        self.faulty_account = InvestmentAccount(123, 404, 1050.50,
                                           datetime.date(2025, 9, 29), "3.99")

    def test_init_valid(self):
        """
        Description:
            Test function for verifying the constructor is functioning
            as intended.
        """
        # Act & Assert
        self.assertEqual(123, self.i_account._BankAccount__account_number)
        self.assertEqual(404, self.i_account._BankAccount__client_number)
        self.assertEqual(1050.50, self.i_account._BankAccount__balance)
        self.assertEqual(datetime.date(2025, 9, 29),
                         self.i_account._date_created)
        self.assertEqual(3.99,
                         self.i_account._InvestmentAccount__management_fee)

    def test_management_fee_non_numeric_invalid(self):
        """
         Description:
            Test function for testing to make sure that when you enter
            the improper type, it sets the management_fee to 2.55.
        """
        # Act & Assert
        self.assertEqual(2.55,
                        self.faulty_account._InvestmentAccount__management_fee)

    def test_get_service_charges_more_than_ten_years_valid(self):
        """
         Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a date more than 10 years
            ago is entered.
        """
        # Arrange
        more_ten_years = InvestmentAccount(123, 404, 1050.50,
                                           datetime.date(1998, 9, 29), 3.99)

        # Act
        actual = more_ten_years.get_service_charges()

        # Assert
        self.assertEqual(0.50, actual)

    def test_get_service_charges_exactly_ten_years_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a date equal to 10 years
            ago is entered.
        """
        ### At the time of testing this was exactly 10 years ago ###
        # Assert
        exactly_ten_years = InvestmentAccount(123, 404, 1050.50,
                                           datetime.date(2015, 9, 30), 3.99)

        # Act
        actual = exactly_ten_years.get_service_charges()

        # Assert
        self.assertEqual(0.50, actual)

    def test_get_service_charges_less_than_ten_years_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a date less than than 10 years
            ago is entered.
        """
        # Act
        actual = self.i_account.get_service_charges()

        # Assert
        self.assertEqual(4.49, actual)

    def test_more_than_ten_years_str_valid(self):
        """
        Description:
            Test function for ensuring he __str__ method is functioning
            as intended when the account was created more than 10 year
            ago.
        """
        # Arrange
        more_ten_years = InvestmentAccount(123, 404, 1050.50,
                                           datetime.date(1998, 9, 29), 3.99)

        # Act
        expected = ("Account Number: 123 Balance: $1,050.50\nDate Created: "
                    + "1998-09-29 Management Fee: Waived Account Type: "
                    + "Investment")
        # Assert
        self.assertEqual(expected, str(more_ten_years))

    def test_less_than_ten_years_str_valid(self):
        """
        Description:
            Test function for ensuring he __str__ method is functioning
            as intended when the account was created less than 10 year
            ago.
        """
        # Arrange
        expected = ("Account Number: 123 Balance: $1,050.50\nDate Created: "
                    + "2025-09-29 Management Fee: $3.99 Account Type: "
                    + "Investment")

        # Assert & Assert
        self.assertEqual(expected, str(self.i_account))
