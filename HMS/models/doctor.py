# doctor model 
from models.person import Person

class Doctor(Person):
  def __init__(self, name, age,phone,address,speciality):
    super().__init__(name, age,phone,address)
    self.speciality = speciality

  def display_doc_info(self):
    print(self.name, self.age, self.phone, self.address, self.speciality)
