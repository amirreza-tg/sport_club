students ={}
student_counter=1
import json

count = int(input('tedade danesh amoz ro vared kon: '))


def get_info_students(name_students):
    u_name=input('shomare daneshjoyi:')
    f_name = input('name pedar: ')
    m_name = input('name mother: ')
    add = input('address: ')
    students[name_students] = {
        'info': {
            'user_number':u_name,
            'father_name': f_name,
            'mother_name': m_name,
            'address': add
        }
    }


def get_grades_students(count_sub,name_students):

    print(count_sub,name_students)

    if name_students not in students:
            students[name_students] = {}

    if 'grades' not in students[name_students]:
        students[name_students]['grades'] = {}

    for j in range(count_sub):
        subject_name = input(f'name darse {j+1} ra vared kon: ')
        nomre_dars = int(input(f'nomre darse {j+1} ra vared kon: '))


        students[name_students]['grades'][subject_name] = nomre_dars
    

def save_professor_of_studetents():

    if 'teachers' not in students[name_students]:
        students[name_students]['teachers']={}


    grades=students[name_students].get('grades',{})

    
    for subject_name,nomre_dars in grades.items():
        ostad_dars=input(f'naame ostade darse {subject_name} ro vared kon:')
        user_ostad=input(f'code ostad{subject_name}ro vared kon:')
        
        if ostad_dars not in students[name_students]['teachers']:
            students[name_students]['teachers'][ostad_dars]={}
        students[name_students]['teachers'][ostad_dars][subject_name]={
            'nomre':nomre_dars,
            'code_ostad':user_ostad
        }





def print_menu():
    print('\n1. baraye didan nomre daneshjo mored nazar')
    print('2. baraye didan bishtrin va kamtarin nomre daneshjo mored nazar')
    print('3. baraye didan moadel danesh amoz mored nazar')
    print('4. baraye didan moadel kol daneshjoyan')
    print('5.baraye zakhire etelat hameye danshjoyan')
    print('6. khorooj')
    print('7.baraye didn etelaat ostade morede nazar')


# ========== MENU  ==========

def get_name_of_specific_student():
    return input('name danesh amoz mored nazar ro vared kon: ')

def find_student_name(m):
    if m in students:
        return students[m]
    return None

def get_student_gardes_list(student_data):
    if 'grades' not in student_data:
        return []
    return list(student_data['grades'].values())

def get_professor_of_students_subject(name_students):
    if 'teachers' not in students[name_students]:
        students[name_students]['teachers']={}

    grades=students[name_students].get('grades',{})

    for subject_name,nomre_dars in grades.items():
        ostad_dars=input(f'naame ostad darse {subject_name} ro vared kon:')
        user_ostad=input(f'code ostad {subject_name} ro vared kon:')
        if ostad_dars not in students[name_students]['teachers']:
            students[name_students]['teachers'][ostad_dars]={} 

        students[name_students]['teachers'][ostad_dars][subject_name]={
            'nomre':nomre_dars,
            'code_ostad':user_ostad
        }   

def save_student_to_file(name,data,counter):
    filename=f"student_{counter}_{name}.json"
    
    info=data.get('info',{})
    grades=data.get('grades',{})
    grades_list=list(grades.values())
    
    json_data={
        "student_name":name,
        "personal_info":{
            "shomare_daneshjoyi":info.get('user_number', 'N/A'),
            "name_pedar":info.get('father_name', 'N/A'),
            "name_madar":info.get('mother_name','N/A'),
            "adress":info.get('address','N/A'),
        },
        "grades":grades,
        "summary":{}
    }
    if grades_list:
        json_data["summary"]={
            "bishtarin_nomre":max(grades_list),
            "kamtarin_nomre":min(grades_list),
            "miyangin_nomre":round(sum(grades_list)/len(grades),2)
        }
    else:
        json_data["summary"]={
            "bishtarin_nomre":None,
            "kamtarin_nomre":None,
            "miyangin_nomre":None,
            "note":"hich nomre vared nashod!"   
        }

    with open(filename, 'w',encoding='utf-8')as f:
        json.dump(json_data,f, ensure_ascii=False, indent=4)



#     filename=f"student_{counter}_{name}.txt"
    
#     with open(filename,'w',encoding='utf-8') as f:
#         f.write(f"{'='*40}\n")
#         f.write(f"  ETELAAT DANESHJO:{name}\\n")
# #اطلاعات شخصی
#         f.write("*** moshakhsat shakhsi***")
#         info=data.get('info', {})
#         f.write(f"shomare daneshjoyi: {info.get('user_number', 'N/A')}\\n")
#         f.write(f"name pedar: {info.get('father_name','N/A')}\\n")
#         f.write(f"name madar: {info.get('mother_name','N/A')}\\n")
#         f.write(f"Address: {info.get('address','N/A')}\\n")
# #نمرات 
#         f.write("////nomarat////")
#         grades=data.get('grades',{})
#         if grades:
#             for subject,score in grades.items():
#                 f.write(f"  {subject}:{score}\\n")
#             grades_list=list(grades.values())
#             f.write(f"\\n bishtarin nomre: {max(grades_list)}")
#             f.write(f" kamtarin nomre : {min(grades_list)}\\n") 
#             f.write(f" miyangin nomerat :{sum(grades_list)/len(grades_list)}")
#         else:
#             f.write('hich nomre vared nashod!\\n')

    print(f"File'{filename}'ba moafagiyt zakhire shod")
    return filename

