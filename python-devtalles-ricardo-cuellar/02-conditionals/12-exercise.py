# Instructions:
# You will create a program to evaluate potential candidate profiles for HR.
# The program will extract the name, years of experience, and skills.

# Evaluation rules:
# If the candidate knows Python/Django and has +3 years of experience → Optimal Candidate
# If the candidate knows Python/Django and has +1 year of experience → Good Candidate
# If the candidate does not know Python/Django but has experience in something else → Possible Candidate
# If the candidate does not know Python at all → Not optimal, save CV

# Tip:
# Use the .split() method to process the fields.

# MY SOLUTION
DJANGO = "django"
PYTHON = "python"

has_more_skills = True

skills = {}

name = input("Enter your name: ")

while has_more_skills:
  new_skill = input("Enter the languages and frameworks that you know: ")
  new_year = input("Enter your years of experience: ")
  
  normalized_skill = new_skill.lower()
  normalized_year = int(new_year) or 0
  
  skills[normalized_skill] = normalized_year
  
  should_add_new = input("Do you want to add other skill Y/N?").capitalize()
  
  has_more_skills = should_add_new == 'Y'


if DJANGO in skills or PYTHON in skills:
  if skills[DJANGO] >= 3 or skills[PYTHON] >= 3:
    print("Optimal Candidate")
  if skills[DJANGO] >= 1 or skills[PYTHON] >= 1:
    print("Good Candidate")
else:
  if len(skills) >= 1:
    print("Possible Candidate")
  else:
    print("Not optimal, save CV")
    
    
# ORIGINAL SOLUTION
name = input("Candidate's name: ")
experience = int(input("Years of experience: "))
skills = input("Enter your skills split by commas e.g. Laravel, Golang, Django, etc: ").split(",")

evaluate_skills = "Python" in skills or "Django" in skills

result = ""

if evaluate_skills:
  if experience >= 3:
    result = "Optimal Candidate"
  elif experience >= 1:
    result = "Good Candidate"
  else:
    result = "Possible Candidate"
else:
  result = "Not optimal, save CV"

print(f"The candidate {name} is {result}")