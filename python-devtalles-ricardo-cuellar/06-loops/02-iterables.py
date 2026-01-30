# iterable
# is an object that can be iterated (lists, dicts, sets, tuples or custom objects)

# iterator: object that remember their position (more manual than iterable)
numbers = [1, 2, 3, 4, 5]

# ITERABLE
for number in numbers:
  print(number)
  

# ITERATOR
iterator = iter(numbers)
print(iterator)
print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5
# print(next(iterator)) # throws error


user = {
  'name': 'Kone',
  'age': 29,
  'can_swim': False
}

# item is keys
for item in user:
  print(item)
  
# we use values in order to get the val instead default key behavior
for item in user.values():
  print(item)
  
# items iterates over the value key in our object returning a tuple
# we could use 
# for key, value in user.items():
# to simplify it
for item in user.items():
  key, value = item
  print(item)
  print(key, value)
  
