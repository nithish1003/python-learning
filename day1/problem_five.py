# Problem: Online Transaction Calculation
# A customer has ₹10,000 in their digital wallet.
#
# They perform the following transactions:
# - Purchase 3 products costing ₹1,250 each.
# - Receive a cashback of ₹300.
# - Pay a transaction fee of ₹50.
# - Receive a refund of ₹500.
# Write a Python program to calculate the final wallet balance using a single arithmetic expression.
#
# Conditions:
# 1. Use variables for all values.
# 2. Calculate the final balance in one expression.
# 3. Use parentheses to control calculation order.
# 4. Don't use if, loops or functions.
balance=10000
caskback=300
refund=500
transaction_fee=50
purchase=3*1250
final_balance=balance+caskback+refund-purchase-transaction_fee
print(final_balance)