# devops class week 1 

#3/20
#3/21


#3/22
# make projects for resume + matters more than experience

# Garage door , test case writing
'''Test Case 1
TestCaseID: TC001
Title: Open Garage Door Successfully
Pre-requisite: Garage door is initially closed.
Steps: Click the button once.
Expected Result: The garage door opens completely within 10 seconds.
Test Case 2
TestCaseID: TC002
Title: Close Garage Door Successfully
Pre-requisite: Garage door is initially open.
Steps: Click the button once.
Expected Result: The garage door closes completely within 10 seconds.
Test Case 3
TestCaseID: TC003
Title: Pause Garage Door While Opening
Pre-requisite: Garage door is initially closed.
Steps:
Click the button to start opening the door.
Click the button again before the door fully opens.
Expected Result: The garage door pauses its opening action.
Test Case 4
TestCaseID: TC004
Title: Pause Garage Door While Closing
Pre-requisite: Garage door is initially open.
Steps:
Click the button to start closing the door.
Click the button again before the door fully closes.
Expected Result: The garage door pauses its closing action.
Test Case 5
TestCaseID: TC005
Title: Reverse Door Direction From Opening to Closing
Pre-requisite: Garage door is in the process of opening.
Steps:
Click the button to pause the opening action.
Click the button again after the pause.
Expected Result: The garage door starts closing.
Test Case 6
TestCaseID: TC006
Title: Reverse Door Direction From Closing to Opening
Pre-requisite: Garage door is in the process of closing.
Steps:
Click the button to pause the closing action.
Click the button again after the pause.
Expected Result: The garage door starts opening.
Test Case 7
TestCaseID: TC007
Title: Continuous Operation Without Interruption
Pre-requisite: Garage door is initially closed.
Steps:
Click the button to open the door and wait for it to fully open without interruption.
Once open, click the button to close the door and wait for it to fully close without interruption.
Expected Result: The garage door opens and then closes completely, each action taking exactly 10 seconds without any pauses.
Test Case 8
TestCaseID: TC008
Title: Rapid Clicks Handling
Pre-requisite: Garage door is initially closed.
Steps:
Click the button four times rapidly at the start.
Expected Result: The garage door begins to open, pauses, and then depending on the timing of the clicks, 
may start to close or pause again, demonstrating the system's handling of rapid inputs.'''

import time

class GarageDoor:
    def __init__(self):
        self.state = 'closed' #possible states: open, closed, opening, closing, paused
        self.action = None # tracks the current action
    
    def click_button(self):
        if self.state in ['closed', 'open']:
            self.action = 'opening' if self.state == 'closed' else 'closing'
            self.state = self.action
            print(f"Door started {self.action}")
        elif self.state in ['opening', 'closing']:
            self.state = 'paused'
            print("Door paused")
        elif self.state == 'paused':
            self.action = ' closing' if self.action == 'opening' else 'opening'
            self.state = self.action
            print(f"Door is reversed and started {self.action}")
    
    def simulate_time_passage(self, seconds):
        print(f"Simulating time passage of {seconds} seconds for {self.action}. ")
        if self.action == 'opening':
            self.state = 'open'
        elif self.action == 'closing':
            self.state == 'closed'
        print(f"Door is now {self.state}")

    def status(self):
        return self.state
    
# Simulating test cases
door = GarageDoor()

# TC001: Open Garage Door Successfully
door.click_button()
door.simulate_time_passage(10)

# TC003: Pause Garage Door While Opening
door.click_button()  # Assuming it's starting from closed as per pre-requisite reset
door.click_button()  # Pause it
door.simulate_time_passage(5)  # Simulate half-way, though not necessary as we control state change manually
door.click_button()  # Resume in the opposite direction
door.simulate_time_passage(10)


