python_course = { 'Ana', 'Luis', 'Pedro', 'Maria'}
java_course = { 'Jose', 'Ricardo', 'Pedro', 'Miguel'}

student_in_two_courses = python_course.intersection(java_course)
print(student_in_two_courses) # Pedro

only_python = python_course.difference(java_course)
print(only_python) # Maria, Ana, Luis

all_students = python_course.union(java_course)
print(all_students) # {'Miguel', 'Luis', 'Ricardo', 'Pedro', 'Jose', 'Ana', 'Maria'}