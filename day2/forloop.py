Write a Python program that asks the user to enter their personal and academic information and displays it in a formatted output
for i in range(1, 11):
    salary = int(input(f"Enter salary of employee {i}: "))
    print(f"Employee {i}: {salary}")
Write a Python program that accepts salaries from 5 employees and calculates:
1. Total salary paid.
2. Average salary.
3. Highest salary.
4. Lowest salary
total_salary=0
highest_salary=0
lowest_salary=0
for i in range(1,6):
    salary=int(input(f"Enter your salary {i}: "))
    total_salary+=salary
    if i==1:
        highest_salary=salary
        lowest_salary=salary
    else:
        if salary>highest_salary:
           highest_salary=salary
        if salary<lowest_salary:
           lowest_salary=salary

average_salary=total_salary/5
print("Total Salary:", total_salary)
print("Average Salary:", average_salary)
print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)

A bank wants to process 5 transactions from a customer.

Write a Python program that accepts 5 transaction amounts and determines whether each transaction is a deposit or withdrawal.
- Positive amount = Deposit
- Negative amount = Withdrawal
At the end, calculate:
1. Total deposited amount.
2. Total withdrawn amount (display as a positive number).
3. Final account balance.

deposit_Amount=0
withdrawal_Amount=0
for i in range(1,6):
    transaction_amount=int(input(f"Enter your transaction amount {i} : "))
    if transaction_amount>0:
        deposit_Amount=deposit_Amount+transaction_amount
    else:
        withdrawal_Amount=withdrawal_Amount+transaction_amount
final_balance=deposit_Amount-withdrawal_Amount
print(f'deposit Amount : {deposit_Amount}')
print(f'withdrawal Amount : {withdrawal_Amount}')


This is your final challenge for the Loops topic.
Problem statement
A company has 3 departments, and each department has 3 employees.

Write a Python program to collect each employee's attendance status for one day.
- 1 = Present
- 0 = Absent
Your program must calculate the attendance report for each department.

total_present = 0
total_absent = 0

for i in range(1, 4):

    present = 0
    absent = 0

    for j in range(1, 4):

        attendance = input(
            f"Department {i}, Employee {j}: "
        ).lower()

        if attendance == 'present':
            present += 1
            total_present += 1

        elif attendance == 'absent':
            absent += 1
            total_absent += 1

    print(f"\nDepartment {i}")
    print(f"Present: {present}")
    print(f"Absent: {absent}")

print("\n========== TOTAL REPORT ==========")
print(f"Total Present: {total_present}")
print(f"Total Absent: {total_absent}")