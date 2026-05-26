from expense import Expense
from flask import session
import sqlite3
class ExpenseManager:
    def __init__(self):
        self.budget= None
        self.init_db()
    def add_expense(self,expense,user_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("""
        INSERT INTO expenses (title,amount,category,date, user_id)
        VALUES (?,?,?,?,?)
        """,(
            expense.title,
            expense.amount,
            expense.category,
            expense.date,
            user_id
        ))
        conn.commit()
        conn.close()
        print("Expense added succesfully!")
    def remove_expense(self,expense_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id=? ", (expense_id,))
        conn.commit()
        if cursor.rowcount==0:
            print("Expenses not found.")
        else:
            print("Expense removed successfully!")
        conn.close()
    def update_expense(self,expense_id,new_title,new_amount,new_category):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("""UPDATE expenses SET title=?,amount=?,category=? WHERE id =? """,(
            new_title,new_amount,new_category,expense_id
        ))
        conn.commit()
        if cursor.rowcount ==0:
            print("Expense not found.")
        else:
            print("Expense updated successfully!")
        conn.close()
    def view_expenses(self):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        expenses=cursor.fetchall()
        conn.close()
        if not expenses:
            print("No expenses found.")
            return
        for expense in expenses:
            expense_id=expense[0]
            title=expense[1]
            amount=expense[2]
            category=expense[3]
            date=expense[4]
            print(f"{expense_id}. {title} - ${amount} - {category} - {date}")
    def total_expenses(self,user_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id=?",(user_id,))
        total=cursor.fetchone()[0]
        conn.close()
        return total or 0
    def search_expense(self, keyword):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE title LIKE ?",(f"%[keyword]%",))
        results=cursor.fetchall()
        conn.close()
        if not results:
            print("NO matching expenses found.")
            return
        for expense in results:
            expense_id=expense[0]
            title=expense[1]
            amount=expense[2]
            category=expense[3]
            date=expense[4]
            print(f"{expense_id}. {title} - ${amount} - {category} - {date}")
    def show_statistics(self):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT category,SUM(amount) FROM expenses GROUP BY category")
        stats=cursor.fetchall()
        conn.close()
        if not stats:
            print("No expenses found.")
            return
        print("\n === Statistics by Category ===")
        for category, total in stats:
            print(f"{category}: ${total}")

    def set_budget(self,budget):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("DELETE FROM budget")
        cursor.execute("INSERT INTO budget (amount) VALUES(?)", (budget,))
        conn.commit()
        conn.close()
    def show_budget_status(self):
        total=self.total_expenses()
        print(f"\nTotal expenses: ${total}")

        if self.budget is None:
            print("No budget set.")
            return 
        remaining= self.budget -total
        print(f"Budget: ${self.budget}")
        print(f"Remaining: ${remaining}")

        if remaining <0 :
            print("You exceeded your budget!")
    def init_db(self):

        conn = sqlite3.connect("expenses.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                amount REAL,
                category TEXT,
                date TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS budget (
                id INTEGER PRIMARY KEY,
                amount REAL
            )
        """)

        conn.commit()
        conn.close()


    def get_all_expenses(self,user_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE user_id=?",(user_id,))
        expenses=cursor.fetchall()
        conn.close()
        return expenses
    def get_expense_by_id(self,expense_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE id = ?",(expense_id,))
        expenses=cursor.fetchone()
        conn.close()
        return expenses
    def get_statistics(self,user_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT category,SUM(amount)  FROM expenses WHERE user_id=? GROUP BY category",(user_id,))
        data=cursor.fetchall()
        conn.close()
        
        return data
    def get_budget(self,user_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT amount FROM budget WHERE user_id=?",(user_id,))
        result=cursor.fetchone()
        conn.close()
        return result[0] if result else 0
    def get_budget_status(self,user_id):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT amount FROM budget WHERE user_id=?",(user_id,))
        budget=cursor.fetchone()
        budget=budget[0] if budget else 0
        cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id=?",(user_id,))
        total=cursor.fetchone()[0] or 0
        remaining=budget - total
        percent_used=(total/budget *100) if budget >0 else 0
        conn.close()
        return{
            "budget": budget,
            "total": total,
            "remaining": remaining,
            "percent": percent_used

        }