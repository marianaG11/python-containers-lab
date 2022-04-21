#exercise 1
students = ['Mariana', 'David', 'Samantha', 'Maggie']

print(students[1])
print(students[-1])


#exercise 2 
foods = ('ice cream', 'tacos', 'sushi', 'pizza' )
for food in foods:
    print(f"{food} is a good food")

#exercise 3
for food in foods[-2:]:
  print(food)


#exercise 4 
hometown = {
    'city': 'Chicago', 
    'state': 'IL',
    'population': '2.71 million'
}

print(f"I was born in {hometown['city']}, {hometown['state']}, where there is a population of {hometown['population']}")

#exercise 5
for key, val in hometown.items():
    print(f"{key} = {val}")

#exercise 6
cohort = []
for index, student in enumerate(students):
  cohort.append({
    'student': student,
    'favorite_food': foods[index]
  })
for student in cohort:
  print(student)

#exercise 7
awesome_students = [f"{student} is awesome!" for student in students]
for  student_name in awesome_students:
    print(student_name)

#exercise 8  
# [<expression> for <item> in <list>]
# This reads as: I want <expression> for each <item> in <list>
a_in_foods = [food for food in foods if 'a' in food]
print(a_in_foods)