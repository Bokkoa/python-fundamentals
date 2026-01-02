# Sort methods
letters = ['a', 'f', 'b', 'c', 'z', 'h', 'o', 'd', 'e']
original_letters = letters[:]
print(letters) # ['a', 'f', 'b', 'c', 'z', 'h', 'o', 'd', 'e']

# sort()
# sort ALTERS the original variable
letters.sort()
print(letters) # ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'o', 'z']
print(original_letters) 


# sorted()
# sorted doesn't alter the original list
new_list = sorted(original_letters)
print(new_list)


# copy()
# Create new letter instances without alter the original
# and without use sorted()

new_letters = original_letters.copy()



# Reverse
# Is going to sort in reverse order the original list
original_letters.reverse()
print(original_letters)