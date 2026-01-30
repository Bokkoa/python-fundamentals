
# module for abstract classes 
from abc import ABC, abstractmethod

# abstract class (inherit from ABC)
class Animal(ABC):
  
  # this should be implemented by class that inherits
  # the abstract class
  @abstractmethod
  def sound(self):
    pass
  
  # not necessarily an abstract class might have 
  # abstract methods only 
  # but it cannot be instantiated directly
  def sleep(self):
    print("zzzz...")
    