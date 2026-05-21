from expense import Expense
class ExpenseManager:
    def __init__(self):
        self.expenses=[]
    def add_expense(self,expense):
        self.expenses.append(expense)
    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        for index,expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense.title} - ${expense.amount} - {expense.category}")
    def total_expenses(self):
        total=sum(expense.amount for expense in self.expenses)
        return total