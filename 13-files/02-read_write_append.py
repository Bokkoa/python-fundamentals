
# in file contexts this keyword allow us
# to automatically close this file after its use

# mode = r is for read mode
with open('test.txt', mode='r') as my_file:
  print(my_file.readlines())
  
# w for write
with open('file.txt', mode='w') as my_file:
  # this is going to override all the file
  text = my_file.write(":D")
  
  
# r+ stands for read and write
with open('test.txt', mode='r+') as my_file:
  # this is going to read (so the pointer will move)
  # and then write the file
  print(my_file.readlines())
  text = my_file.write("Hello worlD")
  
# a stands for append
with open('test.txt', mode='a') as my_file:
  # this is going to write at the end of the file
  text = my_file.write("Something!")
  print(text)