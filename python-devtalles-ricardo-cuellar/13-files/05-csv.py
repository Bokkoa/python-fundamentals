import csv

with open('data.csv', 'w', newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["Name", "Age"])
  writer.writerow(["Felipe", 28])
  writer.writerow(["Kone", 20])
  
with open('data.csv', 'r') as file:
  reader = csv.reader(file)
  
  for row in reader:
    print(row)