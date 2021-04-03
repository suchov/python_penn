import csv
students = []
with open('MOOC.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append(row)
filtered_students = [row for row in students if (int(row["age"]) < 30 and float(row["weight"]) < 190)]
for student in filtered_students:
    print(student["name"], student["age"], student["weight"])