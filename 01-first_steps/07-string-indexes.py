name = "Felipe" # 5 indexes
print(name) # Felipe

print(name[0]) # F
print(name[1]) # e


# How to get last letter dynamically
print(name[-1]) 


# [start:stop]
# the last index is not taking in count (in this case 3 is I in Felipe, so is going to be Fel)
# Felipe - Fel
print(name[0:3]) # Fel


# [start:stop:stepover]
# Basically the same but adding the "step skip"
# In this example is skipping 2 by 2, so that means that is going to skip E in Felipe
print(name[0:3:2]) # Fl


# EXERCISE
# # How to get the reverse name

# start: Omitted, so it defaults to the end of the string when the step is negative.
# stop: Omitted, so it defaults to the beginning of the string (index 0), but the slice goes up to, but not including, the stop index.
# step: -1, which tells Python to traverse the string one character at a time, moving backward
print(name[::-1])