# Problem: Banking Transaction Validation
#
# A bank allows a customer to withdraw money only when:
# - The withdrawal amount is greater than zero.
# - The withdrawal amount does not exceed the account balance.
# - The account balance is at least the requested withdrawal amount

balance = int(input("Enter your balance: "))
withdrawal = int(input("Enter your withdrawal: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount")

elif withdrawal > balance:
    print("Insufficient balance")

else:
    balance -= withdrawal
    print("Withdrawal successful!")
    print(f"Remaining balance: {balance}")
# from day2.forloop import total_salary
#
# Intermediate
#  Nested if + multiple conditions
#
# Problem: Employee Bonus Eligibility System
# A company wants to calculate employee bonuses based on performance and experience.
# Problem statement
# Write a Python program that accepts:
# 1. Employee name
# 2. Years of experience
# 3. Performance rating (1–5)
# 4. Monthly salary
# Apply these rules:
# Condition	Bonus
# Experience 5+ years AND rating 5	20%
# Experience 3+ years AND rating 4	15%
# Experience 1+ years AND rating 3	10%
# Any other combination	No bonus
employee = input("Enter employee name: ")
experience = int(input("Enter experience years: "))
monthly_salary = int(input("Enter monthly salary: "))
rating = int(input("Enter rating (1-5): "))

if rating < 1 or rating > 5:
    print("Invalid rating")

elif experience >= 5 and rating == 5:
    bonus = monthly_salary * 20 / 100
    total_salary = monthly_salary + bonus

    print(f"Employee: {employee}")
    print(f"Monthly salary: {monthly_salary}")
    print(f"Bonus: {bonus}")
    print(f"Total salary: {total_salary}")

elif experience >= 3 and rating == 4:
    bonus = monthly_salary * 15 / 100
    total_salary = monthly_salary + bonus

    print(f"Employee: {employee}")
    print(f"Monthly salary: {monthly_salary}")
    print(f"Bonus: {bonus}")
    print(f"Total salary: {total_salary}")

elif experience >= 1 and rating == 3:
    bonus = monthly_salary * 10 / 100
    total_salary = monthly_salary + bonus

    print(f"Employee: {employee}")
    print(f"Monthly salary: {monthly_salary}")
    print(f"Bonus: {bonus}")
    print(f"Total salary: {total_salary}")

else:
    print(f"Employee: {employee}")
    print("Not eligible for bonus")
    print(f"Monthly salary: {monthly_salary}")
    print(f"Total salary: {monthly_salary}")