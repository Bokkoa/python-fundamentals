
# Are values that can be true or false

# Truthy (True values)
print(bool(True)) # True
print(bool(1)) # True
print(bool(3.12)) # True
print(bool(1j)) # True
print(bool(-1)) # True
print(bool("Hello!"))
print(bool([1, 2, 3, 4])) # True list
print(bool((1, 2, 3, 4))) # True set
print(bool({1, 2, 3, 4})) # True dict

# Falsey (False values)
print(bool(False)) # Flase
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(0j)) # False
print(bool("")) # False
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False
print(bool(None)) # False
