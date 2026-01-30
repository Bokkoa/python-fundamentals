students = {
  "Ana": [8, 7, 9],
  "Luis": [6, 5, 7],
  "Sofía": [10, 9, 10]
}

# Add new student
# Calculate the average of an existing student
# Calculate the average of the new student


# add student
# students['Vianey'] = students.get('Vianey', [7, 8, 9])
students.update({ 'Vianey': [8, 9, 10]})
print(students)

name = 'Ana'
# Average existing student
if name in students:
  ana_average = sum(students[name]) / len(students[name])
  print(ana_average)
else:
  print('Ana is not a student')


# Average new student
name = 'Vianey'
vianey_average = sum(students[name]) / len(students[name])
print(vianey_average)