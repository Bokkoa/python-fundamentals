
# == equal or equivalent

print(5 == 5) # True
print(True == 1) # True

print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True

new_list = []
other_list = []

# == is for value comparison
print(new_list == other_list) # True

# is is for memory comparison
print(new_list is other_list) # False