1. Create a class with attributes and access those attributes with objects and class.

python

class MyClass:
    class_attr = "This is a class attribute"

    def __init__(self, value):
        self.instance_attr = value

# Accessing attributes with objects
obj = MyClass("This is an instance attribute")
print(obj.instance_attr)

# Accessing attributes with class
print(MyClass.class_attr)

2. Create a class with attributes and access those attributes with user-defined function.

python

class MyClass:
    def __init__(self, value):
        self.instance_attr = value

    def get_attr(self):
        return self.instance_attr

obj = MyClass("This is an instance attribute")
print(obj.get_attr())

3. OOP program to find Area of circle by using CLASS and OBJECTS.

python

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
print(f"Area of circle: {circle.area()}")

4. OOP program to find the Area of Triangle by using CLASS and OBJECTS.

python

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

triangle = Triangle(5, 10)
print(f"Area of triangle: {triangle.area()}")

5. OOP program to find Area of a room by using CLASS and OBJECTS.

python

class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

room = Room(20, 15)
print(f"Area of room: {room.area()}")

6. OOP program to print Employee details by using user-defined function.

python

class Employee:
    def __init__(self, emp_id, emp_name, emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Age: {self.emp_age}")

employee = Employee(1, "John Doe", 30)
employee.display()

7. Definitions

    Objects: Instances of a class that hold data and behavior defined by the class.
    Class: A blueprint for creating objects, defining attributes and methods.
    Methods: Functions defined within a class that operate on its instances.
    Attributes: Variables that hold data specific to a class and its objects.
    Inheritance: A mechanism where one class inherits attributes and methods from another class.
    Polymorphism: The ability of different objects to respond, each in its own way, to identical messages.
    Abstraction: Hiding complex implementation details and showing only the necessary features.
    Encapsulation: Restricting access to certain components of an object and preventing outside interference.
    Programming paradigms: Different styles of programming (e.g., procedural, object-oriented, functional).

8. OOP program to find Average of 3 numbers by using CLASS and OBJECTS.

python

class Average:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_average(self):
        return (self.a + self.b + self.c) / 3

numbers = Average(10, 20, 30)
print(f"Average: {numbers.calculate_average()}")

9. OOP program to find simple interest by using CLASS and OBJECTS.

python

class SimpleInterest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate(self):
        return (self.principal * self.rate * self.time) / 100

si = SimpleInterest(1000, 5, 2)
print(f"Simple Interest: {si.calculate()}")

10. OOP program to print employee details using __init__ method.

python

class Employee:
    def __init__(self, emp_id, emp_name, emp_age):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Age: {self.emp_age}")

employee = Employee(1, "John Doe", 30)
employee.display()

11. OOP program for default constructor to increment and decrement a variable.

python

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count

counter = Counter()
print(f"Increment: {counter.increment()}")
print(f"Decrement: {counter.decrement()}")

12. Class Dog with attributes breed, age, colour for parameterized constructor.

python

class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

dog = Dog("Labrador", 5, "Yellow")
print(f"Breed: {dog.breed}, Age: {dog.age}, Color: {dog.color}")

13. Class Movie with attributes area, movie name, ticket price for parameterized constructor with use of temporary variables.

python

class Movie:
    def __init__(self, area, name, price):
        self.area = area
        self.name = name
        self.price = price

movie = Movie("Downtown", "Inception", 15)
print(f"Area: {movie.area}, Movie Name: {movie.name}, Ticket Price: {movie.price}")

14. OOP program using “myparameter” as “self “parameter.

python

class MyClass:
    def __init__(myparameter, value):
        myparameter.value = value

    def display(myparameter):
        print(myparameter.value)

obj = MyClass("Hello World")
obj.display()

15. Class Pens with attributes colour, brand and user destructor to delete objects.

python

class Pens:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def __del__(self):
        print(f"Deleted {self.color} pen of {self.brand} brand")

pen = Pens("Blue", "Parker")
print(f"Color: {pen.color}, Brand: {pen.brand}")
del pen

16. Class with user-defined functions and access the user-defined function through class.

python

class Greeting:
    def say_hello(self):
        print("Hello, World!")

greet = Greeting()
greet.say_hello()

17. OOP program to find factorial of a number through OOP.

python

class Factorial:
    def __init__(self, num):
        self.num = num

    def calculate(self):
        if self.num == 0:
            return 1
        else:
            return self.num * self.calculate(self.num - 1)

fact = Factorial(5)
print(f"Factorial: {fact.calculate()}")

18. OOP program to find Fibonacci series through OOP.

python

class Fibonacci:
    def __init__(self, n):
        self.n = n

    def series(self):
        a, b = 0, 1
        result = []
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        return result

fib = Fibonacci(10)
print(f"Fibonacci series: {fib.series()}")

19. OOP program to find whether a number is even or odd.

python

class Number:
    def __init__(self, num):
        self.num = num

    def is_even(self):
        return self.num % 2 == 0

number = Number(5)
print(f"Is number even? {number.is_even()}")

20. OOP program to check whether a number is palindrome or not.

python

class Palindrome:
    def __init__(self, num):
        self.num = num

    def is_palindrome(self):
        return str(self.num) == str(self.num)[::-1]

number = Palindrome(121)
print(f"Is number palindrome? {number.is_palindrome()}")

21. OOP program to check whether a number is perfect or not.

python

class PerfectNumber:
    def __init__(self, num):
        self.num = num

    def is_perfect(self):
        return self.num == sum(i for i in range(1, self.num) if self.num % i == 0)

number = PerfectNumber(28)
print(f"Is number perfect? {number.is_perfect()}")

22. OOP program to check whether a number is Armstrong or not.

python

class Armstrong:
    def __init__(self, num):
        self.num = num

    def is_armstrong(self):
        order = len(str(self.num))
        return self.num == sum(int(digit) ** order for digit in str(self.num))

number = Armstrong(153)
print(f"Is number Armstrong? {number.is_armstrong()}")

23. OOP program to call one method from another method by OOP.

python

class Example:
    def method1(self):
        print("Method 1")

    def method2(self):
        self.method1()
        print("Method 2")

example = Example()
example.method2()

24. OOP program to implement decorator class method.

python

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before function call")
        self.func()
        print("After function call")

@MyDecorator
def my_function():
    print("Inside function")

my_function()

25. OOP program to implement decorator static method (both ways).

python

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before function call")
        self.func()
        print("After function call")

class MyClass:
    @staticmethod
    @MyDecorator
    def my_static_method():
        print("Inside static method")

MyClass.my_static_method()

26. OOP program to implement prototyping.

python

import copy

class Prototype:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return copy.deepcopy(self)

original = Prototype("Original")
clone = original.clone()
print(f"Original: {original.name}, Clone: {clone.name}")

27. OOP program to implement Access modifiers for both variables and methods.

python

class MyClass:
    def __init__(self):
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"

    def public_method(self):
        return "Public method"

    def _protected_method(self):
        return "Protected method"

    def __private_method(self):
        return "Private method"

obj = MyClass()
print(obj.public_var)
print(obj._protected_var)
# print(obj.__private_var)  # This will raise an AttributeError
print(obj.public_method())
print(obj._protected_method())
# print(obj.__private_method())  # This will raise an AttributeError

28. OOP program to implement Built-in Attribute methods (getattr, hasattr, setattr, delattr).

python

class MyClass:
    def __init__(self):
        self.attribute = "Initial value"

obj = MyClass()

# getattr
print(getattr(obj, 'attribute'))

# hasattr
print(hasattr(obj, 'attribute'))

# setattr
setattr(obj, 'attribute', 'New value')
print(obj.attribute)

# delattr
delattr(obj, 'attribute')
print(hasattr(obj, 'attribute'))

29. OOP program to implement Built-in class methods (repr, len, cmp, dict, doc, bases, module, name).

python

class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyClass({self.value})"

    def __len__(self):
        return len(self.value)

obj = MyClass("Hello")
print(repr(obj))
print(len(obj))
print(obj.__dict__)
print(obj.__doc__)
print(MyClass.__bases__)
print(MyClass.__module__)
print(MyClass.__name__)

30. OOP program to implement Arrays of objects.

python

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("John", 20),
    Student("Jane", 22),
    Student("Doe", 21)
]

for student in students:
    print(f"Name: {student.name}, Age: {student.age}")

31. Memory management in Python.

Python manages memory using private heaps, and memory allocation and deallocation is handled by the Python memory manager. Python uses reference counting and garbage collection to reclaim memory from objects that are no longer in use.
32. Differences of OOP & POP.

    OOP (Object-Oriented Programming): Uses objects and classes, encapsulation, inheritance, and polymorphism.
    POP (Procedural-Oriented Programming): Based on functions or procedures, uses a top-down approach, focuses on procedures rather than data.

33. Create a class and implement all methods (public, private, protected, class, static) and also call one method from another method.

python

class MyClass:
    def __init__(self, value):
        self.value = value

    def public_method(self):
        print("Public method")
        self.__private_method()

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

    @classmethod
    def class_method(cls):
        print("Class method")

    @staticmethod
    def static_method():
        print("Static method")

obj = MyClass(10)
obj.public_method()
obj._protected_method()
# obj.__private_method()  # This will raise an AttributeError
MyClass.class_method()
MyClass.static_method()
