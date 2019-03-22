# class Trainer():
#     trainer_count = 0 # class variable
#     #constructor
#     def __init__(self, name, age = 30): # parameters
#         # object variable declaration
#         self.name = name # trainer1.name = "Prasant"
#         self.age = age # trainer1.age = "25"
#         self.__salary = None # private object variable
#         Trainer.trainer_count += 1 #class obbject incrementation
    
#     def set_salary(self, salary):
#         self.__salary = salary]
    
#     def get_salary(self):
#         return self.__salary

# print(Trainer.trainer_count)
# trainer1 = Trainer("Prasant", 25) # arguments
# trainer1.set_salary(50000)
# print(Trainer.trainer_count)
# # print(trainer1.trainer_count,"trainer count used with object") # do not use it
# trainer2 = Trainer("Rojalin")
# print(Trainer.trainer_count)
# print(trainer1.name, trainer1.age, trainer1.get_salary())
# print(trainer2.name, trainer2.age)


# '''
# bdlnlanda
# as;ldma;sdmasdm
# ;ansdanasnkdalsdn
# laknlansdlansd
# '''
# """
# ;lamsd;almsd;lams
# a;sd;amsd;aslmd
# amd;alsmd;aslmd
# """

# a = '''
# bdlnlanda
# as;ldma;sdmasdm
# ;ansdanasnkdalsdn
# laknlansdlansd
# '''

# print(a, type(a))
# count = 0
# for i in a : 
#     if i == "\n":
#         count += 1
#         print(count)





# class Trainer():
#     def __init__(self, age = 20, height= None):
#         self.age = age
#         self.height = height
#         self.__name = None
#         self.__salary = None
        
#     def set_name(self, name): # mutators
#         self.__name = name

#     def get_name (self): # accessors
#         return self.__name

#     def set_salary(self, salary):
#         self.__salary = salary
    
#     def get_salary(self):
#         return self.__salary

# obj1 = Trainer(40, 4.9)
# obj2 = Trainer(height = 5.8, age=58)
# obj1.set_salary(50000)
# obj1.set_name("Prasant")
# obj2.set_name("Anusha")
# print(obj1.age)
# obj1.age = 40
# print(obj1.age, obj1.get_name(),obj1.height, obj1.get_salary())
# print(obj2.age, obj2.get_name(), obj2.height, obj2.get_salary())


# class Monkey():
#     def __init__(self):
#         self.breed = None
#         self.color = None

    # def ride_cycle(self):
    #     if (self.breed) == "Chimpanzee":
    #         print("Ride bicycle on a rope")
    #     else:
    #         print("Ride cycle")

# chimpu = Monkey() # chimpu is an object of the class Monkey
# chimpu.breed = "Chimpanzee"
# chimpu.color = "brown"
# chimpu.ride_cycle()
# print(chimpu.breed, chimpu.color)

# chimpu1 = Monkey() # chimpu is an object of the class Monkey
# chimpu1.breed = "Gorilla"
# chimpu1.color = "brown"
# chimpu1.ride_cycle()
# print(chimpu1.breed, chimpu1.color)


# class Employee:
#     __emp_count = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.__emp_count += 1
#
#     @staticmethod
#     def display_count(): # class method
#         # print(Employee.emp_count)
#         return (Employee.__emp_count)
#
#     def display_emp_details(self):
#         print("Name : ", self.name, "  Salary : ", self.salary)
#
#
# pk = Employee("pk", 25000)
# # pk.display_count() # improper method
# print(Employee.display_count()) # proper method
# pk.display_emp_details()
# # print(pk.display_count())
# pk1 = Employee("pk1", 55000)
# print(Employee.display_count())
# pk1.display_emp_details()
# pk3 = Employee("pk1", 55000)
# print(Employee.display_count())
# pk.display_count()



# Aggregation

'''
    In O-O approach, it is possible to have relationships between classes.
    When an object of a class becomes the instance variable of another class, 
    the relationship is known as a "has-a" relationship or "AGGREGATION". <>-----
'''

