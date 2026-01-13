# This structure is...
# SORTED
# INMUTABLE
# ALLOW DUPED ROWS
# INDEXED

a_tuple = (1, 2, 3, 4, 1, "Hello", 1, True, "asdfasd", 45)
print(a_tuple)


# Methods


# count()
# get number of coincidences
print(a_tuple.count(1)) # 3

# index()
# get index by value
print(a_tuple.index("Hello")) # 5

# every time index is going to match with the first coincidence
print(a_tuple.index(1)) # 0


# this is going to throw error since this structure is inmutable
# a_tuple[4] = "World" # this cannot be done

new_tuple = a_tuple[5]
print(new_tuple)

# Inmutable and faster than lists
week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)