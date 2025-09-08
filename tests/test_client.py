"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import unittest
from email_validator import EmailNotValidError
from client.client import Client

class TestClient(unittest.TestCase):
    """
    Description:
        This class defines all test functions for the Client class.
    """
    def setUp(self):
        """
        Description:
            Setup for unittest's, it allows for more efficient code as well
            as less clutter.
        """
        self.client = Client(123, "Trevor", "Donald",
                             "Tdonald35@academic.rrc.ca")
    def test_init_valid(self):
        """
        Description:
            Test function for verifying that the constructor for Client class
            is functioning properly.
        """
        # Act & Assert
        self.assertEqual(123, self.client._Client__client_number)
        self.assertEqual("Trevor", self.client._Client__first_name)
        self.assertEqual("Donald", self.client._Client__last_name)
        self.assertEqual("Tdonald35@academic.rrc.ca",
                         self.client._Client__email_address)

    def test_client_number_invalid_type(self):
        """
        Description:
            Test function used for verifying proper ValueError is called
            when a non integer is entered as a client_number.
        """
        # Arrange
        expected = "Client Number must be of a numeric type."
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            Client("123", "Trevor", "Donald", "Tdonald35@academic.rrc.ca")
        self.assertEqual(expected, str(context.exception))

    def test_first_name_invalid_empty(self):
        """
        Description:
            Test function used for verifying proper ValueError is called
            when a no first_name is entered.
        """
        # Arrange
        expected = "First Name must not be blank."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            Client(123, "", "Donald", "Tdonald35@academic.rrc.ca")
        self.assertEqual(expected, str(context.exception))

    def test_last_name_invalid_empty(self):
        """
        Description:
            Test function used for verifying proper ValueError is called
            when a no last_name is entered.
        """
        # Arrange
        expected = "Last Name must not be blank."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            Client(123, "Trevor", "", "Tdonald35@academic.rrc.ca")
        self.assertEqual(expected, str(context.exception))

    def test_email_address_invalid_entry(self):
        """
        Description:
            Test function used for verifying proper EmailNotValidError
            is called when an email that is not valid is entered.
        """
        # Arrange
        expected = "An email address must have an @-sign."

        with self.assertRaises(EmailNotValidError) as context:
            bad_client = Client(123, "Trevor", "Donald", "invalid")
            self.assertEqual(expected, str(context.exception))
            self.assertEqual("email@pixell-river.com",
                            bad_client.email_address)

    def test_client_number_accessor_valid(self):
        """
        Description:
            Test function defined for validating that the accessor for
            client_number is functioning properly.
        """
        # Act & Assert
        self.assertEqual(123, self.client.client_number)

    def test_first_name_accessor_valid(self):
        """
        Description:
            Test function defined for validating that the accessor for
            first_name is functioning properly.
        """
        # Act & Assert
        self.assertEqual("Trevor", self.client.first_name)

    def test_last_name_accessor_valid(self):
        """
        Description:
            Test function defined for validating that the accessor for
            last_name is functioning properly.
        """
        # Act & Assert
        self.assertEqual("Donald", self.client.last_name)

    def test_email_address_accessor_valid(self):
        """
        Description:
            Test function defined for validating that the accessor for
            email_address is functioning properly.
        """
        # Act & Assert
        self.assertEqual("Tdonald35@academic.rrc.ca",
                         self.client.email_address)

    def test_str_valid(self):
        """
        Description:
            Test function defined that the __str__ function is
            outputting the proper information into a string when called
            by print().
        """
        self.assertEqual("Donald, Trevor, [123] - Tdonald35@academic.rrc.ca",
                         str(self.client))
