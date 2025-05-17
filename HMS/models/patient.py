# patient model 
from models.person import Person

class Patient(Person):
  def __init__(self, name, age,phone,address,disease,doctor):
    super().__init__(name, age,phone,address)
    self.disease = disease
    self.doctor = doctor
  

  def display_pat_info(self):
    print(self.name, self.age, self.phone, self.address, self.disease, self.doctor)