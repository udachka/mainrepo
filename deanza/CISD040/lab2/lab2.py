# Feyza Atabey 
# Lab 2 - Cost of Car Insurance and Information of Car Costs

# A.
#Ask the user for their name
age = int(input("Please enter your age : "))
# Ask the user if they have had an accident in the last two years
accident = input("Have you been in an accident in last two years? (yes/no) : ").lower( )
# Determine the insurance cost based on age and accident history
if 16 <= age <= 25:
    if accident == "no":
        cost = 3000
    else:
        cost = 3500
elif 26 <= age <= 45:
    if accident == "no":
        cost = 2000
    else:
        cost = 2500
elif age >= 46:
    if accident == "no":
        cost = 1200
    else:
        cost = 1500
else:
    cost = "Invalid age or accident input."

#PRint the insurance cost
print(f"Your insurance cost is: ${cost}")

# B.

# Ask the user for the prices of three cars
car_price1 = float(input("Please enter the price of the first car: "))
car_price2 = float(input("Please enter the price of the second car: "))
car_price3 = float(input("Please enter the price of the third car: "))

# Create a list with all 3 car prices
car_prices = [car_price1, car_price2, car_price3]

# Calculate the maximum, minimum, difference, and total cost
max_cost = max(car_prices)
min_cost = min(car_prices)
cost_difference = max_cost - min_cost
total_cost = sum(car_prices)

# Store the information in a dictionary
car_costs_info = {
        "maximum cost": max_cost,
        "minimum cost": min_cost,
        "cost difference": cost_difference,
        "total cost": total_cost
    }

# Print out the car cost information
print(f"Maximum cost: ${max_cost}")
print(f"Minimum cost: ${min_cost}")
print(f"Difference between maximum and minimum cost: ${cost_difference}")
print(f"Total cost of all three cars: ${total_cost}")