
class Person:
  
  species = "Human"
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # Class method allows us to create a method usable regardless the instance.
  # this means that all instances might share the same method and state in case of 
  # exist
  @classmethod
  def change_species(cls, new_specie):
    cls.species = new_specie
    
  # Method that doesn't depends on class or isntance attributes or state
  @staticmethod
  def is_older(age):
    return age >= 18
    
person1 = Person("Felipe", 29)
print(person1.species)

# we should call the class methods by class name instead instance name
Person.change_species("Cyborg")
print(person1.species)


person2 = Person("FeliVianeype", 24)
print(person2.species)



# static method could be used with or without the class
print(Person.is_older(19)) # True
person2.is_older(person2.age)





# Notice the difference in the call signatures of foo, class_foo and static_foo:

class A(object):
    def foo(self, x):
        print(f"executing foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"executing class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"executing static_foo({x})")

a = A()
# Below is the usual way an object instance calls a method. 
# The object instance, a, is implicitly passed as the first argument.

a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>, 1)



# With classmethods, 
# the class of the object instance is implicitly passed as the first argument instead of self.

a.class_foo(1)
# executing class_foo(<class '__main__.A'>, 1)


# You can also call class_foo using the class. 
# In fact, if you define something to be a classmethod, 
# it is probably because you intend to call it from the class rather than from a class instance. 
# A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:

A.class_foo(1)
# executing class_foo(<class '__main__.A'>, 1)