def save_teachers_to_file():
    teachers_data={}

    for subject_name,student_data in students.items():
        teachers=student_data.get('teachers',{})
        for Teacher_name, subjects in teachers.items():
            for subject_name,subject_info in subjects.items():
                teacher_code=subject_info.get('code_ostad', 'N/A')
                nomre=subject_info.get('nomre',0)

                if teacher_code not in teachers_data:
                    teachers_data[teacher_code]={
                        'teacher_name': Teacher_name,
                        'teacher_code': teacher_code,
                        'subjects':{}
                    }

                if subject_name not in teachers_data[teacher_code]['subjects']:
                    teachers_data[teacher_code]['subjects'][subject_name]={
                        'students':[],
                        'grades':[]
                    }
                teachers_data[teacher_code]['subjects'][subject_name]['grades'].append(nomre)

        for teacher_code , data in teachers_data.items():
            for subject_name,subject_data in data['subjects'].items():
                grades=subject_data['grades']
                if grades:
                    subject_data['miyangin_kelasi']=round(sum(grades)/len(grades),2)
                else:
                    subject_data['miyangin_kelasi']=None
                del subject_data['grades']

            filename=f"teacher_{teacher_code}_{data['teacher_name']}.json"
            with open(filename,'w',encoding='utf-8') as f:
                json.dump(data,f,ensure_ascii=False,indent=4)
            print(f"file'{filename}' ba movafagiyat zakhire shod")
        return teachers_data

def show_teacher_info():
    teacher_code=input('cde ostad ra vard konid:')

    found=False
    teacher_data=None

    for student_name,student_data in students.items():
        teachers=student_data.get('teachers',{})
        for teacher_name,subjects in teachers.items():
            for subject_name,subject_info in subjects.items():
                if subject_info.get('code_ostad')==teacher_code:
                    found = True
                    if teacher_data is None:

                        teacher_data = {
                            "teacher_name":teacher_name,
                            "teacher_code":teacher_code,
                            "subjects":{}
                        }


                                                                
                    if subject_name not in teacher_data["subjects"]:
                        teacher_data["subjects"][subject_name]={
                            "students":[],
                            "grades":[]
                        }

                    teacher_data["subjects"][subject_name]["students"].append({
                        "student_name":student_name,
                        "grade":subject_info.get('nomre',0)
                    })
                    teacher_data["subjects"][subject_name]["grades"].appaend(subject_info.get('nomre',0))    

        if not found:
            print('ostad payda nashod!')
            return
    print(f"\n{'='*50}")
    print(f"  Etelaat Ostad: {teacher_data['teacher_name']}")
    print(f"  Code Ostad: {teacher_data['teacher_code']}")
    print(f"{'='*50}")


    for subject_name, subject_data in teacher_data["subjects"].items():
        print(f"\n dars:{subject_name}")
        print(f"  {'-'*40}")

        for student in subject_data["students"]:
            print(f" -{student["student_name"]} :{student['grade']}")

        grades=subject_data["grades"]
        if grades:
            miyangin=sum(grades)/len(grades)
            print(f"  \n MIYANGIN KELASI:{miyangin:.2f}")




