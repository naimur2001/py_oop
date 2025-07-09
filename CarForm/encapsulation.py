class Car:
  total_car=0
  def __init__(self,brand,model):
    self.__brand=brand
    self.__model=model
    Car.total_car += 1
    # self.total_car += 1


  def get_brand(self):
    return self.__brand + " @_@"
  
  def set_brand(self,brand):
    self.__brand=brand
  
  def get_model(self):
    return self.__model +  " @_@"
  
  def set_model(self,model):
    self.__model=model

  def fuel_type(self):
    return "Patrol Or Diesel"
     
  def full_name(self):
    return f"{self.get_brand()} {self.get_model()}"
  
  @staticmethod
  def general_description():
    return "Cars are means of transport"
  
class ElectricCar(Car):
  def __init__(self, brand,model,batter_size): #ineritance
    super().__init__(brand,model)
    self.battery_size=batter_size
  def fuel_type(self):
    return "Electric Charge"



my_tesla=ElectricCar("Tesla","Model_S","86kwh")
my_tesla.set_model("Model_M")
my_tesla.set_model("SPACEX")
print(my_tesla.full_name(),my_tesla.battery_size)
print(my_tesla.fuel_type())

safari=Car("BMW", "B8")
print(safari.full_name())
print(safari.fuel_type())

benz= Car("Mercedez","7u")
# benz2= Car("Mercedez","7u")
print(benz.full_name())
print(benz.fuel_type())
print(Car.total_car)
print(Car.general_description())
# Car("Walton","Vangari")

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

class Battery:
  def battery_info(self):
    return "This is Battery"

class Engine:
  def engine_info(self):
    return "This is Engine"
  

class Electric_Vehicle(Battery,Engine,Car):
  def EV():
    return "This is time changing"

my_new_tesla=Electric_Vehicle("T E S L A", "M O D E L EM")
print(my_new_tesla.full_name(), my_new_tesla.engine_info()
      , my_new_tesla.battery_info())