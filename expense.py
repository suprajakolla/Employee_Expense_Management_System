from database import connection
from datetime import datetime
def add_expenses():
    try:
        expense_id = int(input("Enter Expense ID: "))
        employee_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid ID. Please enter numbers only.")
        return
    cursor=connection.cursor()
    cursor.execute(
        "SELECT employee_id FROM project_employees WHERE employee_id=:1",(employee_id,)
        
    )
    employee=cursor.fetchone()
    if not employee:
        print("Employee not found.Please enter a valid Employee ID.")
        cursor.close()
        return
    cursor.close()
    expense_type=input("Enter Expense Type: ")
    try:
        amount=float(input("Enter Amount:"))
        if amount<=0:
            print("Expense amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount,Please enter a number.")    
        return
    try:
        expense_date=input("Enter Expense Date(YYYY-MM-DD): ")
        datetime.strptime(expense_date,"%Y-%m-%d")
    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD format")   
        return 
    description=input("Enter Description: ")
    cursor=connection.cursor()
    query=""" INSERT INTO expenses (expense_id,employee_id,expense_type,amount,expense_date,description)
    VALUES(:1,:2,:3,:4, TO_DATE(:5,'YYYY-MM-DD'),:6)"""
    try:
        cursor.execute(query,(expense_id,employee_id,expense_type,amount,expense_date,description))
        connection.commit()
        print("Expenses added successfully!.")
    except Exception as e:
        connection.rollback()
        print("Unable to add expenses.")
        print("Error:",e)
    finally:
            cursor.close()
    
def view_expenses():
    cursor=connection.cursor()
    query=""" SELECT expense_id,employee_id,expense_type,amount,expense_date,description,status
    FROM expenses ORDER BY expense_id"""
    cursor.execute(query)
    expenses=cursor.fetchall()
    if not expenses:
        print("NO expenses found.")
    else:
        print("\n Expenses Details: ")    
        for expense in expenses:
            print("Expense ID   :", expense[0])
            print("Employee ID  :", expense[1])
            print("Expense Type :", expense[2])
            print("Amount       :", expense[3])
            print("Expense Date :", expense[4])
            print("Description  :", expense[5])
            print("Status       :", expense[6])
            print("-----------------------------")
    cursor.close() 

def search_expense():
    try:
        expense_id = int(input("Enter Expense ID: "))
    except ValueError:
        print("Invalid Expense ID. Please enter numbers only.")
        return   
    cursor=connection.cursor()
    query=""" SELECT expense_id,employee_id,expense_type,amount,expense_date,description,status
    FROM expenses WHERE expense_id=:1"""
    try:
        cursor.execute(query, (expense_id,))

        expense = cursor.fetchone()

        if expense:
            print("\n===== Expense Found =====")
            print("Expense ID   :", expense[0])
            print("Employee ID  :", expense[1])
            print("Expense Type :", expense[2])
            print("Amount       :", expense[3])
            print("Expense Date :", expense[4])
            print("Description  :", expense[5])
            print("Status       :", expense[6])
        else:
            print("Expense not found.")

    except Exception as e:
        print("Unable to search expense.")
        print("Error:", e)

    finally:
        cursor.close()
def update_expense():
    expense_id=int(input("Enter Expense ID to Update: "))        
    new_status=input("Enter new status (Approved/Rejected): ").upper()
    if new_status not in ("APPROVED","REJECTED"):
        print("Invalid status.Please enter APPROVED or REJECTED")
        return
    cursor=connection.cursor()
    query=""" UPDATE expenses SET status=:1 WHERE expense_id=:2"""
    try:
        cursor.execute(query, (new_status, expense_id))

        if cursor.rowcount > 0:
            connection.commit()
            print("Expense status updated successfully!")
        else:
            print("Expense not found.")

    except Exception as e:
        connection.rollback()
        print("Unable to update expense status.")
        print("Error:", e)

    finally:
        cursor.close()
def delete_expense():
    expense_id=int(input("Enter Expense ID to delete: "))            
    cursor=connection.cursor()
    query=""" DELETE FROM expenses WHERE expense_id=:1"""
    try:
        cursor.execute(query, (expense_id,))

        if cursor.rowcount > 0:
            connection.commit()
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")

    except Exception as e:
        connection.rollback()
        print("Unable to delete expense.")
        print("Error:", e)

    finally:
        cursor.close()
def total_expenses():
    cursor=connection.cursor()
    query= """ SELECT NVL(SUM(amount),0) FROM expenses"""   
    cursor.execute(query)
    total=cursor.fetchall()[0]
    print("\n===========Total Expenses========")
    print("Total Expense Amount: ",total)
    cursor.close()
def employee_wise_expenses():
    cursor=connection.cursor()
    query=""" SELECT employee_id,SUM(amount)
    FROM expenses GROUP BY employee_id 
    ORDER BY employee_id"""    
    cursor.execute(query)
    expenses=cursor.fetchall()
    print("\n==========Employee-wise-Total Expensea============")
    for expense in expenses:
        print("Employee ID: ",expense[0])
        print("Total Expense :",expense[1])
        print("==============================")
    cursor.close()

def approved_expenses():
    cursor=connection.cursor()
    query=""" SELECT NVL(SUM(amount),0) 
    FROM expenses 
    WHERE status='APPROVED'"""
    cursor.execute(query)
    total=cursor.fetchone()[0]
    print("\n=======Approved Expenses=====")
    print("Approved Expenses Amount==========",total)
    cursor.close()
def pending_expenses():
    cursor=connection.cursor()
    query=""" SELECT NVL(SUM(amount),0) 
    FROM expenses 
    WHERE status='PENDING'"""
    cursor.execute(query)
    total=cursor.fetchone()[0]
    print("\n=======PENDING Expenses=====")
    print("PENDING Expenses Amount==========",total)
    cursor.close()  
def rejected_expenses():
    cursor=connection.cursor()
    query=""" SELECT NVL(SUM(amount),0) 
    FROM expenses 
    WHERE status='REJECTED'"""
    cursor.execute(query)
    total=cursor.fetchone()[0]
    print("\n=======REJECTED Expenses=====")
    print("REJECTED Expenses Amount==========",total)
    cursor.close()  
    

        


