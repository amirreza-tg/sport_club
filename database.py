import mysql.connector

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="club",
        charset="utf8mb4",
        collation="utf8mb_general_ci"
    )


# sql = """
# SELECT m.Fname, m.Lname, p.startdate, p.enddate
# FROM member m 
# JOIN membership p ON m.id = p.member_id
# WHERE p.enddate BETWEEN '2026-08-08 08:00:00'
#                     AND '2026-08-22 12:00:00';
# """
# cursor.execute(sql)
# result = cursor.fetchall()

# for row in result:
#     print(row)


# id = int(input('id morabi ra vared kon: '))
# f_name = input('name morabi ra vared kon: ')
# l_name = "alizadeh"
# speciality = "CX"
# start_date = "1404-03-03 00:00:00"
# salary = 10000
# hire_date = "1405-05-16"

# sql = """
# INSERT INTO coach (`id`, `f_name`, `l_name`, `start_date`, `speciality`, `salary`, `hire_date`) 
# VALUES (%s, %s, %s, %s, %s, %s, %s)
# """

# cursor.execute(sql, (id, f_name, l_name, start_date, speciality, salary, hire_date))
# connection.commit()
# print("Coach added successfully!")

# connection.close()

def main_menu():
    print("   AB gym - menue Asli")
    print("1. Gozaresh giri didn eteleaat:")
    print("2. Tanzimat (vared krdn etelat jadid):")
    print("0. khoroj az barname:")
    print("="*40)








def report_menu():
    print('\n 1. baraye didn moshakhasat member :')
    print('\n 2. baraye didn morabi member ba name class:')
    print('\n 3. baraye didn plan member morede nazar: ')
    print('\n 4. baraye didn vaziyt payment member mored nazar:')
    print('\n 5. baraye didn morabi mored nazar behmrahe klass va tedade shagerd hayash:')
    print('\n 6. baraye didn barname ghazayi member mored nazar ba name coach:')
    print('\n 7. baraye didn barname varzeshi member morede nazar ba name coach:')
    print('\n 8. baraye didn locker haye azad:')
    print('\n 9. baraye didn kaarkonan  bashghah:')
    print("\n 0. Bazgasht be menu asli:")
 

def settings():
    print('\n 1.baraye vred krdn moshakhasat member jadid :')
    print('\n 2.baraye vred krdn moshakhasat morabi jadid :')
    print('\n 3.baraye vred krdn moshakhasat class jadid :')
    print('\n 20.baraye vred krdn moshakhasat classregestration jadid :')
    print('\n 4.baraye vred krdn moshakhasat membership jadid :')
    print('\n 5.baraye vred krdn moshakhasat payment jadid :')
    print('\n 6.baraye vred krdn moshakhasat food jadid :')
    print('\n 7.baraye vred krdn moshakhasat fooddiet jadid :')
    print('\n 8.baraye vred krdn moshakhasat dietprogram jadid :')
    print('\n 9.baraye vred krdn moshakhasat exrecise jadid :')
    print('\n 13.baraye vred krdn moshakhasat exerciseprogram jadid :')
    print('\n 12.baraye vred krdn moshakhasat workoutprogram jadid :')
    print('\n 10.baraye vred krdn moshakhasat locker jadid :')
    print('\n 11.baraye vred krdn moshakhasat memberlocker jadid :')
    print('\n 14.baraye vred krdn moshakhasat equipmtent jadid :')
    print('\n 15.baraye vred krdn moshakhasat equipmtentmaintance jadid :')
    print('\n 16.baraye vred krdn moshakhasat invoice jadid :')
    print('\n 17.baraye vred krdn moshakhasat attendance jadid :')
    print("\n 0. Bazgasht be menu asli:")

def show_member_details():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    member_id=input("ID member ra vared kon:")
    cursor.execute("select * from member where id=%s",(member_id))
    row=cursor.fetchone()
    if row:
        for key,value in row.items():
            print(f"  {key}:{value}")
    else:
        print("member payda nashod!")         
 
    cursor.close()
    con.close()           

def show_coach_with_class():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    sql=""" select  c.f_name,c.l_name,cl.className as class_name
            from coach c   
            left join class cl 
            on c.id=cl.coach_id"""
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(f"  {row['f_name']} {row['l_name']} | class:{row['class_name']}")
    cursor.close()
    con.close()    

def show_payment_status():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    member_id=input("ID member ra vared kon:")
    cursor.execute("select * from payment where member_id=%s",(member_id))
    rows=cursor.fetchall()
    total=sum( r['amount'] for r in rows) if rows else 0
    print(f" tedade pardakht:{len(rows)} | majmo:{total}")
    cursor.close()
    con.close()

def show_coach_atudents():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    sql="""
            select c.f_name,c.l_name,cl.className as class_name,count(cr.member_id)as student_count
            from coach c
            left join class cl on cl.coach_id=c.id
            left join classregitration cr on cr.class_id=cl.id
            group by c.id,cl.id
    """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(f"{row['f_name']} {row['l_name']} | {row['class_name']} | shagerd:{row['student_count']}")
    cursor.close()
    con.close()    


def show_workout_program():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    member_id=input("ID member ra vared kon:")
    cursor.execute("""
                        select m.Fname,m.Lname,wp.*,e.exerciseName as exercise_name,ep.reps as tedade_harakat
                        from memer m left join workoutprogram wp on m.id=wp.member_id
                        join exerciseprogram ep on ep.exercise_id=e.id
                        where wp.member_id=%s
    
                                            """,(member_id))
    rows=cursor.fetchall()
    if rows:
        print(f"barname varzeshi :  {rows[0]['Fname']} {rows[0]['Lname']}")
        for row in rows:
            print(f"   {row['exercise_name']} {row['tedade_harakat']}")
    else:
        print("barname varzeshi payda nashod!")
    cursor.close()
    con.close()


def show_diet_program():
    con=get_connection()
    cursor=con.cursor()
    member_id=input('ID member ra vared konid:')
    cursor.execute(""""
    select f.foodName,dp.goal as hadafe_program,wp.*
    from workoutprogram wp 
    join programexercise ep on wp.id=ep.program_id
    join exercise e on ep.exercise_id=e.id
    where wp.member_id=%s """ ,(member_id))
    for row in cursor.fetchall():
        print(f"  {row['exercise_name']}")

    cursor.close()
    con.close()

def show_member_plan():
    con=get_connection()
    cursor=con.cursor()
    member_id=input("ID member morede nazar ra vared konid:")
    cursor.execute("""select m.Fname.m.Lname,mp.plan_name
                      from member m join memnership ms  on m.id=ms.member_id
                      join membership_plan mp on mp.id=ms.plan_id
                      where member_id=%s""",(member_id))
    rows=cursor.fetchall()
    if rows:
        print(" plan member morede nazare :{rows[0]['Fname']} {rows[0]['Lname']}")
        for row in rows:
            print(f"{row['plan_name']}")
    else:
        print("member plan nadard!")        



def show_free_lockers():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    cursor.execute(""" select * from locker l
                        where l.id not in (select locker_id from memberlocker where enddate> now())""")
    for row in cursor.fetchall():
        print(f" locker  ///{row['id']}-number:{row.get('lockernumber','N/A')} ")




def show_employees():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    cursor.execute("select * from employee") 
    for row in cursor.fetchall():
        print(f" {row.get('f_name','')}  {row.get('l_name','')} | post:{row.get('position','N/A')}")           
    cursor.close()
    con.close()

