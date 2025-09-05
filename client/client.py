"""
This file holds the Client class and functions.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from email_validator import validate_email
from email_validator import EmailNotValidError

class Client():
    """
    Description:
    This class will define all functions of a client.
    """
    def __init__(self, client_number:int, first_name:str, last_name:str,
                 email_address:str):
        """
        Description:
            The constructor for the client class.

        Args:
            client_number(int):
            first_name(str):
            last_name(str):
            email_address(str):

        Raises:
            ValueError("Client Number must be of a numeric type."): When the
            Client Number is not a numeric type.
            ValueError("First Name must not be blank."): When the First Name
            is blank as nothing was entered.
            ValueError("Last Name must not be blank."): When the Last Name
            is blank as nothing was entered.
            EmailNotValidError("Email Address not valid"): When the entered
            Email Address is not valid.
        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be of a numeric type.")

        if len(first_name.strip()) <= 0:
            raise ValueError("First Name must not be blank.")
        else:
            self.__first_name = first_name

        if len(last_name.strip()) <= 0:
            raise ValueError("Last Name must not be blank.")

        if validate_email(email_address):
            self.__email_address = email_address
        else:
            raise EmailNotValidError("Email Address not valid")
            self.__email_address = "email@pixell-river.com"
