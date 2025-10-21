"""
File containing the Subject class of the Observer design pattern.
"""
__author__ = "Trevor Donald"
__version__ = "1.0.0"

from patterns.observer.observer import Observer

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
        self._observers = Observer