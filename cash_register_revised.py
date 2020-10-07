#hip_hw_2
total = (0)
tax = (1.095)
#title
print("Cash Register #3")
#instruction
print("Enter Prices Individually, When Done Enter 0")
#input, save and add prices, make input get turned into float. with correct format.
item_price = float(input("Item Price: $"))
total += item_price
while item_price > 0:
  item_price = float(input("Item Price: $"))
  total += item_price
print("Your total is $",format(total,",.2f"),sep="")
#ask for sales tax
sales_tax = input("Is Sales Tax Applied? (y/n) ")
if sales_tax == "y":
#save the multiplication when adding tax
  total *= tax
  print("Your Total + Tax is $",format(total,",.2f"),sep="" )
else:
  print("Your Total is $",format(total,",.2f"),sep="")
#ask for your money and return change
cash = float(input("Pay $"))
#while loop for paying under until owed >= 0
while cash < total:
  print("Your total is $", format(total - cash,",.2f"),sep="")
  total -= cash
  cash = float(input("Pay $"))
#providing change to any number greater than the toal
if cash > total:
  change = cash - total
  print("Your Change is $",format(change,",.2f"),sep="")
  print ("Thank you!")
#no change provide for paying exact.
elif cash == total:
  print("Exact change was provided.")
  print("Thank you!")





























