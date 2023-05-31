# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

# Encapsulation is demonstrated in this code because, the Podracer, AnakinsPod, and SebulbasPod classes encapsulate data (attributes) and methods relevant to a podracer. The attributes (max_speed, condition, price) are encapsulated within each class, and the methods (repair(), boost(), flame_jet()) operate on the encapsulated data.

# Inheritance is demostrated because both the AnakinsPod and SebulbasPod classes inherit from the Podracer class. By inheriting from Podracer, they inherit its attributes (max_speed, condition, price) and any methods defined in the Podracer class.

# Polymorphism is demonstrated because despite sharing the same method name, each class defines a different behavior for both the AnakinsPod and SebulbasPod classes. They have their own implementations of the boost() and flame_jet() methods.

# Abstraction is not portrayed in this code. 

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

# Although other coding styles, like functional programming, can be valid options, they may not offer the equivalent level of organization, reusability, and adaptability provided by OOP. The modular design of OOP, coupled with principles like encapsulation, inheritance, and polymorphism, are well-suited to meet the requirements of the problem, making OOP an appropriate and efficient choice for implementing the solution.

# How in particular did Object Oriented Programming assist in the solving of this problem?

# Object-oriented programming (OOP) played a crucial role in solving this problem by providing several benefits. First, OOP facilitated code organization and maintainability through the modular and encapsulated nature of classes. This allowed for the grouping of related data and behaviors, making it easier to understand and work with individual objects. Second, OOP promoted code reuse through inheritance, enabling the child classes to inherit attributes and methods from the parent class. This avoided repetitive code and improved development efficiency. Third, the inheritance mechanism in OOP established a hierarchical relationship between classes, ensuring consistency and promoting code reuse. Fourth, polymorphism in OOP allowed different objects to respond to the same method name in their own specialized way. This flexibility enabled diverse behaviors while adhering to a common interface. Fifth, OOP facilitated the creation of specialized classes with unique functionalities, such as the AnakinsPod and SebulbasPod, which inherited from the base Podracer class. Finally, the OOP approach simplified the implementation, enhanced code organization, and provided a solid foundation for extending and maintaining the system in the future.