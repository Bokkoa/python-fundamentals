
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)


# Unpacking
# "unpack" a list or destructure it in multiple vars
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)


# unpacking the rest
# If we don't assing the rest we gonna have an error
# the unpack variable should match with the quantity of our list

# If we assign a variable after the asterisk rest,
# this variable is going to assign the last item
a, b, c, *others, d = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(c)
print(others)
print(d) # 9
