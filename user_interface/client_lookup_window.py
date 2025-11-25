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

        self.filter_button.clicked.connect(self.__on_filter_clicked)

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
            self.__toggle_filter(False)

        for key in self.__accounts.items():
            if key[1].client_number == entered_client_number_int:
                rows = QTableWidget.rowCount(self.account_table)
                self.account_table.insertRow(rows)

                account_number = QTableWidgetItem(str(key[1].account_number))
                balance = QTableWidgetItem(f"${key[1].balance:,.2f}")
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
        column = 0
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

    @Slot()
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
            if (self.account_table.item(row, 0).text() ==
                str(account.account_number)):
                updated_account = QTableWidgetItem(f"${account.balance:,.2f}")
                self.account_table.setItem(row, 1, updated_account)
                self.__accounts[account.account_number] = account
                update_data(account)

    @Slot()
    def __on_filter_clicked(self) -> None:
        """
        Description:
            This method is responsible for checking the state of the
            filter_button, if the state is Apply Filter it will take the
            entered criteria of filter_edit and append all accounts
            that are shown in the account_table that match the criteria
            and append them to a list. It then compares that list and
            hides all of the rows that contents do not match the created
            list and tells the __toggle_filter method to change to the
            "reset" option. If the state is not Apply Filter it tells
            tells the __toggle_filter method reset the filter sections
            to the default.

        Returns:
            None
        """
        filter_state = self.filter_button.text()

        if filter_state == "Apply Filter":
            to_be_reset = True
            displayed_accounts = {}
            inputted_filter_text = self.filter_edit.text().lower()
            inputted_filter_type = self.filter_combo_box.currentIndex()

            for row in range(self.account_table.rowCount()):
                if inputted_filter_text in (self.account_table.item(row,
                   inputted_filter_type).text().strip("$").replace(",", "")
                   .lower()):
                    taken_row = self.account_table.item(row, 0).text()
                    displayed_accounts[taken_row] = self.__accounts[taken_row]

            print(inputted_filter_text)
            print(inputted_filter_type)
            print(displayed_accounts)

            for row in range(self.account_table.rowCount()):
                if (self.account_table.item(row, 0).text()
                    not in displayed_accounts):
                    self.account_table.setRowHidden(row, True)

        else:
            to_be_reset = False

        self.__toggle_filter(to_be_reset)

    def __toggle_filter(self, filter_on:bool) -> None:
        """
        Description:
            The method that is responsible to handling the state of the
            filter section, if you have entered a filter option and
            clicked apply filter this method will change the display of
            the filter section to disable the combo box and input and
            replace the apply filter button with a reset button. Then if
            you hit the reset button will reset the filter section back
            to the "default" where you can filter.

        Args:
            filter_on (bool): A boolean that is used to determine if the
            method resets the filter section to default or displays the
            reset filter option.

        Returns:
            None
        """
        self.filter_button.setEnabled(True)
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setDisabled(True)
            self.filter_edit.setDisabled(True)
            self.filter_label.setText("Data is Currently Filtered")

        else:
            self.filter_button.setText("Apply Filter")

            self.filter_combo_box.setEnabled(True)
            self.filter_combo_box.setCurrentIndex(0)

            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")
