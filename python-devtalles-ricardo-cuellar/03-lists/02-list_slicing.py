
shopping_cart = ['Coffee', 'Shirts', 'Tennis', 'Socks', 'Pants']

# print(shopping_cart[3]) # Socks

# SLICING CREATES A NEW LIST
new_list = shopping_cart[0:2]

# [Start : end]
# print(new_list) # Coffee, shirts

# [Start : end]
# print(shopping_cart[1:4]) # shirts, tennis, socks

# LIST ARE MUTABLE
new_list[0] = 'Shoes'
new_list[1] = 'Games'
# print(new_list)

# Copy A list 
# (this is a reference to the same list, so modify new_cart is going to modify the shopping_cart list)
new_cart = shopping_cart
print(new_cart) # ['Coffee', 'Shirts', 'Tennis', 'Socks', 'Pants']
print(shopping_cart) # ['Coffee', 'Shirts', 'Tennis', 'Socks', 'Pants']

# new_cart[0] = 'A'
# print(new_cart) # ['A', 'Shirts', 'Tennis', 'Socks', 'Pants']
# print(shopping_cart) # ['A', 'Shirts', 'Tennis', 'Socks', 'Pants']


# Copy a list without reference
# Creating a new list using slicing
# Trick to get rid of the reference
new_cart = shopping_cart[:]
new_cart[1] = 'Food'
print(new_cart) # ['Coffee', 'Shirts', 'Tennis', 'Socks', 'Pants']
print(shopping_cart) # ['Coffee', 'Food', 'Tennis', 'Socks', 'Pants']