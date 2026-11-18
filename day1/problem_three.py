# Problem: Bank Loan Repayment Calculator
# A bank provides a personal loan to a customer. You need to calculate the monthly repayment details.
#
# Given details:
# - Loan amount: ₹500,000
# - Annual interest rate: 12%
# - Loan duration: 2 years
# - Processing fee: ₹2,000

# Stores all the given values in variables.
# Calculates the total interest using simple interest.
#
# Formula: \(SI = \frac{P \times R \times T}{100}\)
#
# Calculates the total repayment amount (loan + interest).
#
# Calculates the monthly EMI (total repayment / total months).
# Calculates the tota
# Displays all calculated values.l amount including the processing fee.

loan_amount=500000
annual_interest=12
loan_duration=2
processing_fee=2000
total_month=12
total_interest = loan_amount * annual_interest / 100 * loan_duration
total_repayment = loan_amount + total_interest

monthy_emi=total_repayment/(total_month*loan_duration)
total_amount=total_repayment+processing_fee
print(total_amount)
print(monthy_emi)
print(total_interest)
print(total_repayment)
print(loan_amount)










