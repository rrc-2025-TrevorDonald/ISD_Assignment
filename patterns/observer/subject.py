"""
File containing the Subject class of the Observer design pattern.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from patterns.observer.observer import Observer
from abc import abstractmethod

class Subject(Observer):
    """
    Description:
        The class that holds methods defined for the subject class.
    """
    def __init__(self) -> None:
        """
        Description:
            The constructor for Subject class.
        """
        self._observers = []

    @abstractmethod
    def attach(self, observer:Observer) -> None:
        """
        Description:
            Abstract method attach that will be implemented in the
            concrete class BankAccount.
        """
        pass

    @abstractmethod
    def detach(self, observer:Observer) -> None:
        """
        Description:
            Abstract method detach that will be implemented in the
            concrete class BankAccount.
        """
        pass

    @abstractmethod
    def notify(self, observer:Observer) -> None:
        """
        Description:
            Abstract method notify that will be implemented in the
            concrete class BankAccount.
        """
        pass
