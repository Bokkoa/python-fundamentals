# Symmetric difference
# it retrieves everything that ISN'T present in both sets
# set1.symmetric_difference(set2)
set1 = { 1, 2, 3, 4 }
set2 = {3, 4, 5, 6}

print(set1.symmetric_difference(set2)) # {1, 2, 5, 6}


# is subset
# if a set is a subset from other
# set1.issubset(set2)
set1 = {2, 3}
set2 = { 1, 2, 3, 4, 5}
set3 = { 9, 10 }
print(set1.issubset(set2)) # True
print(set3.issubset(set2)) # False


# is super set
# if one set has all the elements of other set
# set1.issuperset(set2)

set1 = { 1, 2, 3, 4}
set2 = { 1, 2, }
set3 = { 1, 2, 3, 4}
set4 = { 4, 5 }

print(set1.issuperset(set2)) # True
print(set1.issuperset(set3)) # True
print(set1.issuperset(set4)) # False