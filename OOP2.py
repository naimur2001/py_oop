class Car:
  color="black"
  @staticmethod
  def start ():
    print("Car started")  
  
  @staticmethod
  def stop ():
    print("Car stopped")


class Toyoyota(Car):
  def __init__(self,name):
    self.name=name
  

# car1=Toyoyota("Camry")
# car2=Toyoyota("Prius")
# car1.start()
# car1.stop()

# print(car1.name)
# print(car1.color )
# print(car2.name)

class Fortunarer(Toyoyota):
  def __init__(self,type):
    self.type=type

car1=Fortunarer("disel")
print(car1.type)
car1.start()



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
    

class Complex:
  def __init__(self, real,img):
    self.real=real
    self.img=img
  
  def showNumber(self):
    print(self.real,"i +",self.img,"j")
  
  def __add__ (num1,num2):
    newNum1=num1.real+num2.real
    newNum2=num1.img+num2.img
    return Complex(newNum1,newNum2)
  def __sub__ (num1,num2):
    newNum1=num1.real-num2.real
    newNum2=num1.img-num2.img
    return Complex(newNum1,newNum2)


num1=Complex(2,3)
num1.showNumber()

num2=Complex(4,5)
num2.showNumber()

# num3=num1.add(num2)
num3=num1+num2
num3.showNumber()
num3=num1-num2
num3.showNumber()


class Order:
  def __init__(self,item,price):
    self.item=item
    self.price=price


  def __gt__(self,order2):
    return self.price>order2.price

order1=Order("Shirt",500)
print(order1.item)
print(order1.price)
order2=Order("Pant",1000)
print(order2.item)
print(order2.price)

print(order1<order2)