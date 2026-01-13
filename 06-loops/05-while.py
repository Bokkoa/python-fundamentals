
# Infinite Loop (careful)
#while True:
 # print("This never gonna stop")
 

counter = 1
while counter <= 5:
  print(f"- {counter}")
  counter += 1
else:
  print("We finished")

response = ''

while response.lower() != 'python':
  response = input("Type python for exit: ")
  
print("We finished, actually exited!")