from expense import Expense
from expense_manager import ExpenseManager

manager=ExpenseManager()

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. Update Expense")
    print("4. Search Expense")
    print("5. View Expense")
    print("6. Show total")
    print("7. exit")

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
        index=int(input("Enter expense number to remove: ")) -1
        manager.remove_expense(index)
    elif choice == "3":
        if not manager.expenses:
            print("No expenses to update.")
            continue
        manager.view_expenses()
        index=int(input("Enter expense number to update: "))-1
        if not (0<= index < len(manager.expenses)):
            print("Invalid expense index.")
            continue
        new_title=input("Enter new title: ")
        new_amount=float(input("Enter new amount: "))
        new_category=input("Enter new category: ")

        manager.update_expense(index,new_title,new_amount,new_category)
    elif choice == "4":
        keyword = input("Enter keyword to search: ")
        manager.search_expense(keyword)    
    elif choice == "5":
        manager.view_expenses()
    elif choice == "6":
       total=manager.total_expenses()
       print(f"Total expenses: ${total}")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")