# class Student:
#     name="naimur rahman"

#     # object is isinstance of class 

# s1 = Student()
# print(s1.name)


# class Car:
#     def __init__(self,fullname):
#         self.brand=fullname
#         print("adding brand")
#     color="blue"

#     info={
#         "cname":"ppp",
#         "cc":700
#     }

    
    

# c1=Car("BMW")
# print(c1.brand)
# print(c1.color)

# c2=Car("Tesla")
# print(c2.brand)

# c3=Car.info
# print(c3)


class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Taka : ",amount,"was debited")
        print("total balance", self.check_balance())

    def credit(self, amount):    
        self.balance += amount
        print("Taka : ",amount,"was credited")
        print("total balance", self.check_balance())   


    def check_balance(self):
        return self.balance




a1 = Account(10000,2564645)
print(a1.balance)   
print(a1.account_no)
print(a1.credit(5000))