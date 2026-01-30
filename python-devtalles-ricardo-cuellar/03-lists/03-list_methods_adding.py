
# Add methods

number_list = [1, 2, 3, 4, 5]

# append
# Adding a new node at the end of the list
print(number_list) # [1, 2, 3, 4, 5]
number_list.append(100)
print(number_list) # [1, 2, 3, 4, 5, 100]
number_list.append(200)
print(number_list) # [1, 2, 3, 4, 5, 100, 200]

# Insert
# Insert a new node in an specific index
number_list.insert(1, 200)
number_list.insert(3, 300)
print(number_list) # [1, 200, 2, 300, 3, 4, 5, 100, 200]


# Extends
# adding or append a new list
number_list.extend([11, 22, 33])
print(number_list) # [1, 200, 2, 300, 3, 4, 5, 100, 200, 11, 22, 33]