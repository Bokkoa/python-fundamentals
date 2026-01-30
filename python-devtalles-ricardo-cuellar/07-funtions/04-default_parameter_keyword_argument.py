# Default parameter
# Are parameters with a value in case that
# function didn't get some args
def hello(greet = "Hello", name = "Guest"):
  print(f"{greet}, {name}")

hello("Hola") # Hola, Guest
hello() # Hello, Guest

# Keyword Arguments

# this is a different order, could be not semantically correct
hello("Felipe", "Hola") # Felipe, Hola 

# this worked as keyword args, that respect the argument order
hello(name="Kone", greet="Hello") # Hello, Kone