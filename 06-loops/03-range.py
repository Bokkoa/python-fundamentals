print(range(0, 10)) # range (0, 10)

print(iter(range)) # range iterator

# print(iter(10)) # throws error

# with range you can generate the numbers without use a data structure as list
# start, stop, step
# start = 0 (from)
# stop = 100 (to)
# step = 2 (2, 4, 6, 8...)
for number in range(0, 100, 2):
  print(number)
