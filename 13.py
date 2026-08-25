my_students=[]
my_grades=[]
for i in range (0,10):
    name_of_students=input(f" naam{i}khod ra vared konid:\n")
    my_students.append(name_of_students)
    for j in range (0,10):
        grades=int(input(f"nomerat {j}khod ra vared konid:\n")) 
        my_grades.append(grades)

