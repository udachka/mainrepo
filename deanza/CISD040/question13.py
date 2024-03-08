#Feyza Atabey
# Question 13 make-up , highest high and lowest high temparatures

#1) Ask the user for daily high temperatures (you may make up the values) 
#for the following cities: New York, Los Angeles, Chicago, Houston, Phoenix.
new_york_temp=int(input("Enter the daily high temperature for New York: "))
los_angeles_temp=int(input("Enter the daily high temperature for Los Angeles: "))
chicago_temp=int(input("Enter the daily high temperature for Chicago: "))
houston_temp=int(input("Enter the daily high temperature for Houston: "))
phoenix_temp=int(input("Enter the daily high temperature for Phoenix: "))
#2) Store the value pairs in a container of your choosing (hint: which container type is best for key-value pairs?).
temperatures = {
    "New York": new_york_temp,
    "Los Angeles": los_angeles_temp,
    "Chicago": chicago_temp,
    "Houston": houston_temp,
    "Phoenix": phoenix_temp
}

#3) Print out the city names with the highest and lowest temperatures.
highest_temp_city = max(temperatures, key=temperatures.get)
lowest_temp_city = min(temperatures, key=temperatures.get)

print(f"The highest city temperature for the day is: {highest_temp_city}")
print(f"The lowest city temperature for the day is: {lowest_temp_city} ")