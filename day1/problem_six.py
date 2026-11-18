# Problem: ATM Cash Withdrawal System
# An ATM has a balance of ₹50,000. A customer requests ₹8,750.
#
# The ATM only dispenses cash in ₹500 notes and ₹100 notes.
#
# Your task is to write a Python program that calculates:
# 1. How many ₹500 notes are required?
# 2. How much money remains after dispensing ₹500 notes?
# 3. How many ₹100 notes are required?
# 4. What is the remaining amount that cannot be dispensed?
# 5. What is the total number of notes dispensed?

withdraw=8750
note1=500
note2=100
remain_500=withdraw%note1
print(remain_500)
remain_100=remain_500//note2
print(remain_100)
total_number_notes=remain_100+(withdraw//note1)
print(total_number_notes)
remain_amount=remain_500-remain_100*note2
print(remain_amount)
