students = [{'name': 'ali', 'info': {'father_name': '1', 'mother_name': '1', 'address': '1'},'grades': [{'name': '1', 'grade': 1}],'sum': 1,'miyangin nomerat': 1.0,'bishtrin nomre': 1,'kamtarin nomre': 1}]
print(students)

guid = '1'
    
if guid == '1':
    # req = input('name danesh amoz mored nazar ro vared kon: ')
    found = False
    for s in students:
        print( list(s.values())[1])
    #     student_data = list(s.values())[0]
    #     print(student_data)
    #     if student_data['name'] == req:
    #         # print(f"nomarat daneshamoz {student_data['name']} barabare: {student_data['grades2']}")
    #         found = True
    #         break
    # if not found:
    #     print('daneshjo peyda nashod!')