def  save_all_students_to_file():
     
     

     """ذخیره همه دانشجویان تو یک فایل"""
     filename="all_students.json"
     all_data={
         "title":"gozaresh kol daneshjoyan",
         "total_students":len(students),
         "students":[],
         "overall_summary":{}
     }
     total_means=[]



     for i,(name,data) in enumerate(students.items(),1):
         info=data.get('info',{})
         grades=data.get('grades',{})
         grades_list=list(grades.values())
         student_entery={
             "id":i,
             "name":name,
             "personal_info":{
                 'shomaredaneshjoyi':info.get('user_number','N/A'),
                 'name_pedar':info.get('father_name','N/A'),
                 'address':info.get('address','N/A')
             },
             "grades":grades,
             "summary":{}
         }


         if grades_list:
            mean=sum(grades_list)/len(grades_list)
            total_means.append(mean)
            student_entery["summary"]={

                "bishtarin_nomre":max(grades_list),
                "kamtarin_nomre":min(grades_list),
                "miyangin_nomre":round(mean,2)
        }
         else:
            student_entery["summary"]={
                "bishtarin_nomre":None,
                "kamtrin_nomre":None,
                "miyangin_nomre":None,
                "note":"hich nomrei vared nashode!"             
         }
         all_data['students'].append(student_entery)      
     if total_means:
         all_data["overall_summary"]={
             "moadel kol daneshjoyan":round(sum(total_means)/len(total_means),2)

         }
     else:
             all_data['overall_summary']={
             "moadel kol daneshjoyan":None,
             "note":"hich daneshjoyi vared nashode!"
             }    
     with open(filename,'w',encoding='utf-8') as f:
         json.dump(all_data,f,ensure_ascii=False,indent=4)
     print(f" file {filename} ba movafagiyt zakhire shod.")

    # filename="all_students.txt"
    # with open(filename,'w',encoding='utf-8')as f:
    #     f.write(f"gozaresh ko; hameye daneshjoyan\\n")

    #     total_means=[]
    #     for i,(name,data) in enumerate(students.items(),1):
    #         f.write(f" daneshjo{i}: {name}\\n")
    #         info = data.get('info', {})
    #         f.write(f"  Shomare Daneshjoyi: {info.get('user_number', 'N/A')}\\n")
    #         f.write(f"  Name Pedar: {info.get('father_name', 'N/A')}\\n")
    #         f.write(f"  Name Madar: {info.get('mother_name', 'N/A')}\\n")
    #         f.write(f"  Address: {info.get('address', 'N/A')}\\n\\n")
    #         f.write("nomerat:\\n")
    #         grades=data.get('grades')
    #         grades=data.get('grades', {})
    #         if grades:
    #             for subject,score in grades.items():
    #                 f.write(f"  {subject}:{score}")
    #             grades_list=list(grades.values())
    #             mean= sum(grades_list)/len(grades_list)
    #             total_means.append(mean)
    #             f.write(f"\n    Bishtarin Nomre: {max(grades_list)}\n")
    #             f.write(f"    Kamtarin Nomre: {min(grades_list)}\n")
    #             f.write(f"    Miyangin Nomre: {mean:.2f}\n")
    #         else:
    #             f.write("    Hich nomrei vared nashode!\n")     
    #         f.write(f"\n{'='*50}\n")
    #         f.write(f"    Moadel Kol Daneshjoyan\n")
    #     if total_means:
    #         f.write(f"  Moadel Kol: {sum(total_means)/len(total_means):.2f}\n")
    #     else:
    #         f.write(f"  Hich daneshjoi vared nashode!\n")
    # print(f"File '{filename}' ba movafaghiat zakhire shod!")
     return filename 

for i in range(count):
    name_students = input(f'\n name danesh amoz {i+1} ro vared kon: ')
    print('moshakhasat danesh amoz ro vared kon:')
    get_info_students(name_students)
    
    
    count_sub = int(input('tedad dars daneshamoz: '))
    get_grades_students(count_sub,name_students)

    get_professor_of_students_subject(name_students)

    save_student_to_file(name_students,students[name_students],student_counter)
    student_counter += 1

    print(students)     
  
print_menu()


while True:

    guid = input('\nadade menu ro vared konid: ')
    
    match guid:
        case '1':
            req=get_name_of_specific_student()    
            student_data=find_student_name(req)
            if student_data:
                grades_list=get_student_gardes_list(student_data)
                print(f"nomarat daneshamoz {req} barabare: {grades_list}")
            else:
                print('daneshjo peyda nashod!')
        case '2':
            reg = input('name danesh amoz mored nazar ra vared kon: ')
            student_data=find_student_name(reg)
            if student_data:
                grades_list=get_student_gardes_list(student_data)
                if grades_list:

                    print(f'bishtarin nomre: {max(grades_list)}')
                    print(f'kamtarin nomre: {min(grades_list)}')
                else:
                    print('hich nomre vared nashod')
            else:
                print('daneshjo peyda nashod!')
    
        case '3':
            rez = get_name_of_specific_student()
            student_data=find_student_name(rez)
            if student_data:
                grades_list=get_student_gardes_list(student_data)
                if grades_list:
                    mean=sum(grades_list)/len(grades_list)
                    print(f'miyangin nomerat daneshjo {rez} barabare: {mean}')
                else:
                    print('hich nomrei vared nashode')
            else:        
                print('daneshjo peyda nashod!')
    
        case '4':
            if len(students) > 0:
                print('\n--- moadel hame daneshjoyan ---')
                total_sum = 0
                valid_count = 0
                for name, data in students.items():
                    grades_list =get_student_gardes_list(data)
                    if grades_list:
                        mean = sum(grades_list) / len(grades_list)
                        print(f'{name}: {mean}')
                        total_sum += mean
                        valid_count += 1
                if valid_count > 0:
                    moadel_kol = total_sum / valid_count
                    print(f'\nmoadel kol daneshjoyan: {moadel_kol}')
                else:
                    print('hich nomrei vared nashode!')
            else:
                print('hich daneshjoi vared nashode!')
        case '5':
            print('\n--- Zakhire Etelaat Dar File ---')
            counter = 1
            for name, data in students.items():
                save_student_to_file(name, data, counter)
                counter += 1
            save_all_students_to_file()
            save_teachers_to_file() 

        case '6':
            print('khodafez!')
            break

        case '7':
            print('\n----ETELAATE ASATID-----')
            show_teacher_info()

# ========== FINAL OUTPUT ==========
print('\n--- data kamel ---')
print(students)
