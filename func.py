# def fun1():
#   print("fun1")
#   return
class fun2:

    # def __init__(self, name, age):
    #  self.name = name
    #  self.age = age
    # def __init__(self, phone, address):
    #   self.phone =phone
    #   self.address=address
    def check_list(self,arr):
       
       for i in arr:
        if type(i)==list:
             arr.append(self.check_list(i))
        else:
           arr.append(i)
       return arr

    def do_print(self,var:list[int]):
       arr=[]
       for i in var:
           if type(i)==list:
             arr.append(self.check_list(i))
           else:
             arr.append(i)
       return arr
              
 

f=fun2()
print(f.do_print([[1,2,3],[[4],5,[6]]]) )
print("shs")
print(f.do_print([1,2,[3,4],[6],[0,2,9],[3],5]))

    #  arr=[]
    #   for i in var:
    #        if isinstance(i,list):
    #          arr.extend(self.do_print(i))
    #        else:
    #          arr.append(i)

      
    #   return arr