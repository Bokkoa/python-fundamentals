
# relative path
with open('./file_folder/relative.txt', mode='r') as my_file:
  print(my_file.readlines())
  
  
  
# absolute path
with open('C:/path/to/your/folder/file_folder/relative.txt', mode='r') as my_file:
  print(my_file.readlines())