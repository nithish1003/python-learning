# Problem: Employee Salary Calculator
# A company calculates an employee's monthly salary based on the following details:
# - Basic salary: ₹35,000
# - HRA: 20% of basic salary
# - DA: 10% of basic salary
# - Professional tax: ₹200
# - Provident Fund (PF): 12% of basic salary
# Your task:
#
# Write a Python program that:
# 1. Stores all the given values in variables.
# 2. Calculates HRA.
# 3. Calculates DA.
# 4. Calculates PF.
# 5. Calculates gross salary (Basic + HRA + DA).
# 6. Calculates net salary after deducting PF and professional tax.
# 7. Displays gross salary and net salary.
# Expected output format:
# HRA: ₹7000
# DA: ₹3500
# PF: ₹4200
# Gross Salary: ₹45500
# Net Salary: ₹41100


salary=35000
hra=salary*20/100
print('hra',hra)
da=salary*10/100
print('da',da)
professional_tax=200
pf=salary*12/100
print('pf',pf)
gross_salary=salary+hra+da
print('gross_salary',gross_salary)
net_salary=gross_salary-pf-professional_tax
print('net_salary',net_salary)
