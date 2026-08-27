import mysql.connector

from mysql.connector import Error

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="club",
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )

def do_insert(table_name, columns, values):

    conn = get_connection()
    cursor = conn.cursor()
    
    placeholders = ", ".join(["%s"] * len(values))
    cols = ", ".join(columns)
    
    sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
    
    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"✅ Sabt shod! ID: {cursor.lastrowid}")
        return cursor.lastrowid
    except Error as e:
        print(f"❌ Error: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()
        conn.close()


def do_update(table_name, id_column, record_id, updates):
    """
    updates: {'Fname': 'Reza', 'phone': '0913...'}
    """
    if not updates:
        print("❌ Hich meghdari baraye virayesh vared nashod!")
        return
    
    conn = get_connection()
    cursor = conn.cursor()
    
    
    set_clause = ", ".join([f"{col} = %s" for col in updates.keys()])
    values = list(updates.values()) + [record_id]
    
    sql = f"UPDATE {table_name} SET {set_clause} WHERE {id_column} = %s"
    
    try:
        cursor.execute(sql, values)
        conn.commit()
        if cursor.rowcount > 0:
            print(f"✅ {cursor.rowcount} radif virayesh shod!")
        else:
            print("⚠️ Radifi peyda nashod!")
    except Error as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# ─── GENERIC DELETE ───
def do_delete(table_name, id_column, record_id):
    conn = get_connection()
    cursor = conn.cursor()
    

    cursor.execute(f"SELECT * FROM {table_name} WHERE {id_column} = %s", (record_id,))
    row = cursor.fetchone()
    
    if not row:
        print("❌ Radifi ba in ID peyda nashod!")
        cursor.close()
        conn.close()
        return
    
    print(f"\n  Radif morede nazar: {row}")
    confirm = input("  Az hazf etminan dari? (yes/no): ").lower().strip()
    
    if confirm != 'yes':
        print("❌ Hazf laghv shod.")
        cursor.close()
        conn.close()
        return
    
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE {id_column} = %s", (record_id,))
        conn.commit()
        print(f"✅ Hazf shod! {cursor.rowcount} radif hazf gardid.")
    except Error as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()






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
    print("2. settings:")
    print("0. khoroj az barname:")
    print("="*40)

def settings_menu():
    print("\n" + "-" * 45)
    print("     ⚙️  TANZIMAT")
    print("-" * 45)
    print("  📥 INSERT (Vared kardan):")
    print("     11. Member jadid")
    print("     12. Morabi jadid")
    print("     13. Class jadid")
    print("  ✏️ UPDATE (Virayesh):")
    print("     21. Virayesh Member")
    print("     22. Virayesh Morabi")
    print("     23. Virayesh Class")
    print("  🗑️ DELETE (Hazf):")
    print("     31. Hazf Member")
    print("     32. Hazf Morabi")
    print("     33. Hazf Class")
    print("  0. ⬅️  Bazgasht be menu asli")
    print("-" * 45)





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
 

# def settings():
#     print('\n 1.baraye vred krdn moshakhasat member jadid :')
#     print('\n 2.baraye vred krdn moshakhasat morabi jadid :')
#     print('\n 3.baraye vred krdn moshakhasat class jadid :')
#     print('\n 20.baraye vred krdn moshakhasat classregestration jadid :')
#     print('\n 4.baraye vred krdn moshakhasat membership jadid :')
#     print('\n 5.baraye vred krdn moshakhasat payment jadid :')
#     print('\n 6.baraye vred krdn moshakhasat food jadid :')
#     print('\n 7.baraye vred krdn moshakhasat fooddiet jadid :')
#     print('\n 8.baraye vred krdn moshakhasat dietprogram jadid :')
#     print('\n 9.baraye vred krdn moshakhasat exrecise jadid :')
#     print('\n 13.baraye vred krdn moshakhasat exerciseprogram jadid :')
#     print('\n 12.baraye vred krdn moshakhasat workoutprogram jadid :')
#     print('\n 10.baraye vred krdn moshakhasat locker jadid :')
#     print('\n 11.baraye vred krdn moshakhasat memberlocker jadid :')
#     print('\n 14.baraye vred krdn moshakhasat equipmtent jadid :')
#     print('\n 15.baraye vred krdn moshakhasat equipmtentmaintance jadid :')
#     print('\n 16.baraye vred krdn moshakhasat invoice jadid :')
#     print('\n 17.baraye vred krdn moshakhasat attendance jadid :')
#     print("\n 0. Bazgasht be menu asli:")

def show_member_details():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    member_id=input("ID member ra vared kon:")
    cursor.execute("select * from member where id=%s",(member_id,))
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
    cursor.execute("""
    SELECT p.* 
    FROM member m 
    JOIN membership ms ON m.id = ms.member_id
    JOIN payment p ON p.membership_id = ms.id
    WHERE m.id = %s
    """, (member_id,))   
    rows=cursor.fetchall()
    total=sum( r['amount'] for r in rows) if rows else 0
    print(f" tedade pardakht:{len(rows)} | majmo:{total}")
    cursor.close()
    con.close()

def show_coach_students():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    sql="""
            select c.f_name,c.l_name,cl.className as class_name,count(cr.member_id)as student_count
            from coach c
            left join class cl on cl.coach_id=c.id
            left join classregistration cr on cr.class_id=cl.id
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
    cursor.execute("""  SELECT m.Fname, m.Lname, e.exerciseName AS exercise_name, ep.reps AS tedade_harakat
                        FROM member m
                        JOIN workoutprogram wp ON m.id = wp.member_id
                        JOIN programexercise ep ON wp.id = ep.program_id
                        JOIN exercise e ON ep.exercise_id = e.id
                        where wp.member_id=%s""",(member_id,))
    rows=cursor.fetchall()
    if rows:
        print(f"barname varzeshi :  {rows[0]['Fname']} {rows[0]['Lname']}")
        for row in rows:
            print(f"   {row['exercise_name']} |tekrar: {row['tedade_harakat']}")
    else:
        print("barname varzeshi payda nashod!")
    cursor.close()
    con.close()


def show_diet_program():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    member_id=input('ID member ra vared konid:')
    cursor.execute("""
                        SELECT f.foodName, dp.goal, f.Calories
                        FROM dietprogram dp
                        JOIN dietfood df ON dp.id = df.diet_id
                        JOIN food f ON df.food_id = f.id
                        WHERE dp.member_id = %s """ ,(member_id,))
    for row in cursor.fetchall():
        print(f"  {row['foodName']} | hadaf:{row['goal']} | cal:{row['Calories']}")

    cursor.close()
    con.close()

def show_member_plan():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    member_id=input("ID member morede nazar ra vared konid:")
    cursor.execute("""select m.Fname,m.Lname,mp.plan_name
                      from member m join membership ms  on m.id=ms.member_id
                      join membership_plan mp on mp.id=ms.plan_id
                      where m.id=%s""",(member_id,))
    rows=cursor.fetchall()
    if rows:
        print(f" plan member morede nazare :{rows[0]['Fname']} {rows[0]['Lname']}")
        for row in rows:
            print(f"{row['plan_name']}")
    else:
        print("member plan nadard!")  

    cursor.close()
    con.close()          



def show_free_lockers():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    cursor.execute(""" select * from locker l
                        where l.id not in (select locker_id from memberlocker where enddate> now())""")
    for row in cursor.fetchall():
        print(f" locker  ///{row['id']}-number:{row.get('lockernumber','N/A')} ")
    cursor.close()
    con.close()   



def show_employees():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    cursor.execute("select * from employee") 
    for row in cursor.fetchall():
        print(f" {row.get('F_name','')}  {row.get('L_name','')} | post:{row.get('Position','N/A')}")           
    cursor.close()
    con.close()

def insert_member():
    print("\n--- ➕ Member Jadid ---")
    fname = input("  Name: ").strip()
    lname = input("  Famil: ").strip()
    phone = input("  Telefon: ").strip()
    email = input("  Email: ").strip()
    do_insert('member', ['Fname', 'Lname', 'phone', 'email'], (fname, lname, phone, email))


def insert_coach():
    print("\n--- ➕ Morabi Jadid ---")
    cid = int(input("  ID morabi: "))
    fname = input("  Name: ").strip()
    lname = input("  Famil: ").strip()
    spec = input("  Takhasos: ").strip()
    salary = int(input("  Hoghogh: "))
    sdate = input("  Tarikh shoroo (YYYY-MM-DD): ").strip()
    hdate = input("  Tarikh estekhdam (YYYY-MM-DD): ").strip()
    do_insert('coach', ['id', 'f_name', 'l_name', 'speciality', 'salary', 'start_date', 'hire_date'],
              (cid, fname, lname, spec, salary, sdate, hdate))


def insert_class():
    print("\n--- ➕ Class Jadid ---")
    className = input("  Name class: ").strip()
    coach_id = int(input("  ID morabi: "))
    schedule = input("  Zaman class: ").strip()
    capacity = int(input("  Zarfiat: "))
    do_insert('class', ['className', 'coach_id', 'schedule', 'capacity'], (className, coach_id, schedule, capacity))


def update_member():
    print("\n--- ✏️ Virayesh Member ---")
    mid = int(input("  ID member: "))
    print("  Meghdar jadid (Enter bezar agar nemikhahi taghir kone):")
    d = {}
    if (v := input("    Name: ").strip()):     d['Fname'] = v
    if (v := input("    Famil: ").strip()):    d['Lname'] = v
    if (v := input("    Telefon: ").strip()):  d['phone'] = v
    if (v := input("    Email: ").strip()):    d['email'] = v
    do_update('member', 'id', mid, d)


def update_coach():
    print("\n--- ✏️ Virayesh Morabi ---")
    cid = int(input("  ID morabi: "))
    print("  Meghdar jadid (Enter bezar agar nemikhahi taghir kone):")
    d = {}
    if (v := input("    Name: ").strip()):       d['f_name'] = v
    if (v := input("    Famil: ").strip()):      d['l_name'] = v
    if (v := input("    Takhasos: ").strip()):   d['speciality'] = v
    if (v := input("    Hoghogh: ").strip()):    d['salary'] = int(v)
    do_update('coach', 'id', cid, d)


def update_class():
    print("\n--- ✏️ Virayesh Class ---")
    clid = int(input("  ID class: "))
    print("  Meghdar jadid (Enter bezar agar nemikhahi taghir kone):")
    d = {}
    if (v := input("    Name class: ").strip()):  d['className'] = v
    if (v := input("    Zaman: ").strip()):       d['schedule'] = v
    if (v := input("    ID morabi: ").strip()):   d['coach_id'] = int(v)
    do_update('class', 'id', clid, d)



def delete_member():
    mid = int(input("\n  ID member baraye hazf: "))
    do_delete('member', 'id', mid)


def delete_coach():
    cid = int(input("\n  ID morabi baraye hazf: "))
    do_delete('coach', 'id', cid)


def delete_class():
    clid = int(input("\n  ID class baraye hazf: "))
    do_delete('class', 'id', clid)

REPORT_HANDLERS = {
    1: show_member_details,
    2: show_coach_with_class,
    3: show_member_plan,
    4: show_payment_status,
    5: show_coach_students,
    6: show_diet_program,
    7: show_workout_program,
    8: show_free_lockers,
    9: show_employees
}

SETTINGS_HANDLERS = {
    # INSERT
    11: insert_member,
    12: insert_coach,
    13: insert_class,
    # UPDATE
    21: update_member,
    22: update_coach,
    23: update_class,
    # DELETE
    31: delete_member,
    32: delete_coach,
    33: delete_class,
}


def report_loop():
    while True:
        report_menu()
        try:
            choice = int(input("  Entekhab: "))
        except ValueError:
            print("  ❌ Lotfan adad vared kon!")
            continue
        
        if choice == 0:
            break
        
        handler = REPORT_HANDLERS.get(choice)
        if handler:
            handler()
        else:
            print("  ❌ Gozine eshtebah!")


def settings_loop():
    while True:
        settings_menu()
        try:
            choice = int(input("  Entekhab: "))
        except ValueError:
            print("  ❌ Lotfan adad vared kon!")
            continue
        
        if choice == 0:
            break
        
        handler = SETTINGS_HANDLERS.get(choice)
        if handler:
            handler()
        else:
            print("  ❌ Gozine eshtebah!")


def main():
    while True:
        main_menu()
        try:
            choice = int(input("  Entekhab: "))
        except ValueError:
            print("  ❌ Lotfan adad vared kon!")
            continue
        
        if choice == 0:
            print("  👋 Khodahafez!")
            break
        elif choice == 1:
            report_loop()
        elif choice == 2:
            settings_loop()
        else:
            print("  ❌ Gozine eshtebah!")


if __name__ == "__main__":
    main()