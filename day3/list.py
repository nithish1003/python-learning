
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

for i in products:
    print(i)
product=input("enter product")
cart=[]
cart.append(product)
print(cart)



products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
cart = []
product=input("enter product name")
if product in products:
    cart.append(product)
    print(cart)
    print('Product added successfully!')
else:
    print('Product not added!')

cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse"]

cart_input=input("enter cart input")
if cart_input in cart:
    cart.remove(cart_input)
    print('cart removed')
    print(f'cart final {cart}')
else:
    print('cart_input not in cart')

cart = ["Laptop", "Mouse", "Keyboard", "Mouse", "Monitor", "Mouse"]

user_input=input('enter your cart')
if user_input in cart:
   result=cart.count(user_input)
   print(result)

salaries = [25000, 35000, 28000, 50000, 42000]
result=sorted(salaries)
print(result)

salaries = [25000, 35000, 28000, 50000, 42000, 35000, 25000]
unique=[]
for sal in salaries:
    if sal not in unique:
        unique.append(sal)
print(unique)

employees = ["Arun", "Bala", "Kumar", "Priya", "Ravi", "Divya", "Sanjay"]

result=employees[0:3]
print(result)

employees = ["Arun", "Bala", "Kumar", "Priya", "Ravi"]
rev=employees[::-1]
print(rev)

salaries = [25000, 45000, 32000, 60000, 38000]
result= max(salaries)
print(result)
salaries = [25000, 45000, 32000, 60000, 38000]
result=sum(salaries)
print(result)
employee_ids = [101, 102, 103, 101, 104, 102, 105]
result=set(employee_ids)
print(result)
employee_ids = {101, 102, 103, 104}
employee_ids.add(105)
print(employee_ids)