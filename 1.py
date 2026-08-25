

# message  = "hello world"

# my_message  = "hello world, i'm mehrdad"
# print(message,my_message)


# fname  = "amir reza"
# lname  = "TagiZADEh"

# full_name  = f"{fname.title()} {lname.lower()}"

# print(full_name)


# fname = "     Amir Reza     "
# lname = "tagizadeh"
# print(fname,lname)
# print(f"{fname.rstrip()} {lname}")
# print(f"{fname.lstrip()} {lname}")
# print(f"{fname.strip()} {lname.strip()}")


# _url = "https://digikala.com"

# print(_url.removeprefix('https://'))

# fname  = input('Whats your name: ')
# print("hello Dear ",fname)

# print("what's yousr name:")
# fname = input()
# print(fname.title())

# program_language = input()
# x = int(program_language)
# print(x)
# if x ==2 :
#     print('i am integer')


# fname  = input("What's your name: ")

# print("Hello dear:\n",f"{fname.title()}","\n")
# print("Are you ready to start programming: if you say yes we started")
# answer = input()
# if answer == 'yes':
#     print('which program language to choise:\n')
#     print('\t1.python\n\t2.php\n\t 3.c')

# program_language = input()
# program_language = int(program_language)

# if program_language == 1:
#     print('hello to python world')
# if program_language == 2:
#     print('hello to php world')
# if program_language == 3:
#     print('hello to c world')



# under_number  = 13_000_000_000
# print(under_number)
# under_number = 1522222
# print(under_number)

# PI = 3.14
# print(PI)
# PI = 4.14 
# print(PI)

# my_animal = ['dog','cat','mouse','rabbit','hourse']

# print(my_animal)
# print(my_animal[0])

# my_animal.append('ali')

# print(my_animal)


# my_animal[1]= 'ali'

# print(my_animal)

# my_animal.insert(10,'hasan')
# my_animal[8] ='ssss'
# print(my_animal)

# print(len(my_animal))

# my_animal = ['dog','cat','mouse','rabbit','hourse']

# print(my_animal)
# print(my_animal[4])

# print("tole liste man chegadar ast:" ,len(my_animal))

# print(my_animal.pop())
# print("tole liste man bad az pop chegadar ast:" ,len(my_animal))

# del my_animal[3]

# print(my_animal)


# my_animal.remove('dog')
# print(my_animal)

# my_animal.append(1)
# my_animal.append(2)

# print(my_animal)

# for i in range (0,10):
#     kalame = input(f"kalameh {i} ra vared kon")
#     my_animal.append(kalame)

# print(my_animal)

# my_add = []

# for i in range (0,10):
#     add = input(f"adde  {i} ra vared kon: ")
#     my_add.append(add)

# print(my_add)

# my_add =['99', '7', '5', '3', '4', '5', '3', '2', '3', '1']

# my_add.sort() 

# print(my_add)

# my_add =['99', '7', '5', '3', '4', '5', '3', '2', '3', '1']


# print("orginal my list: ", my_add)

# my_add =['99', '7', '5', '3', '4', '5', '3', '2', '3', '1']

# x = sorted(my_add) 

# print("sorted my list: ", x)

# print("orginal my list: ", my_add)




# my_add=[]
# sum=0

# number = int(input("tedad nomarati ke mikhahid jam konid ra beneveisid:"))

# for i in range(0,number):
#     add= int(input(f" add delkhah {i} ro vared konid:\n"))
#     my_add.append(add)



# for i in range(0,len(my_add)):
#     sum = sum + int(my_add[i])

# print(my_add)
# sum =  sum(my_add)
# print(sum)


# minmume = min(my_add)
# maximume  = max(my_add)
# print(f"kamtarin nomre daneshamooz barabar ast ba: {minmume} \n")

# print(f"balatarin nomre daneshamooz barabar ast ba: {maximume} \n")

# print(f"avg nomre daneshamooz barabar ast ba: {sum/len(my_add)}")


# print('1. name danesh amoozan ra vared kon: \n')
# print('2. nomarate danesh amoozan ra vared kon: \n')
# print('3. kamtarin nomre danesh amooz barabar ast ba: \n')
# print('4. bishtarin nomre danesh amoozan barabar ast ba: \n')
# print('5. avg nomre danesh amoozan barabar ast ba: \n')
# print('6. nomre ra dar list nomarat jostojo kon: \n')
# print('7. jahat khroj exit ra type konid: \n')

# guide = ''
# stu_nums=[]
# stu_grades=[]

# while guide != '7':
#     guide  = input('add menu ra vared konid:')
#     if guide == '1':
#         number=int(input('tedad danesh amozan khod ra vare kon:'))
#         for i in range(0,number):
#             nums=input(f"name danesh amoz {i} vared kon:")
#             stu_nums.append(nums)
#     if guide =='2':
#         for j in range(0,number):
#             grades=input(f"nomerat danesh amozan {j} ra be tartib vared kon:")
#             stu_grades.append(grades)
#     if guide =='3':
#         for i in range(0,number):
#             print(f"nomre daneshamooz: {stu_nums[i]} barabar ast ba: {stu_grades[i]}")
#     if guide =='6':
#         req = input('nomre ke mikhahid jostojo koni: ')
#         for x in range(number):
#             if stu_grades[x] == req:
#                 print (f"nomre daneshamooz {stu_nums[x]} barabar {req}")
        
    
        


# student = {'name':'Deniz','grade':20,'course_name' :'adabiyat'}

# print(student['name'])
# print(student['grade'])

# student['fname'] = 'Shayan'


# student['fname'] = 'Amir'

# print(student['fname'])
# speed = int(input('speed ra vared kon:'))


