sale_amount = int(input("Enter the amount: "))
actual_cost = int(input("Enter the amiunt: "))

if sale_amount > actual_cost:
   amount = sale_amount - actual_cost
   print("Profit is {0}".format(amount))
else:
   print("No profit is made.")