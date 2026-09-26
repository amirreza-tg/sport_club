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

def main_menu():
    print("   gym - menue Asli")
    print("1. Gozaresh giri didn eteleaat:")
    print("2. settings:")
    print("0. khoroj az barname:")
    print("="*40)

def settings_menu():
    print("\n" + "-" * 45)
    print("      TANZIMAT")
    print("-" * 45)
    print("INSERT (Vared kardan):")
    print(" 11. Member jadid")
    print(" 12. Morabi jadid")
    print("13. Class jadid")
    print("14. classregistration jadid")
    print("15. payment jadid")
    print("UPDATE (Virayesh):")
    print("21. Virayesh Member")
    print(" 22. Virayesh Morabi")
    print("23. Virayesh Class")
    print("DELETE (Hazf):")
    print("31. Hazf Member")
    print("32. Hazf Morabi")
    print("33. Hazf Class")
    print("  0.  Bazgasht be menu asli")

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
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    try:
        while True:

            mid=input("lotfan id mored nazar ra vared kon:")
            f=input("lotfan Fname member ra vared konid:")
            l=input('lotfan Lname member ra vared konid:')
            g=input('lotfan gender memmber ra vared konid:')
            p=input('lotfan phone member ra vared kon :')
            sd=input('lotfan startdate member ra vared kon (Enter=khali):').strip() or None
            st=input('lotfan status member ra vared kon (Enter=khali):').strip() or None

            cursor.execute(
                "insert into member (id, Fname, Lname, gender, phone, startdate, status) values (%s,%s,%s,%s,%s,%s,%s)",
                (mid, f, l, g, p, sd, st),
            )
            con.commit()
            ch=input('enter more records?(y/n)')
            if ch in ("N", "n"):
                break
    finally:            
        cursor.close()
        con.close()

def insert_class():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    try:
        while True:

            cid=input("lotfan id class mored nazar ra vared kon:")
            chid=input("lotfan id coach ra vared konid:")
            cn=input('lotfan name class ra vared konid:')
            dw=input('lotfan tedad roz haye class ro dar hafte vared konid:(tedad-adad)')
            cp=int(input('lotfan zarfiyt class ra vared konid:(addad)'))
            sd=input('lotfan startdate class ra vared kon :')
            ed=input('lotfan enddate class ra vared kon :')
            pr=input('lotfan zarfiyt class ra vared kon :')
            cursor.execute(
                "insert into class (id, coach_id, className, capacity, dayofweek, starttime, endtime, price) values (%s,%s,%s,%s,%s,%s,%s,%s)",
                (cid, chid, cn, cp, dw, sd, ed, pr),
            )
            con.commit()
            ch=input('enter more records?(y/n)')
            if ch in ("N", "n"):
                break
    finally:            
        cursor.close()
        con.close()

def insert_class_registration():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    try:
        while True:
            crid=input("lotfan id classregistration mored nazar ra vared kon:")
            mid=input('lotfan id member mored nazar ra vared kon:')
            clid=input('lotfan id class mored nazar ra vared kon:')
            cursor.execute(
                "insert into classregistration (id, member_id, class_id) values (%s,%s,%s)",
                (crid, mid, clid),
            )
            con.commit()
            ch=input('enter more records?(y/n)')
            if ch in ("N", "n"):
                break
    finally:
        cursor.close()
        con.close()            

def inssert_coach():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    try:
        while True:
            chid=input("lotfan id morabi mored nazar ra vared kon:")
            fn=input('lotfan name morabi mored nazar ra vared kon:')
            ln=input('lotfan last name morabi mored nazar ra vared kon:')
            st=input('lotfan tarikh shoro be kaar morabi jadid ro vared kon:')
            sp=input('tkhsose morabi:')
            sl=int(input('hogoge morabi:(add vared kon)'))
            hd=input('tarikh estekhdame morabi:')

            cursor.execute(
                "insert into coach (id, f_name, l_name, start_date, speciality, salary, hire_date) values (%s,%s,%s,%s,%s,%s,%s)",
                (chid, fn, ln, st, sp, sl, hd),
            )
            con.commit()
            ch=input('enter more records?(y/n)')
            if ch in ("N", "n"):
                break
    finally:
        cursor.close()
        con.close()            

def inssert_paymant():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    try:
        while True:
            pid=input("lotfan id payment ra vared kon:")
            pm=input('lotfan membership_id member ra vared kon:')
            pa=int(input('lotfan amount payment ra vared kon:'))
            pd=input('lotfan tarikh payment jadid ro vared kon:')
            pt=input('payment methode:')
            st=input('status payment:')
            

            cursor.execute(
                "insert into payment (id, membership_id, amount, paymentdate, paymentmethode, status) values (%s,%s,%s,%s,%s,%s)",
                (pid, pm, pa, pd, pt, st),
            )
            con.commit()
            ch=input('enter more records?(y/n)')
            if ch in ("N", "n"):
                break
    finally:
        cursor.close()
        con.close()  


def delete_member():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    try:
        did=input('please enter the id of member you want to delete it!:').strip()
        cursor.execute("delete from member where id=%s", (did,))
        con.commit()
        if cursor.rowcount:
            print('your member deleted!')
        else:
            print('member peyda nashod!')
    finally:
        cursor.close()
        con.close()

def delete_coach():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    did=input('please enter the id of coach you want to delete it!:')
    cursor.execute(" delete from coach where id=%s",(did,))
    con.commit()
    print('your coach  deleted!')
    con.close()    

def delet_class():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    did=input('please enter the id of class you want to delete it!:')
    cursor.execute(" delete from class where id=%s",(did,))
    con.commit()
    print('your class deleted!')
    con.close()    

