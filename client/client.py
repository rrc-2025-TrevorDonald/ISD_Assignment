"""
This file holds the Client class and functions.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

import datetime
from email_validator import validate_email
from email_validator import EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email

class Client(Observer):
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
            client_number(int): The number assigned to the given client.
            first_name(str): The clients first name.
            last_name(str): The clients last name.
            email_address(str): The clients email address.

        Raises:
            ValueError("Client Number must be of a numeric type."):
            When the Client Number is not a numeric type.
            ValueError("First Name must not be blank."): When the First
            Name is blank as nothing was entered.
            ValueError("Last Name must not be blank."): When the Last
            Name is blank as nothing was entered
            EmailNotValidError("An email address must have an @-sign."):
            When the entered Email Address is not valid.
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
        else:
            self.__last_name = last_name

        if validate_email(email_address):
            self.__email_address = email_address
        else:
            self.email_address = "email@pixell-river.com"
            raise EmailNotValidError

    def __str__(self) -> str:
        """
        Description:
            __str__ function for the Client class, displays information
            in a human readable way.

        Returns:
            A human readable string representing the client_number,
            first_name, last_name and email_address of the initiated
            instance.
        """
        return (f"{self.__last_name}, {self.__first_name}, "
                f"[{self.__client_number}] - {self.__email_address}")

    @property
    def client_number(self) -> int:
        """
        Description:
            Accessor for private attribute client_number.

        Returns:
            self.__client_number(int): The client_id of the initiated
            instance.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Description:
            Accessor for private attribute first_name.

        Returns:
            self.__first_name(str): The first_name of the initiated
            instance.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Description:
            Accessor for private attribute last_name.

        Returns:
            self.__last_name(str): The last_name of the initiated
            instance.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Description:
            Accessor for private attribute email_address.

        Returns:
            self.__email_address(str): The email_address of the
            initiated instance.
        """
        return self.__email_address

    def update(self, message:str) -> None:
        """
        Description:
            The method for updating the observer/subject letting them
            know of activity within an account.

        Args:
            message (str): The message that is sent to the
            observer/subject letting them know of action within the
            account.
        """
        subject = f"ALERT: Unusual Activity: {datetime.date.today()}"
        simulate_send_email(self.__email_address, subject, message)
