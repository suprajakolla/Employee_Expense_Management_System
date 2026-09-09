````markdown
# Employee Expense & Management System

A Python-based Employee Expense & Management System that allows users to manage employee information and track employee expenses using an Oracle database.

## Project Overview

The Employee Expense & Management System is a console-based application developed using Python and Oracle SQL.

The system provides employee management, expense management, expense status tracking, and expense reporting features.

## Technologies Used

- Python 3.14.7
- Oracle Database
- SQL
- Python `oracledb` package
- Python `python-dotenv` package
- VS Code

## Features

### Employee Management

- Add Employee
- View Employees
- Search Employee
- Update Employee
- Delete Employee

### Expense Management

- Add Expense
- View Expenses
- Search Expense
- Update Expense Status
- Delete Expense

### Expense Reports

- View Total Expenses
- View Employee-wise Expenses
- View Approved Expenses
- View Pending Expenses
- View Rejected Expenses

### Validation and Error Handling

- Employee ID validation
- Expense ID validation
- Phone number validation
- Salary validation
- Expense amount validation
- Expense date validation
- Employee existence validation
- Database exception handling
- Transaction rollback handling

## Database

The application uses Oracle Database to store employee and expense information.

### Employee Table

`PROJECT_EMPLOYEES`

Stores:

- Employee ID
- First Name
- Last Name
- Email
- Phone
- Department
- Designation
- Salary

### Expense Table

`EXPENSES`

Stores:

- Expense ID
- Employee ID
- Expense Type
- Amount
- Expense Date
- Description
- Status

The `EXPENSES` table uses a foreign key relationship with the `PROJECT_EMPLOYEES` table.

## Project Structure

```text
Employee_Expense_Management_System/
│
├── main.py
├── database.py
├── employee.py
├── expense.py
├── .env
├── .gitignore
└── README.md
````

## Application Flow

```text
Start Application
       ↓
Main Menu
       ↓
Employee Management
       ↓
Expense Management
       ↓
Expense Reports
       ↓
Exit
```

## Security

Database credentials are stored in a `.env` file instead of being directly written in the Python source code.

The `.env` file is excluded from GitHub using `.gitignore`.

## How to Run

### 1. Install Python

Install Python and verify the installation:

```bash
python --version
```

### 2. Install Required Packages

```bash
pip install oracledb
pip install python-dotenv
```

### 3. Configure Database Credentials

Create a `.env` file and add your local Oracle database configuration:

```text
DB_USER=your_username
DB_PASSWORD=your_password
DB_DSN=localhost:1521/orcl
```

Do not upload the `.env` file to GitHub.

### 4. Run the Application

```bash
python main.py
```

## Sample Main Menu

```text
=======================================================
        EMPLOYEE EXPENSE & MANAGEMENT SYSTEM
=======================================================

-------------------------------------------------------
                    MAIN MENU
-------------------------------------------------------
1.  Add Employee
2.  View Employees
3.  Search Employee
4.  Update Employee
5.  Delete Employee
6.  Add Expense
7.  View Expenses
8.  Search Expense
9.  Update Expense Status
10. Delete Expense
11. Expense Reports
12. Exit
-------------------------------------------------------
```

## Future Enhancements

* User authentication and login
* Admin and employee roles
* Monthly and yearly expense reports
* Export reports to Excel or CSV
* Graphical user interface
* Expense approval workflow
* Dashboard with expense statistics

## Author

Supraja Kolla

B.Tech – Computer Science and Engineering

GitHub: `https://github.com/suprajakolla`

```