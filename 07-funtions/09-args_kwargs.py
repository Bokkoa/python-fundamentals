
# this *args means N arguments
# everything pass in args is converted as tuple
def big_function(*args):
  print(args)
  return sum(args)  # summing all the arguments
  
print(big_function(1, 2, 3, 4, 5, 6, 7)) # 28




# this **kwargs get all the information in a dictionary way
def big_function(*args, **kwargs):
  print(args)
  print(kwargs)
  
  total = 0
  for item in kwargs.values():
    total += item
  print(total)
  return sum(args) + total # summing all the arguments + kwargs sum
  
print(big_function(1, 2, 3, 4, 5, 6, 7, num = 77, num2 = 120)) # 28