# make a monkey ride a cycle

# class Cycle():
#     def __init__(self, color, brand, cost):
#         self.color = color
#         self.brand = brand
#         self.cost = cost

# class Monkey():
#     def __init__(self, breed, color, cycle):
#         self.breed = breed
#         self.color = color
#         self.cycle = cycle # doodoo.cycle = cycle1

#     def ride_cycle(self):
#         print(self.breed, self.color, self.cycle.brand, self.cycle.color)
#         if (self.breed == "Chimpanzee") & (self.cycle.brand == "BSA") :
#             print("Riding BSA bicycle on a rope")
#         else:
#             print("Ride cycle")

# cycle1 = Cycle("blue", "BSA", 1500)
# cycle2 = Cycle("red", "BSAOO", 2500)
# doodoo = Monkey("Chimpanzee", "brown", cycle1) # monkey has a cycle
# dunston = Monkey("Gorilla" , "black" , cycle2)
# print(doodoo.cycle.brand, doodoo.cycle.cost, doodoo.cycle.color)
# print(dunston.cycle.brand, dunston.cycle.cost, dunston.cycle.color)
# dunston.ride_cycle()
# doodoo.ride_cycle()



# Assosiation
'''
    In O-O approach, when the object of a class is used as a local variable in another class,
    the relationship is known as a 'uses-a' relationship or 'ASSOSIATION'
'''


# class Ring():
#     def __init__(self, diameter):
#         self.diameter = diameter
#
#
# class Lion():
#     def __init__(self, gender):
#         self.gender = gender
#
#     def jump_through_ring(self, ring):
#         if ((self.gender == "Male") & (ring.diameter>=1)):
#             print("woohoo")
#         elif ((self.gender == "Female") & (ring.diameter>=.5)):
#             print("Ok")
#         else:
#             print("Are you dumb, I cannot do that.....!!!!!")
#
#
# ring1 = Ring(1.5)
# ring2 = Ring(0.3)
# simba = Lion("Male")
# nala = Lion("Female")
# simba.jump_through_ring(ring1)
# nala.jump_through_ring(ring2)




# Inheritance

'''
    When a class is itself derived in another class, the relatonship between the parent and the 
    child class is known as "Inheritance" or a "is-a" relationship.
'''

# class CircusAnimal():

#     def wave_after_performance(self):
#         for counter in range(3):
#             print("waving after performance")
#         return "My task is done"

#     def bow_before_performance(self):
#         print("in parent class")
#         print("bowing before performance")

# class Monkey(CircusAnimal):

#     def __init__(self):
#         pass

#     def bow_before_performance(self):
#         print("inside monkey class")
#         print("bowing before performance")
#         return 0

#     def ride_cycle(self):
#         self.bow_before_performance()
#         print("ride cycle")
#         self.wave_after_performance()
        
# class Lion(CircusAnimal):

#     def __init__(self):
#         pass

#     def jump_through_ring (self):
#         self.bow_before_performance()
#         print("jumping thruogh ring")
#         self.wave_after_performance()

# class Elephant(Lion):

#     def __init__(self, *args, **kwargs):
#         pass

#     def dance (self):
#         self.bow_before_performance()
#         print("Dancing")
#         print(self.wave_after_performance())
#         return "Done..."

# dunstom = Monkey()
# simba = Lion()
# hathi = Elephant()
# hathi.dance()
# print(dunstom.bow_before_performance())
# print(dunstom.wave_after_performance())
# simba.jump_through_ring()



# Polymorphism

'''
    Sometimes an object comes in many types or forms. If we have a button, there are many different 
    draw outputs (round button, check button, square button, button with image) but they do share the 
    same logic: onClick().  We access them using the same method . This idea is called Polymorphism.

    Polymorphism is based on the greek words Poly (many) and morphism (forms).  We will create a 
    structure that can take or use many forms of objects.
'''

'''
    Polymorphism with a function:

    We create two classes:  Bear and Dog, both can make a distinct sound.  We then make two instances 
    and call their action using the same method.
'''

