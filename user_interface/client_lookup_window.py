__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Trevor Donald"

from bank_account import *
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QTableWidget
from PySide6.QtCore import Qt, Slot
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
        Description:
            This method contains the code for looking up a client, it
            takes the input from the client_number_edit and searches
            through the list of clients to find the client as well as
            all of their accounts when the lookup_button is clicked. It 
            then will go through their accounts then appends the
            account_number, balance, date_created as well as the type of
            account to its own row in the table.

        Returns:
            None
        """
        entered_client_number = self.client_number_edit.text()

        try:
            entered_client_number_int = int(entered_client_number)
        except ValueError:
            input_error_prompt = QMessageBox.information(self, "Input Error",
                                "The client number must be a numeric value.",
                                QMessageBox.Yes)
            if input_error_prompt == QMessageBox.Yes:
                self.reset_display()
                return

        if entered_client_number not in self.__client_listing:
            client_not_found = QMessageBox.information(self, "Not Fount",
                                f"Client Number: {entered_client_number}"
                                + " not found", QMessageBox.Yes)
            if client_not_found == QMessageBox.Yes:
                self.reset_display()
                return
        else:
            chosen_client = self.__client_listing[entered_client_number]
            self.client_info_label.setText(
                f"Client Name: {chosen_client.first_name} "
                + f"{chosen_client.last_name}")

        for key in self.__accounts.items():
            if key[1].client_number == entered_client_number_int:
                rows = QTableWidget.rowCount(self.account_table)
                self.account_table.insertRow(rows)

                account_number = QTableWidgetItem(str(key[1].account_number))
                balance = QTableWidgetItem(f"{key[1].balance:,.2f}")
                date_created = QTableWidgetItem(str(key[1]._date_created))
                account_type = QTableWidgetItem(str(key[1].__class__.__name__))

                self.account_table.setItem(rows, 0, account_number)
                self.account_table.setItem(rows, 1, balance)
                self.account_table.setItem(rows, 2, date_created)
                self.account_table.setItem(rows, 3, account_type)

    @Slot()
    def __on_text_changed(self) -> None:
        """
        Description:
            This method is run in the event of the text being changed
            within the client_number_edit, it will set the row count of
            the table to 0 which will result in all the previous entries
            being removed from the table to allow for new information
            to be inputted for the next client search.

        Returns:
            None
        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row:int, column:int) -> None:
        """
        Description:
            This method runs in the event of a cell of the table being
            clicked, it will check the contents of the clicked row and
            column checking to see if the contents of the selected cell
            is a account_number. If it is, it will open the selected
            account in a separate account detail window and trigger the
            method to update the account with the result of the separate
            account detail window.

        Args:
            row (int): The row of the selected cell.
            column (int): The column of the selected cell

        Returns:
            None
        """
        selected_account_number = self.account_table.item(row, column).text()

        if selected_account_number == "":
            QMessageBox.information(self, "Invalid Selection",
            "Please select a valid record.")

        if selected_account_number in self.__accounts:
            focused_account = self.__accounts[selected_account_number]

            account_detail = AccountDetailsWindow(focused_account)
            account_detail.balance_updated.connect(self.__update_data)
            account_detail.exec_()

        else:
            QMessageBox.information(self, "No Bank Account",
            "Bank Account selected does not exist.")

    @Slot(BankAccount)
    def __update_data(self, account:BankAccount) -> None:
        """
        Description:
            This method is in charge of updating the selected
            BankAccount with the changed values received from the
            separate account detail window. It also runs the
            update_date function from the manage_data.py which updates
            the csv file storing the new current balance of any account
            that will be changed.

        Returns:
            None
        """
        for row in range(self.account_table.rowCount()):
            if self.account_table.item(row, 0).text() == \
                str(account.account_number):
                this_account = self.account_table.item(row, 0).text()
                self.__accounts[this_account] = account
                update_data(account)
