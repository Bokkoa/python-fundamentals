# VENN DIAGRAMS

# union
# set1.union(set2)
# adding everything from A and B
set1 = {1, 2, 3}
set2 = {4, 5, 6}

union_set = set1.union(set2)

print(union_set) # 1, 2, 3, 4, 5, 6


# intersection
# set1.intersection(set2)
# adding coincidences between A and B
set1 = { 1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print(intersection) # 3, 4


# Difference
# set1.difference(set2)
# Getting the elements that are in set1 but not in set2
set1 = { 1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = set1.difference(set2)
difference_from_set2 = set2.difference(set1)
print(difference) # {1, 2}
print(difference_from_set2) # {5, 6}
