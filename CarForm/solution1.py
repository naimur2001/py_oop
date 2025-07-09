class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  
  def full_name(self):
    return f"{self.brand} {self.model}"
  
class ElectricCar(Car):
  def __init__(self, brand,model,batter_size): #ineritance
    super().__init__(brand,model)
    self.battery_size=batter_size


my_tesla=ElectricCar("Tesla","Model_S","86kwh")
print(my_tesla.model)
print(my_tesla.full_name(),my_tesla.battery_size)

# my_Car1=Car("Toyota","Corolla")
# my_Car2=Car("Toyota","Safari")
# print(my_Car1.full_name())
