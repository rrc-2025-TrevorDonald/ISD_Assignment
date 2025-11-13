__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Trevor Donald"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)
    def __init__(self, account:BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):
            self.__account = copy.deepcopy(account)
            self.account_number_label.setText(
                str(self.__account.account_number))
            self.balance_label.setText(f"${self.__account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()

    @Slot()
    def __on_apply_transaction(self) -> None:
        """
        Description:
            This method is responsible for applying a transaction to the
            given BankAccount received by the __on_select_account from
            the client lookup window. It will take the amount inputted
            into the transaction_amount_edit input and either deposit
            or withdraw that value depending on if the user click the
            deposit or withdraw button. It then emits the signal back
            to the client lookup window for the __update_data method to
            run and update the table and csv file with the changes.

        Returns:
            None
        """
        try:
            edit_amount = float(self.transaction_amount_edit.text())
        except:
            QMessageBox.information(self, "Invalid Data",
            "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.__account.deposit(edit_amount)
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.__account.withdraw(edit_amount)

            self.balance_label.setText(f"${self.__account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            self.balance_updated.emit(self.__account)
        except Exception as e:
            QMessageBox.information(self, f"{self.sender().text()} Failed",
            f"{e}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    @Slot()
    def __on_exit(self) -> None:
        """
        Description:
            This method is responsible for closing the account detail
            window whenever it is called.

        Returns:
            None
        """
        self.close()