# driver_0 = {'name':'amirreza','flag':0}
# driver_1 = {'name':'mehrdad','flag':10}
# driver_2 = {'name':'mehrdad','flag':10}
# drivers =[driver_0,driver_1,driver_2]
# alert = {'name':'speed','duration':2,'speed_value':100}

# if speed >= alert['speed_value']:
#     print('Dangrooossss')
#     driver['flag'] += 1

# if driver['flag'] >=10 :
#     print('your licnes driver getting to invalid')
# else:
#     print(driver['flag'])


# for key ,value in driver_0.items():
#     print(f"{key} : {value}","\n")

# for key  in driver_0.keys():
#     print(f"{key}","\n")

# for driver in drivers:
#     print(driver)


# student_0 = {}

# students =[]

# for i in range(0,5):
#     name = input('name ra vared kon:')
#     grade = int(input('nomre ra varde kon:'))
#     new_student = {'name':name,'grade':grade}
#     students.append(new_student)

# for student in students:
#     print(student)

# student = {'name':'ali','dars':['riyazi','dini','olum']}

# print(student)

# students = {
#     'student_0' : {
#         'name':'ali',
#         'info':{
#             'father_name':'hasan',
#             'mother_name':'nargges',
#             'address':'roshdiye'
#         },
#         'grades':{
#             'grade_0':{
#                 'name':'math',
#                 'grade':10
#             },
#             'grade_1':{
#                 'name':'physics',
#                 'grade':10
#             },
#         }
#     },
#     'student_1' : {
#         'name':'hasan',
#         'info':{
#             'father_name':'mostfa',
#             'mother_name':'mahrox',
#             'address':'valiasr'
#         },
#         'grades':{
#             'grade_0':{
#                 'name':'math',
#                 'grade':20
#             },
#             'grade_1':{
#                 'name':'physics',
#                 'grade':5
#             },
#         }
#     }
# }

# print(students)
# count_student  =  int(input('tedad danesh amooz ra vared kon:'))
# student_dic = {}
# grade_str = {}
# students  = []
# grades = []
# students_temp = {
#     'student_0' : {
#         'name':'ali',
#         'info':{
#             'father_name':'hasan',
#             'mother_name':'nargges',
#             'address':'roshdiye'
#         },
#         'grades':{
#             'grade_0':{
#                 'name':'math',
#                 'grade':20
#             },
#             'grade_1':{
#                 'name':'physics',
#                 'grade':5
#             },
#         }
#     },
#     'student_1' : {
#         'name':'ali',
#         'info':{
#             'father_name':'hasan',
#             'mother_name':'nargges',
#             'address':'roshdiye'
#         },
#         'grades':{
#             'grade_0':{
#                 'name':'math',
#                 'grade':20
#             },
#             'grade_1':{
#                 'name':'physics',
#                 'grade':5
#             },
#         }
#     }
# }

# for i  in range(0,count_student):
#     name_student = input(f'name danesh amooze {i} ra vared kon:')
#     print('moshakhasat danesh amooz ra be tartib sovalat vared konid:')
#     f_name  = input('name pedare danesh amooz ra vared kon:')
#     m_name  = input('name madare danesh amooz ra vared kon:')
#     address = input('address danesh amooz ra vared kon:')
#     info_dic = {'father_name':f_name,'mother_name':m_name,'address':address}
#     count_subject  =  int(input('tedad dars bardashteh shodeh ra vared konid:'))
#     for j  in range(0,count_subject):
#         subject_name  = input(f'name darse{j}  ra vared kon:')
#         nomre_dars  = input(f'nomre darse{j}  ra vared kon:')
#         grade_dic = {'name':subject_name,'grade':nomre_dars}
#         grade_str = {f'grade_{j}':grade_dic}
#         grades.append(grade_str)

#     student_dic = {'name':name_student,'info':info_dic,'grades':grades}
#     student_str = {f'student_{i}':student_dic}
#     students.append(student_str)
# print(students)


# def say_hello(name):
#     print(f'hi {name}')




# name = ''

# while name !='6':
#     name  =  input('name doste khodra vared konid: ')
#     say_hello(name)


# def describe_pet(animal_type,name='ayyyy'):
#     """display information about pet"""
#     print(f'\nI have a {animal_type}')
#     print(f"\nmy animal type's {animal_type} name is {name}")


# describe_pet(animal_type ='harry')


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# import random
# stu_nums=[]
# stu_grades=[]
# guide = ''

# def print_menu():
#     print('1. name danesh amoozan ra vared kon: \n')
#     print('2. nomarate danesh amoozan ra vared kon: \n')
#     print('3. Didan name va nomre danesh amoozan ra vared kon: \n')
#     print('5. nomre delkhah bareye jostojo ro vared konid:\n')

# def get_sum_student():
#     number=int(input('tedad danesh amozan khod ra vare kon:'))
#     return number


# def get_stundents_name(number)->int:
#     """name danesh amozan ra be list ezafeh mikone"""
#     for i in range(0,number):
#             name = input(f"name danesh amoz {i} vared kon:")
#             stu_nums.append(name)



# print_menu()

# while guide != '6':
#     guide  = input('add menu ra vared konid:')
#     if guide == '1':
#         number =  get_sum_student()
#         get_stundents_name(number)
#     if guide =='2':
#         for j in range(0,number):
#             grades=input(f"nomerat danesh amozan {j} ra be tartib vared kon:")
#             stu_grades.append(grades)
#     if guide =='3':
#         for i in range(0,number):
#             print(f"nomre daneshamooz: {stu_nums[i]} barabar ast ba: {stu_grades[i]}")
#     if guide=='5':
#         req= input('nomre delkhah ke mikhahid vared konid:')
#         for x in range(number):
#             if stu_grades[x]==req:
#                 print(f"nomre mored nazar {stu_nums[x]} barabar {req}")
