# message = "hello wold"
# my_message = "hello world, im amir"
# print(message,my_message)


# fname = "amir reza"
# lname = "taghizadeh"

# full_name = f"{fname.title()}{lname.lower()}"
# print(full_name)


# fname="    amir reza   "
# lname ="taghizadeh"
# print(fname,lname)
# print(f"{fname.rstrip()} {lname}")
# print(f"{fname.lstrip()} {lname}")
# print(f"{fname.strip()} {lname.strip()}")

# _url= "https://digikala.com"
# print(_url.removeprefix('https://'))

# fname= input('whats your name:')
# print("hello dear ",fname)


# print("what is your name: ")
# fname = input()
# print(fname.title())

# programm_language= input()
# x= int(programm_language)
# print(x)
# if x==2:
#     print('im a integer')

# fname = input("what is your name:")

# print("hello dear:\n" ,f"fname.titile()","\n")
# print("are you ready to start programming: if you say yes we started")
# answer= input()
# if answer == 'yes':
#     print ("wich program languag do you want: \n" )
#     print('\t1.phyton \n \t2.php\n \t3.c')

# program_language= input()    
# program_language= int(program_language)

# if program_language==1:
#     print('hello to phyton world')
# if program_language==2:
#     print('hello to php world')    
# if program_language==3:
#     print('hello to c world')

# under_number  = 13_000_000_000
# print(under_number)
# under_number = 1522222
# print(under_number)


# PI = 3.14
# print(PI)
# PI = 4.14 
# print(PI)

# my_animal= ['cat','dog','mouse','rabbit','hourse']

# print(my_animal)
# print(my_animal[2])

# my_animal.append('ali')
# print(my_animal)

# my_animal[1]='ali'
# print(my_animal)


# my_animal.insert(10,'hasam')
# my_animal[8]='snake'
# print(my_animal)


# print(len(my_animal))

# my_add=[]
 
# for i in range(0,10):
#     add=input(f"adde {i} ro vared konid:")
#     my_add.append(add)


# print(my_add)

# my_add=['', '7', '7', '6', '0', '4', '8', '8', '5', '3']

# my_add.sort()

# print(my_add)

# my_add=['', '7', '7', '6', '0', '4', '8', '8', '5', '3']
# print("my orginal list:",my_add)
# x=sorted(my_add)
# print("sortd my list:",x)
# print("my original list is:",my_add)

count_stu=int(input('tedad daneshamoz ro vared kon:'))
stu_dict={}
grade_str={}
stu=[]
grades=[]
stu_temp={
    'student_0':{
        'name':'ali',
        'info':{
            'father':'amir',
            'mother':'maryam',
            'adress':'pastour'
        },
        'grades':{
        'grade_0':{
            'name':'math',
            'grade':5
        },
        'grade_1':{
            'name':'physics',
            'grade':2.5
        }
        }
        },
    'student_1':{
        'name':'reza',
        'info':{
            'father':'bahram',
            'mother':'leila',
            'address':'roshdiye'
        },
        'grade':{
            'grade_0':{
                'name':'math',
                'grade':'19.5'

            },
            'grade_1':{
                'name':'physics',
                'grade':18
            }
        }
        }    

    } 
# print(stu_temp)
students=[]
for i  in range(0,count_stu):
    name_student = input(f'name danesh amooze {i} ra vared kon:')
    print('moshakhasat danesh amooz ra be tartib sovalat vared konid:')
    f_name  = input('name pedare danesh amooz ra vared kon:')
    m_name  = input('name madare danesh amooz ra vared kon:')
    address = input('address danesh amooz ra vared kon:')
    info_dic = {'father_name':f_name,'mother_name':m_name,'address':address}
    count_subject  =  int(input('tedad dars bardashteh shodeh ra vared konid:'))
    for j  in range(0,count_subject):
        subject_name  = input(f'name darse{j}  ra vared kon:')
        nomre_dars  = input(f'nomre darse{j}  ra vared kon:')
        grade_dic = {'name':subject_name,'grade':nomre_dars}
        grade_str = {f'grade_{j}':grade_dic}
        grades.append(grade_str)

    student_dic = {'name':name_student,'info':info_dic,'grades':grades}
    student_str = {f'student_{i}':student_dic}
    students.append(student_str)
print(students)


