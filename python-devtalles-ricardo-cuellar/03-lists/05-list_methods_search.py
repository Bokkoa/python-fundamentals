# Search methods

number_list = [1, 2, 3, 4, 5, 2, 2, 2]


# Index

# Is going to search the first value coincidence 
# and return the index
print(number_list.index(2)) # 1


# Is going to search the first value coincidence
# starting from 0 position until the 4th one
# is desired value, start, end
# and then return the index
print(number_list.index(3, 0, 4)) # 2
print(number_list.index(3, 0, 2)) # Error, 3 is in the last limit (not took in account)



# IN
print( 2 in number_list) # True
print( 12 in number_list) # False


# Count

# Looking for the count of times that 2 value appear in the list
print( number_list.count(2)) # 3