1)class:
A blueprint for creating objects.
Defines attributes (data) and methods (functions) that the object can use.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")


2)object:
an inheritance of class

my_dog = Dog("Buddy", "Labrador")
my_dog.bark()  # Output: Buddy says woof!

3)Encapsulation:
Hiding internal state and requiring all interaction to be performed through methods.
Achieved using private/protected variables (_var, __var).

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

4)Inheritance:
One class can inherit from another to reuse code.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

5)Polymorphism:
Different classes can define methods with the same name, and the correct one is used depending on the object.

def make_animal_speak(animal):
    animal.speak()

make_animal_speak(Dog())     # Dog barks
make_animal_speak(Animal())  # Animal speaks

6)Abstraction:
Hiding complex implementation details and showing only the necessary features.
Can be implemented using abstract base classes (abc module).

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2









