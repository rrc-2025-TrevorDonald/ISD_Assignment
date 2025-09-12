"""
Description: Unit tests for the BankAccount class.
Author: Trevor Donald
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

    def test_balance_non_numeric_invalid(self):
        """
        Description:
            Test function defined for testing when a non numeric number
            is given for the balance.
        """
        # Arrange
        expected = "Balance is not of a float type."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            bad_bank_account = BankAccount(404, 123, "93000")
            self.assertEqual(expected, str(context.exception))
            self.assertEqual(0, bad_bank_account.balance)

    def test_account_number_non_numeric_invalid(self):
        """
        Description:
            Test function defined for testing when a non numeric number
            is given for the account_number.
        """
        # Arrange
        expected = "Account Number must be of a numeric type."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            BankAccount("404", 123, 93000)
            self.assertEqual(expected, str(context.exception))

    def test_client_number_non_numeric_invalid(self):
        """
        Description:
            Test function defined for testing when a non numeric number
            is given for the client_number.
        """
        #Arrange
        expected = "Client Number must be of a numeric type."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            BankAccount(404, "123", 93000)
            self.assertEqual(expected, str(context.exception))

    def test_account_number_accessor_valid(self):
        """
        Description:
            Test function defined for testing to make sure the accessor
            for account_number is working properly.
        """
        # Act & Assert
        self.assertEqual(404, self.bank_account.account_number)

    def test_client_number_accessor_valid(self):
        """
        Description:
            Test function defined for testing to make sure the accessor
            for client_number is working properly.
        """
        # Act & Assert
        self.assertEqual(123, self.bank_account.client_number)

    def test_balance_accessor_valid(self):
        """
        Description:
            Test function defined for testing to make sure the accessor
            for balance is working properly.
        """
        # Act & Assert
        self.assertEqual(93000, self.bank_account.balance)

    def test_update_balance_deposit_valid(self):
        """
        Description:
            Test function defined for testing to make sure the
            update_balance function is working as intended when giving
            a positive number.
        """
        # Arrange
        self.bank_account.update_balance(1000)
        # Act & Assert
        self.assertEqual(94000, self.bank_account.balance)

    def test_update_balance_withdraw_valid(self):
        """
        Description:
            Test function defined for testing to make sure the
            update_balance function is working as intended when giving
            a negative number.
        """
        # Arrange
        self.bank_account.update_balance(-1000)
        # Act & Assert
        self.assertEqual(92000, self.bank_account.balance)

    def test_update_balance_non_numeric_invalid(self):
        """
        Description:
            Test function defined for testing when a non numeric number
            is given to the update_balance function.
        """
        # Arrange
        expected = "Amount must be of a numeric type."
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            self.bank_account.update_balance("1000")
            self.assertEqual(expected, str(context.exception))

    def test_deposit_valid(self):
        """
        Description:
            Test function defined for testing to make sure the deposit
            function is working as intended.
        """
        # Arrange
        self.bank_account.deposit(1000)

        # Act & Assert
        self.assertEqual(94000, self.bank_account.balance)

    def test_deposit_negative_invalid(self):
        """
        Description:
            Test function defined for testing when a negative number is
            given.
        """
        # Arrange
        expected = "Deposit amount: -1000 must be positive."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            self.bank_account.deposit(-1000)
            self.assertEqual(expected, str(context.expected))

    def test_withdraw_valid(self):
        """
        Description:
            Test function defined for testing to make sure the withdraw
            function is working as intended.
        """
        # Arrange
        self.bank_account.withdraw(1000)

        # Act & Assert
        self.assertEqual(92000,self.bank_account.balance)

    def test_withdraw_negative_invalid(self):
        """
        Description:
            Test function defined for testing when a negative number is
            given.
        """
        # Arrange
        expected = "Withdraw amount: -1000 must be positive."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw(-1000)
            self.assertEqual(expected, str(context.expected))

    def test_withdraw_exceeds_balance_invalid(self):
        """
        Description:
            Test function defined for testing the amount being withdrew
            exceeds the balance amount.
        """
        # Arrange
        expected = "Withdraw amount: 94000 must not exceed the account" \
                    "balance: 93000."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw(94000)
            self.assertEqual(expected, str(context.expected))

    def test_bank_account_str_valid(self):
        """
        Description:
            Test function defined for testing to insure the __str__
            method is working as intended.
        """
        self.assertEqual("Account Number: 404 Balance: $93,000.00",
                         str(self.bank_account))
