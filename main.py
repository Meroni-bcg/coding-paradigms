# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

# Create a Podracer instance
my_podracer = Podracer(1000, "perfect", 50000)

# Access the attributes
print(my_podracer.max_speed)   # Output: 1000
print(my_podracer.condition)   # Output: perfect
print(my_podracer.price)       # Output: 50000


#Define a repair() method that will update the condition of the podracer to "repaired".

def repair(self):
        self.condition = "repaired"
