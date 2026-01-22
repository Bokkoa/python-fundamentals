
x = [1, 2, 3]

# retrieve the object type
print(type(x))

# retrieves attributes and methods from the class
print(dir(x))

# boolean function to check if it contains some method or attribute
print(hasattr(x, '__len__'))

# get the method reference including memory address
print(getattr(x, 'append'))

# to check if method is callable
print(callable(x.append))

# get memory address
print(id(x))