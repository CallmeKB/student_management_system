# Student Management System

A simple **Student Management System** built with **Python, OOP, and MySQL**.
This project allows users to manage student records through a command-line interface.

## Features

* Add new students
* View all students
* Search for students
* Update student information
* Delete students
* Store student data in MySQL
* Object-Oriented Programming structure
* Basic input validation and error handling

## Technologies Used

* **Python**
* **MySQL**
* **MySQL Connector/Python**
* **Object-Oriented Programming (OOP)**
* **Git & GitHub**

## Project Structure

```text
student_management_system/
│
├── main.py
├── student.py
├── database.py
├── .gitignore
├── requirements.txt
└── README.md
```

> The exact files may vary depending on the current version of the project.

## Database

The project uses **MySQL** to store student information.

Example student table:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
);
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/CallmeKB/student_management_system.git
```

### 2. Open the project

```bash
cd student_management_system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Make sure MySQL is installed and running.

Create the required database and configure the database connection in the project according to your local MySQL credentials.

**Do not upload your MySQL password or other credentials to GitHub.**

## Running the Project

After configuring the database, run:

```bash
python main.py
```

The program will display the available student management operations.

## Version

**Version 1.0**

This is an early version of the project created for learning and practicing:

* Python
* OOP
* MySQL
* CRUD operations
* Database connectivity
* Git and GitHub

## Future Improvements

Possible improvements for future versions:

* Add a graphical user interface using Tkinter
* Add login/authentication
* Improve input validation
* Add student sorting and filtering
* Add more detailed student information
* Improve project architecture
* Add automated tests
* Build a REST API

## Author

**Kaushal Bohara**

GitHub: [@CallmeKB](https://github.com/CallmeKB)
