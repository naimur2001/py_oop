# hospital.py - Hospital service module

import os
from services.file_manager import save_data, load_data

# Define the base directory (HMS/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class Hospital:
    def __init__(self):
        # Define file paths for storing doctor and patient data
        self.doctors_path = os.path.join(BASE_DIR, 'models', 'data', 'doctors.json')
        self.patients_path = os.path.join(BASE_DIR, 'models', 'data', 'patients.json')

        # Load existing data or initialize empty lists
        self.doctors = load_data(self.doctors_path)
        self.patients = load_data(self.patients_path)

    def add_doctor(self, doctor):
        """
        Add a doctor to the system and save to file.
        :param doctor: dict with doctor information (e.g., {'name': ..., 'specialization': ...})
        """
        self.doctors.append(doctor)
        save_data(self.doctors, self.doctors_path)

    def add_patient(self, patient):
        """
        Add a patient to the system and save to file.
        :param patient: dict with patient information (e.g., {'name': ..., 'disease': ...})
        """
        self.patients.append(patient)
        save_data(self.patients, self.patients_path)

    def show_doctors(self):
        """Print all registered doctors."""
        for doctor in self.doctors:
            print(f"{doctor['name']} - {doctor['specialization']}")

    def show_patients(self):
        """Print all registered patients."""
        for patient in self.patients:
            print(f"{patient['name']} - {patient['disease']}")
