def get_number():
    number = int(input("عدد وارد کن: "))
    return number

while True:
    try:
        number = get_number()
        print(10 / number)

    except ValueError:
        print("ورودی باید عدد باشد")

    except ZeroDivisionError:
        print("تقسیم بر صفر مجاز نیست")