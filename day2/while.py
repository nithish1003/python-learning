# Problem 1: Bank ATM PIN Verification
# You are developing an ATM login system.
#
# A customer has to enter their PIN to access their bank account.
# Requirements
# 1. Store the correct PIN as 1234.
# 2. Ask the user to enter their PIN.
# 3. If the PIN is incorrect, display "Incorrect PIN. Try again."
# 4. Allow the customer to retry until they enter the correct PIN.
# 5. When the correct PIN is entered, display "Login successful!"
# from day2.forloop import withdrawal_Amount
# from day2.conditonal_staement import balance, withdrawal
# from day2.forloop import deposit_Amount

# pin=1234
# entred_pin=int(input('enter pin number: '))
#
# while pin!=entred_pin:
#     print(f'entred incorrect pin number: {entred_pin}')
#     entred_pin=int(input('enter pin number: '))
# print(f'pin number successfully entered: {pin}')
# You are building an ATM withdrawal system.
#
# Initial bank balance = ₹10,000.
## Ask the customer to enter a withdrawal amount.
# # If the withdrawal amount is greater than the available balance, display "Insufficient balance!".
# #
# # Ask the customer to enter another amount.
# # #
# # # Continue asking until the customer enters a valid amount.
# # # # Deduct the amount from the balance.
# # # # # Display the remaining balance


# balance=10000
# withdrawal_Amount=int(input("Enter withdrawal amount: "))
# while withdrawal_Amount>balance:
#     print('enter sufficeint balance')
#     withdrawal_Amount=int(input("Enter withdrawal amount: "))
# balance -= withdrawal_Amount
# print(f'withdrawal successfull {withdrawal_Amount} {balance}')


# Scenario: You are developing a simple banking transaction system.
#
# The customer's initial balance is ₹10,000.
#
# Your program must allow the customer to perform multiple transactions until they choose to exit.
#
# Requirements:
# 1. Display a menu:
#    - 1 – Deposit
#    - 2 – Withdraw
#    - 3 – Check Balance
#    - 4 – Exit
# 2. Ask the user to enter their choice.
# 3. For Deposit:
#    - Ask for the deposit amount.
#    - Add it to the balance.
#    - Display the updated balance.
# 4. For Withdraw:
#    - Ask for the withdrawal amount.
#    - If the amount exceeds the balance, display Insufficient balance.
#    - Otherwise, deduct it and display the updated balance.
# 5. For Check Balance:
#    - Display the current balance.
# 6. For Exit:
#    - Display Thank you for using our banking system! and stop the program.
# 7. If the user enters an invalid menu choice, display Invalid choice.
# Example execution:
#
#

balance=10000

display=input('enter deposit,withdrawal,check balance,exit')
while display!='exit':

    if display=='deposit':
        deposit_Amount=int(input('enter deposit amount'))
        balance+=deposit_Amount
    elif display=='withdrawal':
        withdraw_Amount=int(input('enter withdrawal amount'))
        balance-=withdraw_Amount
    elif display=='check balance':
        print(balance)
    elif display=='exit':
        print('Thank you for using our banking system!')

    else:
        print('invalid input')
print(f'balance: {balance}')
print(f'deposit amount: {deposit_Amount}')
print(f'withdrawal amount: {withdraw_Amount}')





