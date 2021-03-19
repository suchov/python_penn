# # some example of working with dic

# person = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
# print(type(person))
# print(person)
# print(person['name'])
# print(person.get('name'))
# print(person.get('state', 'PA')) # will return the PA if the state key does not exist

# dictionaries are mutable so elements can be updated or added

# create a Grade/attendance book for students

# create a dictionary for each student
billy = {'name': 'Billy', 'grades': [100, 80, 67, 100, 89], 'attendance': [True, True, True, True, True]}
sarah = {'name': 'Sarah', 'grades': [0, 99, 0, 100, 0], 'attendance': [True, False, True, False, True]}
ben = {'name': 'Ben', 'grades': [60, 82, 71, 92, 100], 'attendance': [False, False, False, False, False]}

students = {'1': billy, '2': sarah, '3': ben}

# get the number of students

print(len(students))

# get all the students id's 

print(students.keys())

# iterate over the students

for k in students:
    print('key:', k)

# get billy's attendance
billy_get = students['1']
print(billy_get['attendance']) # print(students['1']['attendance']) - works too

# get the sarah's grades
print(students.get('2').get('grades'))

print(students.get('1')['name']) # get the first student name

# get all key:value pairs for ben

items = students.get('3').items()
for key, val in items:
    print(key, val)

# get average stuent grade for all assignments
grades = []
items = students.items() # key:value pairs for students

for key, val in items:
    for g in val['grades']:
        grades.append(g)

# average grade
print(round(sum(grades) / len(grades)))

# and another way to do this
grades_concatenated = []
items = students.items() #key:value pairs for students
for key, val in items:
    grades_concatenated += val['grades'] #concatenate list of grades

# average grade
print(round(sum(grades_concatenated) / len(grades_concatenated)))
