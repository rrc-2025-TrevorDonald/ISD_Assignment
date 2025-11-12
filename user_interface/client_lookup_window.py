__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from bank_account import *
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QTableWidget
from PySide6.QtCore import Qt, Slot, QObject, Signal, SignalInstance

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

        tuple_dict = load_data()
        self.__client_listing = tuple_dict[0]
        self.__accounts = tuple_dict[1]

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

    @Slot()
    def __on_lookup_client(self) -> None:
        """
        """
        entered_client_number = self.client_number_edit.text()

        try:
            entered_client_number_int = int(entered_client_number)
        except:
            input_error_prompt = QMessageBox.information(None, "Input Error",
                                "The client number must be a numeric value.",
                                QMessageBox.Yes, QMessageBox.Yes)
            if input_error_prompt == QMessageBox.Yes:
                self.reset_display()

        if entered_client_number not in self.__client_listing:
            client_not_found = QMessageBox.information(None, "Not Fount",
                                f"Client Number: {entered_client_number}"
                                + " not found", QMessageBox.Yes,
                                QMessageBox.Yes)
            if client_not_found == QMessageBox.Yes:
                self.reset_display()
        else:
            chosen_client = self.__client_listing[entered_client_number]
            self.client_info_label.setText(
                f"Client Name: {chosen_client.first_name} "
                + f"{chosen_client.last_name}"
            )

            for key in self.__accounts:
                if self.__accounts[key].client_number == \
                    entered_client_number_int:
                    rows = QTableWidget.rowCount(self.account_table)
                    self.account_table.insertRow(rows)

                    account_number = QTableWidgetItem(
                        str(self.__accounts[key].account_number))
                    balance = QTableWidgetItem(
                        f"{self.__accounts[key].balance:,.2f}")
                    date_created = QTableWidgetItem(
                        str(self.__accounts[key]._date_created))
                    account_type = QTableWidgetItem(
                        str(self.__accounts[key].__class__.__name__))

                    self.account_table.setItem(rows, 0, account_number)
                    self.account_table.setItem(rows, 1, balance)
                    self.account_table.setItem(rows, 2, date_created)
                    self.account_table.setItem(rows, 3, account_type)

    @Slot()
    def __on_text_changed(self) -> None:
        """
        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row:int, column:int) -> None:
        """
        """
        selected_account_number = self.account_table.item(row, column).text()

        if selected_account_number == "":
            QMessageBox.information(None, "Invalid Selection",
            "Please select a valid record.", QMessageBox.Yes, QMessageBox.Yes)

        if selected_account_number in self.__accounts:
            focused_account = self.__accounts[selected_account_number]

            account_detail = AccountDetailsWindow(focused_account)
            account_detail.balance_updated.connect(self.__update_data)
            account_detail.exec_()

        else:
            QMessageBox.information(None, "No Bank Account",
            "Bank Account selected does not exist.", QMessageBox.Yes,
            QMessageBox.Yes)

    @Slot(BankAccount)
    def __update_data(self, account:BankAccount):
        """
        """
        for row in range(self.account_table.rowCount()):
            if self.account_table.item(row, 0).text() == \
                str(account.account_number):
                this_account = self.account_table.item(row, 0).text()
                self.__accounts[this_account] = account
                update_data(account)