# class Bear(object):
#     def sound(self):
#         print ("Groarrr")
 
# class Dog(object):
#     def sound(self):
#         print ("Woof woof!")
 
# def makeSound(animalType):
#     animalType.sound()
 
# bearObj = Bear()
# dogObj = Dog()

# objects = [bearObj, dogObj]
# for i in objects:
#     makeSound(i) #makeSound(bearObj)

# makeSound(bearObj)
# makeSound(dogObj)

'''
Polymorphism with abstract class (most commonly used)

If you create an editor you may not know in advance what type of documents a user 
will open (pdf format or word format?).  
Wouldn’t it be great to access them like this,  instead of having 20 types for every document?

for document in documents:
    print document.name + ': ' + document.show()
'''

# Related Courses:

# Automate the Boring Stuff with Python Programming

'''
Polymorphism with abstract class (most commonly used)
polymorphism example
Polymorphism visual.
Abstract structure is defined in Document class.
If you create an editor you may not know in advance what type of documents a user will open 
(pdf format or word format?).  
Wouldn’t it be great to access them like this,  instead of having 20 types for every document?

for document in documents:
    print document.name + ': ' + document.show()

To do so, we create an abstract class called document. This class does not have any implementation 
but defines the structure (in form of functions) that all forms must have.   
If we define the function show() then both the PdfDocument and WordDocument 
must have the show() function.'''

# class Document:
#     def __init__(self, name):    
#         self.name = name

#     def show(self):     
#         raise NotImplementedError("Subclass must implement abstract method")
 
# class Pdf(Document):
#     def show(self):
#         return 'Show pdf contents!'
 
# class Word(Document):
#     def show(self):
#         return 'Show word contents!'
    
# documents = [Pdf('Document1'),
#              Pdf('Document2'),
#              Word('Document3')]
 
# for document in documents:
#     print (document.name + ': ' + document.show())

# We have an abstract access point (document) to many types of objects (pdf,word) that follow the same structure.

# Polymorphism example
'''
    Another example would be to have an abstract class Car which holds the structure  drive() and stop().  
    We define two objects Sportscar and Truck, both are a form of Car. In pseudo code what we will do is:
'''

'''
    class Car:
        def drive abstract, no implementation.
        def stop abstract, no implementation.
    
    class Sportscar(Car):
        def drive: implementation of sportscar
        def stop: implementation of sportscar
    
    class Truck(Car):
        def drive: implementation of truck
        def stop: implementation of truck
'''

# Then we can access any type of car and call the functionality without taking further into account 
# if the form is Sportscar or Truck.

# class Car:
#     def __init__(self, name):    
#         self.name = name
 
#     def drive(self):             
#         raise NotImplementedError("Subclass must implement abstract method")
 
#     def stop(self):             
#         raise NotImplementedError("Subclass must implement abstract method")
 
# class Sportscar(Car):
#     def drive(self):
#         return 'Sportscar driving!'
 
#     def stop(self):
#         return 'Sportscar braking!'
 
# class Truck(Car):
#     def drive(self):
#         return 'Truck driving slowly because heavily loaded.'
 
#     def stop(self):
#         return 'Truck braking!'
 
 
# cars = [Truck('Bananatruck'),
#         Truck('Orangetruck'),
#         Sportscar('Z3')]
 
# for car in cars:
#     print (car.name + ': ' + car.drive())


'''In Python you can define a method in such a way that there are multiple ways to call it.
Given a single method or function, we can specify the number of parameters ourself.

Depending on the function definition, it can be called with zero, one, two or more parameters.

This is known as method overloading. Not all programming languages support method overloading, 
but Python does.

Method overloading example
We create a class with one method sayHello(). The first parameter of this method is set to 
None, this gives us the option to call it with or without a parameter.

An object is created based on the class, and we call its method using zero and one parameter.
'''
#!/usr/bin/env python3.4
 
# class Human: 
#     def sayHello(self, name=None, age = None):
#         if name is not None:
#             print ('Hello ' + name)
#         else:
#             print ('Hello ')
    
 
# Create instance
# obj = Human()
 
