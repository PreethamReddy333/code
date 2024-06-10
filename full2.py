2. Create multiple classes with constructor and user-defined methods

python

class ClassA:
    def __init__(self, a):
        self.a = a

    def display_a(self):
        print(f"ClassA: {self.a}")

class ClassB:
    def __init__(self, b):
        self.b = b

    def display_b(self):
        print(f"ClassB: {self.b}")

obj_a = ClassA(10)
obj_b = ClassB(20)

obj_a.display_a()
obj_b.display_b()

3. Create a parent class and child class, inherit properties and attributes of parent class to child class

python

class Parent:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr

    def parent_method(self):
        print(f"Parent method: {self.parent_attr}")

class Child(Parent):
    def __init__(self, parent_attr, child_attr):
        super().__init__(parent_attr)
        self.child_attr = child_attr

    def child_method(self):
        print(f"Child method: {self.child_attr}")

child = Child("Parent Attribute", "Child Attribute")
child.parent_method()
child.child_method()

4. Create Multiple Parent classes and one child class, inherit properties and attributes of multiple parent class to child classes

python

class Parent1:
    def __init__(self, parent1_attr):
        self.parent1_attr = parent1_attr

    def parent1_method(self):
        print(f"Parent1 method: {self.parent1_attr}")

class Parent2:
    def __init__(self, parent2_attr):
        self.parent2_attr = parent2_attr

    def parent2_method(self):
        print(f"Parent2 method: {self.parent2_attr}")

class Child(Parent1, Parent2):
    def __init__(self, parent1_attr, parent2_attr, child_attr):
        Parent1.__init__(self, parent1_attr)
        Parent2.__init__(self, parent2_attr)
        self.child_attr = child_attr

    def child_method(self):
        print(f"Child method: {self.child_attr}")

child = Child("Parent1 Attribute", "Parent2 Attribute", "Child Attribute")
child.parent1_method()
child.parent2_method()
child.child_method()

5. Write a python program to implement Multilevel inheritance through Object oriented programming

python

class Grandparent:
    def __init__(self, grandparent_attr):
        self.grandparent_attr = grandparent_attr

    def grandparent_method(self):
        print(f"Grandparent method: {self.grandparent_attr}")

class Parent(Grandparent):
    def __init__(self, grandparent_attr, parent_attr):
        super().__init__(grandparent_attr)
        self.parent_attr = parent_attr

    def parent_method(self):
        print(f"Parent method: {self.parent_attr}")

class Child(Parent):
    def __init__(self, grandparent_attr, parent_attr, child_attr):
        super().__init__(grandparent_attr, parent_attr)
        self.child_attr = child_attr

    def child_method(self):
        print(f"Child method: {self.child_attr}")

child = Child("Grandparent Attribute", "Parent Attribute", "Child Attribute")
child.grandparent_method()
child.parent_method()
child.child_method()

6. Write a python program to implement Hierarchical inheritance through Object oriented programming

python

class Parent:
    def __init__(self, parent_attr):
        self.parent_attr = parent_attr

    def parent_method(self):
        print(f"Parent method: {self.parent_attr}")

class Child1(Parent):
    def __init__(self, parent_attr, child1_attr):
        super().__init__(parent_attr)
        self.child1_attr = child1_attr

    def child1_method(self):
        print(f"Child1 method: {self.child1_attr}")

class Child2(Parent):
    def __init__(self, parent_attr, child2_attr):
        super().__init__(parent_attr)
        self.child2_attr = child2_attr

    def child2_method(self):
        print(f"Child2 method: {self.child2_attr}")

child1 = Child1("Parent Attribute", "Child1 Attribute")
child2 = Child2("Parent Attribute", "Child2 Attribute")

child1.parent_method()
child1.child1_method()

child2.parent_method()
child2.child2_method()

7. Write a python program to implement Hybrid inheritance through Object oriented programming

python

class Parent1:
    def __init__(self, parent1_attr):
        self.parent1_attr = parent1_attr

    def parent1_method(self):
        print(f"Parent1 method: {self.parent1_attr}")

class Parent2:
    def __init__(self, parent2_attr):
        self.parent2_attr = parent2_attr

    def parent2_method(self):
        print(f"Parent2 method: {self.parent2_attr}")

class Child1(Parent1, Parent2):
    def __init__(self, parent1_attr, parent2_attr, child1_attr):
        Parent1.__init__(self, parent1_attr)
        Parent2.__init__(self, parent2_attr)
        self.child1_attr = child1_attr

    def child1_method(self):
        print(f"Child1 method: {self.child1_attr}")

class Child2(Parent1):
    def __init__(self, parent1_attr, child2_attr):
        super().__init__(parent1_attr)
        self.child2_attr = child2_attr

    def child2_method(self):
        print(f"Child2 method: {self.child2_attr}")

child1 = Child1("Parent1 Attribute", "Parent2 Attribute", "Child1 Attribute")
child2 = Child2("Parent1 Attribute", "Child2 Attribute")

child1.parent1_method()
child1.parent2_method()
child1.child1_method()

child2.parent1_method()
child2.child2_method()

8. Write a python program to implement Method overloading through Object oriented programming

Python does not support method overloading by default. We can achieve similar functionality by using default arguments or variable-length arguments.

python

class Overload:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Two arguments: {a}, {b}")
        elif a is not None:
            print(f"One argument: {a}")
        else:
            print("No arguments")

obj = Overload()
obj.display()
obj.display(10)
obj.display(10, 20)

9. Write a python program to implement Method overriding through Object oriented programming

python

class Parent:
    def display(self):
        print("Parent method")

class Child(Parent):
    def display(self):
        print("Child method")

child = Child()
child.display()

10. Write a python program to demonstrate __str__ function through Object oriented programming

