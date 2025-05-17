# 🐍 Python OOP Learning Journey

Welcome to my Python OOP learning repository! This project showcases what I'm currently learning and have already learned in Python, especially focusing on **Object-Oriented Programming (OOP)**, **file handling**, and **error management**.

## 🚀 What I'm Learning

- ✅ **Python Basics**: Variables, functions, control flow, loops.
- ✅ **Object-Oriented Programming (OOP)**:
  - Classes and objects
  - Constructors (`__init__`)
  - Instance variables and methods
- ✅ **JSON File Handling**:
  - Reading and writing data using `json` module
  - Saving and loading structured data (list of dictionaries)
- ✅ **Modular Code**:
  - Creating reusable service modules like `file_manager.py` and `hospital.py`
- ✅ **Error Handling**:
  - Using `try-except` blocks
  - Printing exact error messages using `except Exception as e`

## 🏥 Project Overview: Hospital Management System

This is a simple Python project where I applied OOP concepts to simulate a hospital management system.

### Modules:
- `file_manager.py`: Handles JSON file read/write
- `hospital.py`: Manages doctor and patient records using OOP

### Sample Features:
- Add a new doctor or patient
- Display all doctors and patients
- Store all data in local JSON files for persistence

## 📁 Folder Structure

```
HMS/
│
├── models/
│   └── data/
│       ├── doctors.json
│       └── patients.json
│
├── services/
│   └── file_manager.py
│
└── hospital.py
```

## 🧠 What's Next

- Add search and delete functionality
- Build a simple CLI or UI
- Learn inheritance and encapsulation
- Explore using SQLite or PostgreSQL instead of JSON
