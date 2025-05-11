# class Car:
#   color="black"
#   @staticmethod
#   def start ():
#     print("Car started")  
  
#   @staticmethod
#   def stop ():
#     print("Car stopped")


# class Toyoyota(Car):
#   def __init__(self,name):
#     self.name=name
  

# # car1=Toyoyota("Camry")
# # car2=Toyoyota("Prius")
# # car1.start()
# # car1.stop()

# # print(car1.name)
# # print(car1.color )
# # print(car2.name)

# class Fortunarer(Toyoyota):
#   def __init__(self,type):
#     self.type=type

# car1=Fortunarer("disel")
# print(car1.type)
# car1.start()



class Student: 
  def __init__(self,p,c,m):
    self.p=p
    self.c=c
    self.m=m
    # self.percentage =str((p+c+m)/3)+"%"

  # def cal_percentage(self):
  #   return f"{(self.p+self.c+self.m)/3:.2f}%"
  

  @property
  def cal_percentage(self):
    return f"{(self.p+self.c+self.m)/3:.2f}%"

stu1=Student(80,70,90)
print(stu1.cal_percentage)

stu1.p=90
print(stu1.p)
print(stu1.cal_percentage)
    