# An online shopping application needs to calculate a customer's final bill.
#
# A customer purchases 4 products, each costing ₹850.
#
# The store provides a 12% discount on the total product price. A delivery charge of ₹75 is added after applying the discount.
# Stores the product price, quantity, discount percentage and delivery charge in variables.
# Calculates the total product cost.
# Calculates the discount amount.
# Calculates the final bill after discount and delivery charge.
# Displays all three amounts



product_count=4
cost=850
discount=12
delivery=75
total_product_cost=product_count*cost
discount_amount=total_product_cost*discount/100
final_bill=total_product_cost-discount_amount+delivery
print(total_product_cost)
print(final_bill)
print(discount_amount)








