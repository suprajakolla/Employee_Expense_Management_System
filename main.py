import employee
import expense
print("\n" + "=" * 55)
print("        EMPLOYEE EXPENSE & MANAGEMENT SYSTEM")
print("=" * 55)

while True:

    print("\n" + "-" * 55)
    print("                    MAIN MENU")
    print("-" * 55)

    print("1.  Add Employee")
    print("2.  View Employees")
    print("3.  Search Employee")
    print("4.  Update Employee")
    print("5.  Delete Employee")
    print("6.  Add Expense")
    print("7.  View Expenses")
    print("8.  Search Expense")
    print("9.  Update Expense Status")
    print("10. Delete Expense")
    print("11. Expense Reports")
    print("12. Exit")

    print("-" * 55)

    choice = input("Enter your choice: ")
    if choice=="1":
        employee.add_employee()
    elif choice=="2":    
        employee.view_employees()
    elif choice=="3":
        employee.search_employee()
    elif choice=="4":
        employee.update_employee()
    elif choice=="5":
        employee.delete_employee()
    elif choice=="6":
        expense.add_expenses()
    elif choice == "7":
        expense.view_expenses()

    elif choice == "8":
        expense.search_expense()

    elif choice == "9":
        expense.update_expense()

    elif choice == "10":
        expense.delete_expense()

    elif choice == "11":
        print("\n" + "=" * 55)
        print("                 EXPENSE REPORTS")
        print("=" * 55)

        expense.total_expenses()

        print("\n" + "-" * 55)
        expense.employee_wise_expenses()

        print("\n" + "-" * 55)
        expense.approved_expenses()

        print("\n" + "-" * 55)
        expense.pending_expenses()

        print("\n" + "-" * 55)
        expense.rejected_expenses()

        print("\n" + "=" * 55)

    elif choice == "12":
        print("\n" + "=" * 55)
        print("Thank you for using the Employee Expense & Management System!")
        print("             Have a great day! 😊")
        print("=" * 55)
        break

    else:
        print("\n⚠️ Invalid choice!")
        print("Please enter a number between 1 and 12.")



