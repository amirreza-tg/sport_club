class car:

    def __init__(self,name,product_year):
        
        self.name = name
        self.product_year = product_year

    def print_my_car_name(self):
        print(f'yuor car is:{self.name} and created in {self.product_year} year')

my_car = car('quick',1401)

my_car.print_my_car_name()

my_car = car('Tiba',1402)

my_car.print_my_car_name()