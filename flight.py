# import csv
# students = []
# with open('flights.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         students.append(row)
# filtered_students = [row for row in students if int(calculate(row["weight"], row["height"])) < 2]

student_info = [{'first name':'Caroline', 'last name':'Harrison', 'birthdate':'1997-03-02'}, {'first name':'Rachel', 'last name':'Reynolds', 'birthdate':'1996-01-07'}, {'first name':'Olivia', 'last name':'James', 'birthdate':'1998-05-09'}]
youngest_student_info = min(student_info, key=lambda x: x['birthdate'])
print(youngest_student_info)
