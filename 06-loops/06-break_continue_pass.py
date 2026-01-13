

# PASS
# Does nothing just jump to the next line
# a kind of pause
for item in [1, 2, 3, 4, 5]: # 
  pass


# BREAK
# Breaks the loop
for item in [1, 2, 3, 4, 5]: # 1, 2, 3 
  if item == 4:
    break
  print(item)


# CONTINUE
# Ignore a loop fragment
number = 0
while number < len([1, 2, 3, 4, 5]):
  number += 1
  continue # ignores the rest
  print(number)
  
print(number) # 5