# Call the method
# obj.sayHello()
 
# # Call the method with a parameter
# obj.sayHello(name = 'Guido')

# # # To clarify method overloading, we can now call the method sayHello() in two ways:
# # obj.sayHello()
# obj.sayHello('PRASANT')

"""We created a method that can be called with fewer arguments than it is defined to allow.

We are not limited to two variables, your method could have more variables which are optional."""



# Method Overriding
'''
Method overriding in action 
In Python method overriding occurs simply defining in the child class 
a method with the same name of a method in the parent class. When you define a method 
in the object 
you make this latter able to satisfy that method call, so the implementations of its 
ancestors do not come in play
'''

# class Robot:
#     def action(self):
#         print('Robot action')
    
#     def act(self):
#         print("in act")

# class HelloRobot(Robot):    
#     def action(self, name):
#         print('Hello world ', name)

# r = HelloRobot()
# r.action(123)
# r.act()
# r1 = Robot()
# r1.action()



'''Instance r is created using the class HelloRobot, that inherits from parent class Robot.

The HelloRobot class inherits the method action from its parent class, but its overridden in the class itself.

The method is overwritten. This is only at class level, the parent class remains intact.
If we add another class that inherits, let’s see what happens.'''

# class Robot:
#     def action(self):
#         print('Robot action')
#
# class HelloRobot(Robot):
#     def action(self):
#         print('Hello world')
#
# class DummyRobot(Robot):
#     def start(self):
#         print('Started.')
#
# r = HelloRobot()
# d = DummyRobot()
# r.action()
# d.action()



'''
/Difference between overloading and overriding

Overloading means 2 methods with the SAME Name and different signatures + return types. 
Overriding means 2 methods with the SAME name, wherein the sub method has different functionality.
The main difference between overloading and overriding is that in overloading we can use 
same function name with different parameters for multiple times for different tasks with on a class. 
and overriding means we can use same name function name with same parameters of the base class in the derived class. 
this is also called as re usability of code in the program.
'''

# super keyword

# class Person:

#     def __init__(self, first, last):
#         self.firstname = first
#         self.lastname = last

#     def __str__(self):
#         return self.firstname + " " + self.lastname

# class Employee(Person):

#     def __init__(self, first, last, staffnum, abc):
#         super().__init__(first, last)
#         self.staffnumber = staffnum
#         self.declare_variables(abc)
    
#     def declare_variables(self, abc):
#         self.staffnum = abc
#         self.__abc = None


# x = Person("Prasant", "Mishra")
# y = Employee("Sherlock", "Holmes", "221B")

# print(x)
# print(y)


# class Person:

#     def __init__(self, first, last, age):
#         self.firstname = first
#         self.lastname = last
#         self.age = age

#     def __str__(self):
#         return self.firstname + " " + self.lastname + ", " + str(self.age)

# class Employee(Person):

#     def __init__(self, first, last, age, staffnum):
#         super().__init__(first, last, age)
#         self.staffnumber = staffnum

#     def __str__(self):
#         return super().__str__() + ", " +  self.staffnumber


# x = Person("Prasant", "Mishra", 28)
# y = Employee("Sherlock", "Holmes", 38, "221B")

# print(x)
# print(y)



# Python Operator Overloading
# Python Operator overloading enables us to use mathematical, logical and bitwise operators on python objects 
# just like any primitive data type.

# For example, you can easily add two numbers 3 and 5 with + operator, i.e 3 + 5. And the result is 8.

# But what if you want to add two circles (object of a Circle class) and make a circle having twice the radius? 
# Or what if you want to add two cartesian grid points to yield another point with the same ‘+’ operator? 
# Python operator overloading allows you to perform operations just like those.

# class GridPoint:  #Line: 1, Declaring a class
#     def __init__(self, x, y):  
#         self.x = x  
#         self.y = y  #Line: 4
  
#     def __add__(self, other):  # Equivalent of + operator
#         return GridPoint(self.x + other.x, self.y + other.y)
  
