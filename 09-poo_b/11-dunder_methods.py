# Dunder methods
# double underscore methods


class Person:
  def __init__(self, name):
    self.name = name
  
  # This is going to be printed when we call 
  # print for this class instances
  def __str__(self):
    return f"Hello I'm {self.name}"
  
  def __len__(self):
    return 184
    
person = Person("Felipe")
print(person)
print(len(person))