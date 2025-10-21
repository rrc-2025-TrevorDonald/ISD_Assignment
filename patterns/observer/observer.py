"""
File for containing Observer "Super/parent" class.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Description:
        "Parent/Super" class for the Observer design pattern.
    """

    @abstractmethod
    def update(self, message:str) -> None:
        """
        Description:
            Abstract method of update that will be used for Client
            class.
        """
        pass
