# Short circuit
# Breaks every activity in our logic

# OR
# This is not going to be printed
# Because true is short circuiting the
# instructions
# whereas False sentence is going to
# let the print statement being triggered
True or print("Hello world!")
False or print("Hello world!")


# AND
# Is not going to print nothing because is looking for everything
# as True
# thats why True instance worked
False and print("Hello world!")
True and print("Hello world!")



name = None
# Looking for name trhutyness and then show it in uppercase
print(name and name.upper())

