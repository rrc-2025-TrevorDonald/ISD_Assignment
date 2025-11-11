__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Description:
        Class that inherits from LookupWindow and holds methods that
        pertain to the client lookup window.
    """
    def __init__(self):
        """
        Description:
            Constructor for the ClientLookupWindow class.
        """
        super().__init__()

        tuple_data = load_data()
        self.__client_listing = tuple_data[0]
        self.__accounts = tuple_data[1]

        self.lookup_button.clicked.connect(__on_lookup_client)
        self.client_number_edit.textChanged.connect(__on_text_changed)
        self.account_table.cellClicked.connect(__on_select_account)
