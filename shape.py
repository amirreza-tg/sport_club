class Shape:
    def __init__(self, name, color, length, width=0, height=0):
        self.name = name
        self.color = color
        self.length = length
        self.width = width
        self.height = height
    
    def perimeter(self):
        if self.name.lower() == "rectangle":
            return 2 * (self.length + self.width)

        elif self.name.lower() == "square":
            return 4 * self.length

        else:
            return "محیط برای این شکل تعریف نشده است"
    
    def area(self):
        if self.name.lower() == "rectangle":
            return self.length * self.width

        elif self.name.lower() == "square":
            return self.length ** 2

        else:
            return "مساحت برای این شکل تعریف نشده است"
    
    # def show_info(self):
    #     print(f"نام شکل: {self.name}")
    #     print(f"رنگ: {self.color}")
    #     print(f"محیط: {self.perimeter()}")
    #     print(f"مساحت: {self.area()}")

name = input(" noe shekl (rectangle/square): ")
color = input("رنگ شکل: ")

if name.lower() == "rectangle":
    length = float(input("طول: "))
    width = float(input("عرض: "))
    shape = Shape(name, color, length, width)

elif name.lower() == "square":
    length = float(input("اندازه ضلع: "))
    shape = Shape(name, color, length)

else:
    print("شکل پشتیبانی نمی‌شود.")
    exit()

shape.show_info()