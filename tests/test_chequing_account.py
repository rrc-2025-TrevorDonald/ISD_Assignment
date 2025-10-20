""" Unit tests for Chequing Account"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import unittest
import datetime
from bank_account import *
from patterns.strategy import *

class TestClient(unittest.TestCase):
    """
    Description:
        Class defined for holding all unit tests for ChequingAccount
        class.
    """
    def setUp(self):
        """
        Description:
            SetUp instance for more streamlined unit testing.
        """
        self.c_account = ChequingAccount(123, 404, 1050.50,
                                         datetime.date(2025, 9, 29), -50, 0.02)
        self.faulty_account = ChequingAccount(123, 404, 1050.50,"2025, 9, 29",
                                              "-50", "0.02")

    def test_init_valid(self):
        """
        Description:
            Test function for verifying the constructor is functioning
            as intended.
        """
        # Act & Assert
        self.assertEqual(123, self.c_account._BankAccount__account_number)
        self.assertEqual(404, self.c_account._BankAccount__client_number)
        self.assertEqual(1050.50, self.c_account._BankAccount__balance)
        self.assertEqual(datetime.date(2025, 9, 29),
                         self.c_account._date_created)
        self.assertEqual(-50, self.c_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.02, self.c_account._ChequingAccount__overdraft_rate)

    def test_overdraft_limit_non_numeric_invalid(self):
        """
        Description:
            Test function for testing to make sure that when you enter
            the improper type, it sets the overdraft limit to -100.
        """
        # Act & Assert
        self.assertEqual(-100,
                         self.faulty_account._ChequingAccount__overdraft_limit)

    def test_overdraft_rate_non_numeric_invalid(self):
        """
        Description:
            Test function for testing to make sure that when you enter
            the improper type, it sets the overdraft rate to 0.05.
        """
        # Act & Assert
        self.assertEqual(0.05,
                         self.faulty_account._ChequingAccount__overdraft_rate)

    def test_date_created_non_date_invalid(self):
        """
        Description:
            Test function for testing to make sure that when you enter
            a non date type, it sets the date create to .today().
        """
        # Act & Assert
        self.assertEqual(datetime.date.today(),
                         self.faulty_account._date_created)
        
    def test_get_service_charge_greater_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a balance greater than the
            overdraft limit is entered.
        """
        actual = self.c_account.get_service_charges()

        # Act & Assert
        self.assertEqual(0.50, actual)

    def test_get_service_charge_lesser_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a balance less than the
            overdraft limit is entered.
        """
        # Arrange
        below = ChequingAccount(123, 404, -600,
                                        datetime.date(2025, 9, 29), -100, 0.05)

        # Act
        actual = below.get_service_charges()

        # Assert
        self.assertEqual(25.5, actual)

    def test_get_service_charge_equal_valid(self):
        """
        Description:
            Test function for ensuring the get_service_charge is
            functioning as intended when a balance equal to the
            overdraft limit is entered.
        """
        #Arrange
        below = ChequingAccount(123, 404, -100,
                                    datetime.date(2025, 9, 29), -100, 0.05)

        # Act
        actual = below.get_service_charges()

        # Assert
        self.assertEqual(0.50, actual)

    def test_str_valid(self):
        """
        Description:
            Test function for ensuring he __str__ method is functioning
            as intended.
        """
        # Arrange
        expected = ("Account Number: 123 Balance: $1,050.50\nOverdraft Limit: "
                    + "$-50.00 Overdraft Rate: 2.00% Account Type: Chequing")

        # Act & Assert
        self.assertEqual(expected, str(self.c_account))
