
# For: for iterables, when we know when it finishes

# While: When we don't know when is going to finish and we might need a condition


# While need more specific instructions than for, is kind more manual

my_list = [1, 2, 3, 4, 5]

for item in my_list:
  print(item)
  
  
item = 0
while item < len(my_list):  # 0, 1, 2, 3, 4
  print(item)
  item += 1