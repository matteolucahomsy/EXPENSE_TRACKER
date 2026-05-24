from expense import Expense
import sqlite3
class ExpenseManager:
    def __init__(self):
        self.budget= None
    def add_expense(self,expense):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("""
        INSERT INTO expenses (title,amount,category,date)
        VALUES (?,?,?,?)
        """,(
            expense.title,
            expense.amount,
            expense.category,
            expense.date
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
    def total_expenses(self):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM expenses")
        total=cursor.fetchone()[0]
        conn.close()
        return total if total else 0
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
        self.budget=budget
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
    def get_all_expenses(self):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM expenses")
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
    def get_statistics(self):
        conn=sqlite3.connect("expenses.db")
        cursor=conn.cursor()
        cursor.execute("SELECT category,SUM(amount)  FROM expenses GROUP BY category")
        data=cursor.fetchall()
        conn.close()
        
        return data