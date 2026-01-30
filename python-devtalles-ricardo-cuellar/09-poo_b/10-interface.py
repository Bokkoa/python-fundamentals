# Interface:
# is a contract that defines methods but without 
# declare how implement them

# IN THIS LESSON ABSTRACT CLASSES WERE CONSIDER AS INTERFACES
# Are not necessary in python 
"""
his is because Python has proper multiple inheritance, 
and also ducktyping, 
which means that the places where you must have interfaces in Java, 
you don't have to have them in Python.
"""

# module for abstract classes 
from abc import ABC, abstractmethod

# abstract class (inherit from ABC)
class Animal(ABC):
  
  # this should be implemented by class that inherits
  # the abstract class
  @abstractmethod
  def sound(self):
    pass
  
  @abstractmethod
  def sleep(self):
    pass


class Dog(Animal):
  def sound(self):
    return "Woof woof"
  
  def sleep(self):
    return "ZZZZ"

class Cat(Animal):
  def sound(self):
    return "Meow meow"

  def sleep(self):
    return "ZZZZ"

ginger = Dog()
fresito = Cat()
  
print(ginger.sound())
print(ginger.sleep())
print(fresito.sound())
print(fresito.sleep())