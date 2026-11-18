# Problem: Employee Shift Scheduling
# A company has 157 employees. Each shift can accommodate 12 employees.
#
# Write a Python program to calculate:
# 1. How many complete shifts can be formed?
# 2. How many employees will remain without a complete shift?
# 3. How many additional employees are required to fill one more complete shift?
employee=157
person_per_shift=12
total_shift=employee//person_per_shift
print(total_shift)
employee_remain=employee%person_per_shift
print(employee_remain)
complete_shift=person_per_shift-employee_remain
print(complete_shift)