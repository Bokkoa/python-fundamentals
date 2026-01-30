
# Remove methods

number_list = [1, 2, 3, 4, 5]

print(number_list) # 1, 2, 3, 4, 5
# Remove the last element
number_list.pop()
print(number_list)  # 1, 2, 3, 4 

# Delete by index (pop uses -1 by default meaning that is going to delete the last one)
number_list.pop(1)
print(number_list)  # 1, 3, 4 


# Remove()
# Remove is going to delete by value (not index)
# the first coincidence
number_list.remove(4)
print(number_list)  # 1, 3


# Clear
# Delete all list values
number_list.clear()
print(number_list) # []