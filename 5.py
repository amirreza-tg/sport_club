
print('1. name danesh amoozan ra vared kon: \n')
print('2. nomarate danesh amoozan ra vared kon: \n')
print('3. Didan name va nomre danesh amoozan ra vared kon: \n')
print('5. nomre delkhah bareye jostojo ro vared konid:\n')
stu_nums=[]
stu_grades=[]
guide = ''

while guide != '6':
    guide  = input('add menu ra vared konid:')
    if guide == '1':
        number=int(input('tedad danesh amozan khod ra vare kon:'))
        for i in range(0,number):
            nums=input(f"name danesh amoz {i} vared kon:")
            stu_nums.append(nums)
    if guide =='2':
        for j in range(0,number):
            grades=input(f"nomerat danesh amozan {j} ra be tartib vared kon:")
            stu_grades.append(grades)
    if guide =='3':
        for i in range(0,number):
            print(f"nomre daneshamooz: {stu_nums[i]} barabar ast ba: {stu_grades[i]}")
    if guide=='5':
        req= input('nomre delkhah ke mikhahid vared konid:')
        for x in range(number):
            if stu_grades[x]==req:
                print(f"nomre mored nazar {stu_nums[x]} barabar {req}")


        
