#title

print("Hello, Welcome to the Cash Registry")
#instructions

print("Enter in the prices individually, when done enter 0")
#get input on price_item_1

#i need to make price_item_1 a float so the if statement can recognize it.

price_item_1 = float(input("First item price: $"))
#what if they try to get the item price to 0?

if price_item_1 == 0:
  print("Error! Try Again.")
# It works! Now, what if price_item_1 is greater than or equal to 1? this is where you use elif

elif price_item_1 >= 1:
  #get input for price item 2 and make it a float

  price_item_2 = float(input("Additional item prices: $"))
  #It works!

#add them together to get the total and make it a variable

total = price_item_1 + price_item_2
print("Your total is: $",total)
#ask it sales tax is applied.

tax = input("Is sales tax applied? (y/n) ")
#what if sales tax is yes?

if tax == "y":
  #apply sales tax to the total

  total *= 1.095
  #use round to round the sales tax total to the nearest hundredth

  print("With sales tax your new total is $",round(total, 2))
  #Now make a way to pay by taking the user input and saving it as cash_handed_over

  #Make cash_handed_over a float

  cash_handed_over = float(input("You give the cashier: $"))
  #check to see it it works

  print("The cashier recieved your $",cash_handed_over,"dollars")
  #It works!

  #what if you short the cashier?
  if cash_handed_over < total:
    debt = total - cash_handed_over
    print("Your debt is, $",round(debt, 2))
    #round the debt up to the hundredth place, now make them pay the debt.

    #make clear_debt a float.
    clear_debt = float(input("You hand over: $"))
    #now if they hand over the wrong amount of debt kick them out.debt
    if clear_debt < debt:
      print("Error! Shorting the Cashier is not allowed! Next time, provide exact or more change.")
      #if they give you exact debt
    elif clear_debt == debt:
      print("Thank you for exact change! Have a nice day!")
    # if they give you more than what it owed, provide change.
    else:
        change = clear_debt - debt
        print("Your change is $",round(change, 2), "have a nice day!")

  else: 
  #Calculate change
    change = cash_handed_over - total
    print("Your change is $",round(change, 2), "have a nice day!")
  #It works!

  #Now what it they type "n" to the sales tax?
else:
  print("Your due total is: $",total)
  #print the total without the sales tax and pay with cash_handed_over and make it a float

  cash_handed_over = float(input("You give the cashier: $"))
  #make sure the cashier recieves the money

  print("the cashier recieved your: $",cash_handed_over)

  if cash_handed_over < total:
    debt = total - cash_handed_over
    print("Your debt is, $",round(debt, 2))
    #round the debt up to the hundredth place, now make them pay the debt.

    #make clear_debt a float.
    clear_debt = float(input("You hand over: $"))
    #now if they hand over the wrong amount of debt kick them out.debt
    if clear_debt < debt:
      print("Error! Shorting the Cashier is not allowed! Next time, provide exact or more change.")
      #if they give you exact debt
    elif clear_debt == debt:
      print("Thank you for exact change! Have a nice day!")
    # if they give you more than what it owed, provide change.
    else:
        change = clear_debt - debt
        print("Your change is $",round(change, 2), "have a nice day!")

  #Calculate change.
  else:
    change = cash_handed_over - total
    print("Your change is $",round(change, 2), "have a nice day!")