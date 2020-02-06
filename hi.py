class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year)  + ' ' + self.make + ' ' + self.model
        return long_name.title()
my_new_car = Car('toyota', 'benz', 123)
print(my_new_car.get_descriptive_name()) 
