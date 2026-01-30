
class Person:
  
  specie = "Human" # class attribute
  
  def __init__(self, name, age):
    self.name = name # instance attributes
    self.age = age
  
  def work(self):
    return f"{self.name} is working very hard"

  def eat(self, food):
    if food.lower() == 'tacos':
      return "YEAH"
    else:
      return "+Energy"

person1 = Person("Kone", 29)

# Public attributes
print(person1.name) # Kone
print(person1.specie) # Human
print(person1.age) # 29
print(person1.work()) # Kone is working very hard
print(person1.eat("Hot Dog")) # +Energy
print(person1.eat("Tacos")) # YEAH