# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build
on the work done in the previous assignment(s). Ultimately, an entire system will be created to
manage bank transactions for clients who have one or more bank accounts.

## Author

Trevor Donald

## Assignment 1

Assignment 01: Client and BankAccount

## Encapsulation

Encapsulation was achieved by using hidden/private variables, using the double underscore prefix
"Name Mangling" for example when defining a variable for client we want the information to be
private and not accessible without the use of a setter or getter so when defining the client_number
we would set it to be "__client_number".

## Assignment 2: Inheritance with parent/child classes

Polymorphism was achieved by the Child/Sub classes ChequingAccount, InvestmentAccount and SavingsAccount
inheriting the abstract method get_service_charges from the Parent/Super class BankAccount. The method
is used in different ways depending of the instance of the class initialized but is still a method of
any type of bank account. When using get_service_charge within a ChequingAccount it checks to see if the
balance is above the overdraft_limit it the service_charge will be the BASE_SERVICE_CHARGE (0.50) set by
the Parent/Super class of BankAccount, if the balance is lower than the the overdraft_limit it will
subtract the balance with the overdraft_limit then multiply that amount by the overdraft rate and then
add the BASE_SERVICE_CHARGE. When using get_service_charge within a InvestmentAccount if the account was
created 10 or more years earlier the service_charge will be the BASE_SERVICE_CHARGE, if the account is
newer than 10 years the service_charge will be the BASE_SERVICE_CHARGE plu the manager_fee. Finally when
using get_service_charge with a SavingsAccount if the balance is above the minimum_balance the
service_charge will be the BASE_SERVICE_CHARGE but if the balance is less than the minimum_balance the
service_charge will be the BASE_SERVICE_CHARGE multiplied by the SERVICE_CHARGE_PREMIUM (2.0) defined
by SavingsAccount class.

## Assignment 3: Design Patterns

## Strategy Pattern

The strategy pattern is being used within this project by taking the place of the previously created
method get_service_charge and making it more scalable and interchangeable. The ServiceChargeStrategy
class contains 3 child classes, the OverdraftStrategy handles the charges being applied to an account
thats balance is overdrawn past the assigned amount and applies the given overdraft rate to initiated
account. The ManagementFeeStrategy handles the fee applied to investment account and will check to
see if the account is more than 10 years old and handles the charge accordingly. Finally there is the
MinimumBalanceStrategy the handles the fee applied to a savings account if they have less than the
minimum balance and will apply the service charges accordingly.
