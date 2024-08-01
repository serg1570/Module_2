grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
if len(grades) == len(students):
    students = list(students)
    students = sorted(students)
i = 0
dict_students = {}
while i < len(students):
    dict_students[students[i]] = sum(grades[i]) / len(grades[i])
    i = i + 1
print(dict_students)