#     def __str__(self):  #Line: 12, returns the attributes when the object is printed
#         string = str(self.x)  
#         string = string + ", " + str(self.y)  
#         return string  #Line: 12
  
# point1 = GridPoint(3, 5)  #Line: 14 Creating a grid point
# point2 = GridPoint(-1, 4)  #Line: 15, Creating another point
# point3 = point1 + point2  #Line: 16, Add two points using __add__() method
# print(point3)  #Line: 17, Print the attributes using __str__() method


# first four lines indicates the declaration of the class GridPoint and definition of constructor method. 
# Let’s have a look at the __add__ function.


#     def __add__(self, other):  # Equivalent of + operator
#         return GridPoint(self.x + other.x, self.y + other.y)
# When we use ‘+’ operator as mathematical addition operation, the __add__() method is implicitly called.

# So, if we are to add two objects of the class GridPoint, we must re-define this method. So, here we need to create another instance of GridPoint class whose value of x is the summation of x in the two GridPoint instances around the ‘+’ operator and value of y is also the summation of y in the two GridPoint instances around the ‘+’ operator.

# Lines 9 to 12 defines the __str__() method which is called when we try to print the object. That’s also a built in method. But we are going to overload the method so that it prints in our specified format.

# Lines 14 and 15, we’ve created two objects of GridPoint, namely point1 and point2. Now, watch Line 16. Two instances of the class GridPoint class are added using ‘+’ operator and assigned as another instance of GridPoint. Python operator overloading helps you do this. So, don’t get surprised when the 17th line shows an output like below image.

# python operator overloading example output

# List of Mathematical Operators
# Here is a list of operators which can be overloaded and used with python operator overloading in a similar way.

# Operator	Description	Method
# +	Addition	__add__(self, other)
# –	Subtraction	__sub__(self, other)
# *	Multiplication	__mul__(self, other)
# /	True Division	__truediv__(self, other)
# //	Floor Division	__floordiv__(self, other)
# %	Remainder	__mod__(self, other)
# **	Power	__pow__(self, other)
# &	Bitwise AND	__and__(self, other)
# |	Bitwise OR	__or__(self, other)
# ^	Bitwise XOR	__xor__(self, other)
# Overloading Relational Operators in Python
# Relational operators are overloaded in a very similar way in python. But the difference is, those operators often return true/false instead of another instance of the object. Let’s work with an example.

        
# class GridPoint:  
#     def __init__(self, x, y):  
#         self.x = x  
#         self.y = y  
  
#     def __gt__(self, other):  # Overloading the greater than operator
#         return self.x > other.x  
# # Returns true if value of x in the left operand is greater than that in the right one. Returns false otherwise
  
#     def __str__(self):  
#         string = str(self.x)  
#         string = string + ", " + str(self.y)  
#         return string  
  
# point1 = GridPoint(3, 5)  
# point2 = GridPoint(-1, 4)  
# if point1 > point2:  # Compares with the overloaded __gt__() method
#     print('point1 is greater than point2')  
# else:  
#     print('point1 is not greater than point2')  
# Look at line 6, where the ‘greater than’ operator has been loaded. The conventional ‘>’ operator returns true if the operand in the left side of it is greater than the right one. We are going to use this property to compare two instances of class GridPoint.

# Then in line 17, we are comparing the objects of the class GridPoint to obtain a boolean type value which will determine whether the first object has the greater value of ‘x’. In this case, the relational operator returns true as 3 is greater than -1. As a result the program prints ‘point1 is greater than point2’.

# python operator overloading relational operator in python.

# More Relational Operators in python
# Here is a list of relational operators that can be overloaded in the same way.

# Operator	Description	Method
# >	Greater than	__gt__(self, other)
# >=	Greater than or equal to	__ge__(self, other)
# <	Less than	__lt__(self, other)
# <=	Less than or equal to	__le__(self, other)
# ==	Equal to	__eq__(self, other)
# !=	Not equal to	__ne__(self, other)
