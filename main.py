from expense import Expense
import sqlite3
import database
from expense_manager import ExpenseManager
from flask import Flask, render_template, request ,redirect
app=Flask(__name__)
manager=ExpenseManager()

@app.route("/")
def home():
    expenses=manager.get_all_expenses()
    return render_template("index.html",expenses=expenses)
@app.route("/add",methods=["POST"])
def add_expense():
    title=request.form["title"]
    amount=float(request.form["amount"])
    category=request.form["category"]
    expense=Expense(
        title,
        amount,
        category
    )
    manager.add_expense(expense)
    return redirect("/")
@app.route("/delete/<int:id>",methods=["POST"])
def delete_expense(id):
    manager.remove_expense(id)
    return redirect("/")
@app.route("/edit/<int:id>")
def edit_page(id):
    expense=manager.get_expense_by_id(id)
    return render_template("edit.html",expense=expense)
@app.route("/update/<int:id>",methods=["POST"])
def update_expense(id):
    title=request.form["title"]
    amount=float(request.form["amount"])
    category=request.form["category"]

    manager.update_expense(id,title,amount,category)
    return redirect("/")
@app.route("/stats",methods=["POST"])
def stats():
    data=manager.get_statistics()
    return render_template("stats.html",data=data)



if __name__=="__main__":
    app.run(debug=True)
# while True:
#     print("\n=== Expense Tracker ===")
#     print("1. Add Expense")
#     print("2. Remove Expense")
#     print("3. Update Expense")
#     print("4. Search Expense")
#     print("5. View Expense")
#     print("6. Show total")
#     print("7. Show Statistics")
#     print("8. Set Budget")
#     print("9. Show Budget Status")
#     print("10. exit")

#     choice=input("choose an option: ")
#     if choice== "1":
#         title=input("Enter title: ")
#         amount=float(input("Enter amount: "))
#         category=input("Enter category: ")

#         expense=Expense(title,amount,category)
#         manager.add_expense(expense)
#         print("Expense added successfully!")
#     elif choice == "2":
#         manager.view_expenses()
#         expense_id=int(input("Enter expense ID to remove: "))
#         manager.remove_expense(expense_id)
#     elif choice == "3":
#         manager.view_expenses()
#         expense_id=int(input("Enter expense id to update: ")) 
#         new_title=input("Enter new title: ")
#         new_amount=float(input("Enter new amount: "))
#         new_category=input("Enter new category: ")

#         manager.update_expense(expense_id,new_title,new_amount,new_category)
#     elif choice == "4":
#         keyword = input("Enter keyword to search: ")
#         manager.search_expense(keyword)    
#     elif choice == "5":
#         manager.view_expenses()
#     elif choice == "6":
#        total=manager.total_expenses()
#        print(f"Total expenses: ${total}")
#     elif choice == "7":
#         manager.show_statistics()
#     elif choice== "8":
#         budget=float(input("Enter your budget: "))
#         manager.set_budget(budget)
#         print("Budget set!")
#     elif choice == "9":
#         manager.show_budget_status()
#     elif choice == "10":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid option.")