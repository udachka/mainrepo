# Name : Feyza Atabey
# Lab 5 : Clock - date 


# B. B. Write a Python program (20 pts total) that will:
#- Create a Clock class
#- The clock class should have an init function that sets the hours, minutes, 
# and seconds and sets all of them to 0 by default. (5 points)

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

#- Write an instance method that prints out the current time in hours minutes and seconds in this format:
# hh:mm:ss. For example: 08:20:59. (5 points)
        
    def print_time(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

#- Write a instance method that changes the current time (hours, minutes, and seconds) of the Clock and prints
#out the new time with a quick message explaining that it's a new time. The format of the new time should also
#be hh:mm:ss. For example, the message can be "The new time is 04:30:30." (5 points)
    def change_time(self, new_hours, new_minutes, new_seconds):
        self._validate_time(new_hours, new_minutes, new_seconds)
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds
        print("The new time is ", end="")
        self.print_time()

#- Write exception handling on the above function that takes in input for the new time. The exception handling
#should raise a ValueError and check for the following: hours should be between 0 and 23, minutes should be
#between 0 and 59, and seconds should be between 0 and 59. (5 points)

    def _validate_time(self, hours, minutes, seconds):
        if not 0 <= hours <= 23:
            raise ValueError("Hours must be between 0 and 23.")
        if not 0 <= minutes <= 59:
            raise ValueError("Minutes must be between 0 and 59.")
        if not 0 <= seconds <= 59:
            raise ValueError("Seconds must be between 0 and 59.")

#usage
my_clock = Clock()
print("The current time is: ", end="")
my_clock.print_time() 

try:
    my_clock.change_time(25,30,45)
except ValueError as e:
    print("Error:", e)

try:
    my_clock.change_time(15, 30, 45)  
except ValueError as e:
    print("Error:", e)

print("After change, the current time is: ", end="")
my_clock.print_time()