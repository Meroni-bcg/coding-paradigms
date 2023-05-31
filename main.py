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

#Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

        # Create an instance of AnakinsPod
anakins_pod = AnakinsPod(1000, "perfect", 50000)

# Access attributes of AnakinsPod
print(anakins_pod.max_speed)     # Output: 1000
print(anakins_pod.condition)     # Output: perfect
print(anakins_pod.price)         # Output: 50000

# Use the boost
anakins_pod.boost()

# Access the updated max_speed attribute
print(anakins_pod.max_speed)     # Output: 2000

#Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, podracer):
        podracer.condition = "trashed"

# Creating instances of the SebulbasPod and Podracer classes and use the flame_jet()
# Create an instance of SebulbasPod
sebulbas_pod = SebulbasPod(1200, "perfect", 60000)

# Create another Podracer instance
other_podracer = Podracer(1000, "good", 50000)

# Access attributes of SebulbasPod
print(sebulbas_pod.max_speed)     # Output: 1200
print(sebulbas_pod.condition)     # Output: perfect
print(sebulbas_pod.price)         # Output: 60000

# Access attributes of the other Podracer
print(other_podracer.max_speed)    # Output: 1000
print(other_podracer.condition)    # Output: good
print(other_podracer.price)        # Output: 50000

# Use the flame_jet to update the condition of the other Podracer
sebulbas_pod.flame_jet(other_podracer)

# Access the updated condition of the other Podracer
print(other_podracer.condition)    # Output: trashed