python

class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value {self.value}"

obj = MyClass(10)
print(obj)

11. Write a python program to implement abstract class through Object oriented programming

python

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implemented abstract method")

obj = ConcreteClass()
obj.abstract_method()

12. Write a python program to implement singleton class through Object oriented programming

python

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True

13. Write a python program to implement Inner class through Object oriented programming

python

class OuterClass:
    def __init__(self, outer_value):
        self.outer_value = outer_value

    class InnerClass:
        def __init__(self, inner_value):
            self.inner_value = inner_value

        def display(self):
            print(f"Inner value: {self.inner_value}")

outer = OuterClass("Outer")
inner = outer.InnerClass("Inner")
inner.display()

14. Write a python program to implement Meta class through Object oriented programming

python

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super(Meta, cls).__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

obj = MyClass(10)
obj.display()

15. Write a python program to implement Regular class through Object oriented programming

python

class RegularClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

obj = RegularClass(10)
obj.display()

16. Learn about different types of classes

Different types of classes include:

    Regular Class: Basic user-defined class.
    Abstract Class: A class that contains one or more abstract methods.
    Singleton Class: A class that allows only one instance to be created.
    Inner Class: A class defined within another class.
    Meta Class: A class that defines the behavior of other classes (classes of classes).

17. Learn about polymorphism and its types

Polymorphism is the ability of different objects to respond to the same method in different ways. It can be achieved through:

    Method Overriding: When a subclass provides a specific implementation of a method already defined in its superclass.
    Method Overloading: When multiple methods with the same name but different parameters exist in the same class.

18. Learn about inheritance and its types

Inheritance is a mechanism where a new class inherits attributes and methods from an existing class. Types include:

    Single Inheritance: One child class inherits from one parent class.
    Multiple Inheritance: One child class inherits from multiple parent classes.
    Multilevel Inheritance: A class inherits from another class, which in turn inherits from another class.
    Hierarchical Inheritance: Multiple classes inherit from a single parent class.
    Hybrid Inheritance: A combination of two or more types of inheritance.

19. Learn about inbuilt methods, functions and basic operations of different data types
List

    Methods: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy()
    Operations: Concatenation (+), Repetition (*), Membership (in)

String

    Methods: upper(), lower(), capitalize(), title(), strip(), split(), join(), replace(), find(), count(), format()
    Operations: Concatenation (+), Repetition (*), Slicing ([:]), Membership (in)

Tuple

    Methods: count(), index()
    Operations: Concatenation (+), Repetition (*), Slicing ([:]), Membership (in)

Dictionary

    Methods: keys(), values(), items(), get(), pop(), update(), clear(), copy()
    Operations: Membership (in), Iteration (for)

Set

    Methods: add(), update(), remove(), discard(), pop(), clear(), union(), intersection(), difference(), symmetric_difference()
    Operations: Membership (in), Iteration (for)

Number

    Operations: Addition (+), Subtraction (-), Multiplication (*), Division (/), Floor Division (//), Modulus (%), Exponentiation (**)

20. Write a python program to implement implicit type conversion through Object oriented programming

python

class ImplicitConversion:
    def __init__(self, integer, floating):
        self.integer = integer
        self.floating = floating

    def add(self):
        return self.integer + self.floating

obj = ImplicitConversion(5, 2.5)
print(obj.add())

21. Write a python program to implement Explicit type conversion through Object oriented programming

python

class ExplicitConversion:
    def __init__(self, value):
        self.value = value

    def convert_to_int(self):
        return int(self.value)

obj = ExplicitConversion("123")
print(obj.convert_to_int())

22. What is type conversion and explain its types

Type Conversion is the process of converting one data type to another. It can be done in two ways:

    Implicit Type Conversion: Automatically done by the Python interpreter (e.g., converting an integer to a float during division).
    Explicit Type Conversion: Done manually by the programmer using functions like int(), float(), str(), etc.

23. Write a python program to implement Unit Testing

python

import unittest

class MyTestClass:
    def add(self, a, b):
        return a + b

class TestMyTestClass(unittest.TestCase):
    def test_add(self):
        obj = MyTestClass()
        self.assertEqual(obj.add(2, 3), 5)
        self.assertEqual(obj.add(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()

24. Write a python program to implement Classification Hierarchies

python

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

class Motorcycle(Vehicle):
    def __init__(self, make, model, engine_capacity):
        super().__init__(make, model)
        self.engine_capacity = engine_capacity

car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Honda", "CBR", 1000)

print(f"Car: {car.make} {car.model}, Doors: {car.doors}")
print(f"Motorcycle: {motorcycle.make} {motorcycle.model}, Engine Capacity: {motorcycle.engine_capacity}")

25. Write a python program to implement Aggregation

python

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

engine = Engine(150)
car = Car("Toyota", "Corolla", engine)

print(f"Car: {car.make} {car.model}, Engine Horsepower: {car.engine.horsepower}")

26. Write a python program to implement Composition

python

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)

car = Car("Toyota", "Corolla", 150)

print(f"Car: {car.make} {car.model}, Engine Horsepower: {car.engine.horsepower}")

27. Write a python program to implement Exception Handling

python

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Execution completed.")

28. Write a python program to implement the super() keyword in various types

python

class Parent:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Parent value: {self.value}")

class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)
        self.extra = extra

    def display(self):
        super().display()
        print(f"Child extra: {self.extra}")

child = Child(10, 20)
child.display()

29. Write a python program to implement isInstance() and isSubClass()

python

class Parent:
    pass

class Child(Parent):
    pass

obj = Child()

print(isinstance(obj, Child))   # True
print(isinstance(obj, Parent))  # True
print(issubclass(Child, Parent)) # True
print(issubclass(Parent, Child)) # False
