from expense import Expense
from expense_manager import ExpenseManager

manager=ExpenseManager()

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show total")
    print("4. exit")

    choice=input("choose an option: ")
    if choice== "1":
        title=input("Enter title: ")
        amount=float(input("Enter amount: "))
        category=input("Enter category: ")

        expense=Expense(title,amount,category)
        manager.add_expense(expense)
        print("Expense added successfully!")
    elif choice == "2":
        manager.view_expenses()
    elif choice == "3":
       total=manager.total_expenses()
       print(f"Total expenses: ${total}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")