def update_member():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    uid=input('please enter the id of member you want to update it!:')
    print("if you dont want to change pls select eneter")
    fn=input("pls enter first name you want ").strip()
    ln=input("pls enter last name you want to").strip()
    sd=input("pls enter the start date you want to change").strip()
    phone=input("pls enter the phone you want to change ").strip()
    st=input("pls enter the status to change ").strip()
    print(phone)
    try:

        if fn:
            cursor.execute("update member set Fname=%s  where id=%s",(fn,uid))
            print("member first name updated successfullly!")

        if ln:
            cursor.execute("update member set Lname=%s  where id=%s",(ln,uid))
            print("member last name updated successfullly!")

        if sd:
            cursor.execute("update member set startdate=%s  where id=%s",(sd,uid))
            print("member start date updated successfullly!")

        if phone:
            cursor.execute("update member set phone=%s  where id=%s",(phone,uid))
            print("member phone updated successfullly!")

        if st:
            cursor.execute("update member set status=%s  where id=%s",(st,uid))
            print("member status updated successfullly!")
    finally:
        con.commit()
        print('your member updated!')
        con.close()    



def update_class():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    cid=input('please enter the id of class you want to update it!:')
    print("if you dont want to change pls select eneter")
    chid=input("pls enter the id of claas coach to change ").strip()
    cn=input("pls enter class name you want to chang to it").strip()
    cp=int(input("pls enter the number of class capacitance  to change"))
    dyw=int(input("pls enter the number of days in week class  to change "))
    st=input("pls enter the start time to change ").strip()
    ent=input("pls enter the end time to change ").strip()
    price=int(input("pls enter class price to change"))
    try:

        if chid:
            cursor.execute("update class set coach_id=%s  where id=%s",(chid,cid))
            print("coach_id updated successfullly!")

            
        if cn:
            cursor.execute("update class set className=%s  where id=%s",(cn,cid))
            print("class name updated successfullly!")

        if cp:
            cursor.execute("update class set capacity=%s  where id=%s",(cp,cid))
            print("class capacity updated successfullly!")

        if dyw:
            cursor.execute("update class set dayofWeek=%s  where id=%s",(dyw,cid))
            print("class days updated successfullly!")

        if st:
            cursor.execute("update class set starttime=%s  where id=%s",(st,cid))
            print("class start time updated successfullly!")
        if ent:
            cursor.execute("update class set endtime=%s  where id=%s",(ent,cid))
            print("class end time updated successfullly!")
        if price:
            cursor.execute("update class set price=%s  where id=%s",(price,cid))
            print("class price updated successfullly!")            
    finally:
        con.commit()
        print('your class updated!')
        con.close()  

def update_coach():
    con=get_connection()
    cursor=con.cursor(dictionary=True)
    hid=input('please enter the id of coach you want to update it!:')
    print("if you dont want to change pls select eneter")
    fh=input("pls enter the first name if coach to change ").strip()
    lh=input("pls enter the last name coach to chang to it").strip()
    scp=input("pls enter the speciality   to change").strip()
    st=input("pls enter the start date to change ").strip()
    ht=input("pls enter the hire date to change ").strip()
    salary=int(input("pls enter class price to change"))
    try:

        if fh:
            cursor.execute("update coach set f_name=%s  where id=%s",(hid,fh))
            print("coach first name updated successfullly!")

            
        if lh:
            cursor.execute("update coach set l_name=%s  where id=%s",(lh,hid))
            print("class name updated successfullly!")

        if scp:
            cursor.execute("update coach set speciality=%s  where id=%s",(scp,hid))
            print("coach speciality updated successfullly!")

        if st:
            cursor.execute("update coach set start_date=%s  where id=%s",(st,hid))
            print("class start time updated successfullly!")
        if ht:
            cursor.execute("update coach set hire_date=%s  where id=%s",(ht,hid))
            print("class hire date updated successfullly!")
        if salary:
            cursor.execute("update coach set salary=%s  where id=%s",(salary,hid))
            print("coach salary updated successfullly!")            
    finally:
        con.commit()
        print('your coach updated!')
        con.close()      
report={
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
settings={
    11:insert_member,
    12:inssert_coach,
    13:insert_class,
    14:insert_class_registration,
    15:inssert_paymant,

    21:update_member,
    22:update_coach,
    23:update_class,

    31:delete_member,
    32:delete_coach,
    33:delet_class
}


def report_loop():
    while True:
        report_menu()
        try:
            a=int(input("baraye didne gozareshe delkhah addade menu ro vared konid:"))
        except ValueError:
            print("lotfan add vared kon!")
            continue    

        if a==0:
            break


        handeler=report.get(a)
        if handeler:
            handeler()
        else:
            print("gozine eshtebah vared shod!")

def settings_loop():
    settings_menu()
    while True:

        try:
            b=int(input(" baraye dastresresi be baxsaye menu addad ro vared konid:"))
        except ValueError:
            print("lotfan addad vared kon!")
            continue    

        if b==0:
            break
        handler =settings.get(b)
        if handler:
            handler()
        else:
            print("gozine eshtebah vared shod!")


def main():
    main_menu()
    while True:
        try:
            b=int(input(" baraye dastresresi be baxsaye menu addad ro vared konid:"))
        except ValueError:
            print("lotfan addad vared kon!")
            continue
        if b==0:
            print("BYE!")
            break 
        elif b==1:
            report_loop()
        elif b==2:
            settings_loop()
        else:
            print("Gozine eshteah!")    

if __name__=="__main__":
    main()