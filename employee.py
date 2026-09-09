from database import connection
def add_employee():
    try:
        employee_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID. Please enter numbers only.")
        return
    first_name=input("Enter First Name: ")
    last_name=input("Enter Last Name: ")
    email=input("Enter Email: ")
    try:
        phone=int(input("Enter Phone: "))
    except ValueError:
        print("Invalid phone number. Pleasae enter numbers only.")    
        return
    department=input("Enter Department: ")
    designation=input("Enter Designation: ")
    try:
        salary=float(input("Enter Salary: "))
        if salary<0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid salary. Please enter a number.")    
        return

    cursor=connection.cursor()
    query=""" INSERT INTO project_employees
    (employee_id,first_name,last_name,email,phone,department,designation,salary)
    VALUES(:1,:2,:3,:4,:5,:6,:7,:8)"""
    try:
        cursor.execute(query,(employee_id,first_name,last_name,email,phone,department,designation,salary))
        connection.commit()
        print("Employee added successfully!")
    except Exception as e:
        connection.rollback()
        print("Unable to add employee.")    
        print("Error:",e)
    finally:
        cursor.close()    
def view_employees():
    cursor=connection.cursor()
    query=""" SELECT employee_id,first_name,last_name,email,phone,department,designation,salary FROM project_employees ORDER BY employee_id"""
    cursor.execute(query)
    employees=cursor.fetchall()
    if not employees:
        print("No employees found")
    else:
        print("\n=====Employee Details===")    
        for employee in employees:
            print("Employee ID :", employee[0])
            print("Name        :", employee[1], employee[2])
            print("Email       :", employee[3])
            print("Phone       :", employee[4])
            print("Department  :", employee[5])
            print("Designation :", employee[6])
            print("Salary      :", employee[7])
            print("-----------------------------")
    cursor.close()

def search_employee():
    try:
        employee_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID. Please enter numbers only.")
        return
    cursor=connection.cursor()
    query=""" SELECT employee_id,first_name,last_name,email,phone,department,designation,salary 
    FROM project_employees WHERE employee_id=:1"""
    
    try:
        cursor.execute(query, (employee_id,))

        employee = cursor.fetchone()

        if employee:
            print("\n===== Employee Found =====")
            print("Employee ID :", employee[0])
            print("Name        :", employee[1], employee[2])
            print("Email       :", employee[3])
            print("Phone       :", employee[4])
            print("Department  :", employee[5])
            print("Designation :", employee[6])
            print("Salary      :", employee[7])
        else:
            print("Employee not found.")

    except Exception as e:
        print("Unable to search employee.")
        print("Error:", e)

    finally:
        cursor.close()
def update_employee():
    try:
        employee_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID. Please enter numbers only.")
        return  
    new_department=input("Enter New Department: ")
    new_designation=input("Enter New Designation: ")
    try:
        new_salary=float(input("Enter New Salary: "))
        if new_salary<=0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid salary.Please enter a number.")    
        return
    cursor=connection.cursor()
    query=""" UPDATE project_employees SET department=:1,designation=:2,salary=:3 
    WHERE employee_id=:4"""
    try:
        cursor.execute(query,(new_department,new_designation,new_salary,employee_id))
        connection.commit()
        if cursor.rowcount>0:
            print("Employee updated successfully!")
        else:
            print("Employee not found") 
    except Exception as e:
        connection.rollback()
        print("Unable to update employee.")           
        print("Error:",e)
    finally:
        cursor.close()
def delete_employee():
    try:
        employee_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid Employee ID. Please enter numbers only.")
        return    
    cursor=connection.cursor()
    query=""" DELETE FROM project_employees
    WHERE employee_id=:1"""
    try:
        cursor.execute(query, (employee_id,))

        if cursor.rowcount > 0:
            connection.commit()
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    except Exception as e:
        connection.rollback()
        print("Unable to delete employee.")
        print("Error:", e)

    finally:
        cursor.close()