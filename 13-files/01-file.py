# best practice:
# when we finish with some file
# we must close it

my_file = open('./test.txt', 'r')
# It only prints this file once
print(my_file.read())
print(my_file.read())
print(my_file.read())

# seek
# positioning by byte
# 0 means that It'll get back to start
my_file.seek(0)
print(my_file.read())

# readline
# it reads line by line
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())


# readlines
# it reads all the lines from the current text pointer
my_file.seek(10)
print(my_file.readlines())

my_file.close()