# # Feyza Atabey
# Receipt and Pricing - Lab 1

# Ask the user for the price of 3 items, by prompting the user and reading in one price at a time. 
berry = float(input("Please enter a price:"))
orange =  float(input("Please enter a price:"))
carrot =  float(input("Please enter a price:"))
# Print the subtotal of the 3 prices, with a text explanation of the number being printed. See the sample output.  
subtotal= berry + orange + carrot
print("Your subtotal is:", round(subtotal,2))
# Give the user a 10% discount on the subtotal. 
discount= subtotal*0.9
# Print the subtotal after discount, with a text explanation. 
print("Your total after discount is:",round(discount, 2))
# Add 8.75% tax to the subtotal. 
tax= discount*1.0875
# Print the total price after tax, with a text explanation.
print("Your total price after tax is:", round(tax,2))
# Ask the user for a payment and read it in.
payment=float(input("Please insert your bill:"))
# Print the amount of change, with a text explanation.  
#print("Your change is:",(payment-tax))
rounded_amount = round((payment-tax), 2)
print("Your change is:", rounded_amount)
#E. Optional extra credit (2 pts):
#Print the change as number of dollars and cents
#Only use arithmetic concepts that have been covered in the reading to separate the change amount into dollars and cents.
dollar= rounded_amount // 1
cents= rounded_amount % 1
print( " Your total amount is" , int(dollar) , "dollars and", int(cents*100), "cents")