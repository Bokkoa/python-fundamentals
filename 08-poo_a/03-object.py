
class Person:
  def __init__(self, name, age):
    if(age > 18):
      self.name = name
      self.age = age

# Instantiating
person1 = Person("Kone", 29)
print(person1)
print(person1.name)

# Instantiating
person2 = Person("Vianey", 24)
print(person2)
print(person2.name)
