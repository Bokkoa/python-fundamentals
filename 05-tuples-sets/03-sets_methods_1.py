
# comparison of sets
# Venn Diagrams


# .add()
# add a new element

new_set = {1, 2, 3}
new_set.add(5)
new_set.add(3) # ignored
new_set.add(3) # ignored
print(new_set)


# .remove()
# remove an element
new_set.remove(2) # success
new_set.remove(3) # success
# new_set.remove(7) # throws error because 7 doesn't exists in the current set


# .discard()
# remove value if exist (whereas remove throw error if doesn't exist)
new_set.discard(5) # success
new_set.discard(7) # ignored
new_set.discard(10) # ignored


# .pop()
# removes a random element and returns it
print(new_set.pop())
print(new_set)