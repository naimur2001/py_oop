# Hospital Management System By Python
# from HMS.models.doctor import doctor
# from HMS.models.patient import patient
# from HMS.services.hospital import hospital

from services.hospital import Hospital

# Create hospital system
hospital = Hospital()


def show_menu():
    print("\n===== Hospital Management Menu =====")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Show Doctors")
    print("4. Show Patients")
    print("5. Exit")
    print("====================================")

# Loop forever until user exits
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Doctor Name: ")
        specialization = input("Specialization: ")
        doctor = {"name": name, "specialization": specialization}
        hospital.add_doctor(doctor)
        print("✅ Doctor added successfully!")

    elif choice == "2":
        name = input("Patient Name: ")
        age = input("Age: ")
        phone=input("Phone: ")
        symptoms = input("Symptoms: ")
        patient = {"name": name, "age": age, "phone":phone, "symptoms": symptoms}
        hospital.add_patient(patient)
        print("✅ Patient added successfully!")

    elif choice == "3":
        print("\n📋 All Doctors:")
        for doc in hospital.doctors:
            print(f"👨‍⚕️ Name: {doc['name']}, Specialization: {doc['specialization']}")

    elif choice == "4":
        print("\n📋 All Patients:")
        for pat in hospital.patients:
            print(f"🧑 Name: {pat['name']}, Age: {pat['age']}, Phone: {pat.get('phone','N/A')}, Symptoms: {pat['symptoms']}")

    elif choice == "5":
        print("👋 Exiting the system. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please try again.")
