# ALL the __ attribtues and methods are considered as private

class Person:
  def __init__(self, name, age):
    self.name = name # instance attributes
    
    # NAME MANGLING is going to rename as _CLASSNAME__password
    self.__password = "1234" # private convention 
    
  def __generate_password(self):
    return f"$${self.name}{self.age}"


person1 = Person("Kone", 29)

print(person1.name) # Kone
# print(person1.__generate_password())
# print(person1.__password) # this throws error

# NAME MANGLING REAL PROPERTY
# BUT IT SHOULD BE PRIVATE 
# THIS IS NOT RECOMMENDED TO DO
# print(person1._Person__password)
