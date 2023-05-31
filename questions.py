# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

# Encapsulation is demonstrated in this code because, the Podracer, AnakinsPod, and SebulbasPod classes encapsulate data (attributes) and methods relevant to a podracer. The attributes (max_speed, condition, price) are encapsulated within each class, and the methods (repair(), boost(), flame_jet()) operate on the encapsulated data.

# Inheritance is demostrated because both the AnakinsPod and SebulbasPod classes inherit from the Podracer class. By inheriting from Podracer, they inherit its attributes (max_speed, condition, price) and any methods defined in the Podracer class.

# Polymorphism is demonstrated because despite sharing the same method name, each class defines a different behavior for both the AnakinsPod and SebulbasPod classes. They have their own implementations of the boost() and flame_jet() methods.

# Abstraction is not portrayed in this code. 