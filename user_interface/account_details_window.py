__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
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
    def __on_apply_transaction(self):
        """
        """
        try:
            edit_amount = float(self.transaction_amount_edit.text())
        except:
            QMessageBox.information(None, "Invalid Data",
            "Amount must be numeric.", QMessageBox.Yes, QMessageBox.Yes)
            self.transaction_amount_edit.focus()

        try:
            if self.sender(self.deposit_button):
                transaction_type = "Deposit"
                self.__account.deposit(edit_amount)
            elif self.sender(self.withdraw_button):
                transaction_type = "Withdraw"
                self.__account.withdraw(edit_amount)

            self.balance_label.setText(f"${self.__account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.focus()
        except Exception as e:
            QMessageBox.information(None, f"{transaction_type} Failed",
            f"e", QMessageBox.Yes, QMessageBox.Yes)
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.focus()