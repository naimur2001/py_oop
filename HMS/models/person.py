# person model 
from  abc import ABC, abstractmethod

class Person(ABC):
  def __init__(self, name, age,phone,address):
    self.name = name
    self.age = age
    self.phone = phone
    self.address = address

  @abstractmethod
  def get_details(self):
    print(self.name, self.age, self.phone, self.address)

