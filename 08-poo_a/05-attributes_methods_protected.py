
class Person:
  
  def __init__(self, name):
    self.name = name # instance attributes
    self._energy = 100
  
  def _waste_energy(self, quantity):
    self._energy -= quantity

person1 = Person("Kone")

# Public attributes
print(person1.name) # Kone
print(person1._energy)
print(person1._waste_energy(20))
print(person1._energy)
