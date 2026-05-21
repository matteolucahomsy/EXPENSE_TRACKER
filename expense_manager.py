from expense import Expense
import json
class ExpenseManager:
    def __init__(self):
        self.expenses=[]
        self.load_expenses()
    def add_expense(self,expense):
        self.expenses.append(expense)
        self.save_expenses()
    def remove_expense(self,index):
        if 0<= index<len(self.expenses):
            removed= self.expenses.pop(index)
            self.save_expenses()
            print(f"{removed.title} removed successfully!")
        else:
            print("Invalid expense index.")
    def update_expense(self,index,new_title,new_amount,new_category):
        if not (0 <= index < len(self.expenses)):
            print("Invalid expense index.")
            return False
       
        self.expenses[index].title= new_title
        self.expenses[index].amount= new_amount
        self.expenses[index].category = new_category

        self.save_expenses()
        print("Expens updated successfully!")
        return True
    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        for index,expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense.title} - ${expense.amount} - {expense.category} - {expense.date}")
    def total_expenses(self):
        total=sum(expense.amount for expense in self.expenses)
        return total
    def save_expenses(self):
        data=[expense.to_dict() for expense in self.expenses]
        with open("data.json", "w") as file:
            json.dump(data,file, indent=4)
    def load_expenses(self):
        try:
            with open("data.json", "r") as file:
                data=json.load(file)
                for item in data:
                    expense=Expense(
                        item["title"],
                        item["amount"],
                        item["category"]
                    )
                    expense.date=item.get("date", "Unknown")
                    self.expenses.append(expense)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses=[]
    def search_expense(self, keyword):
        found =False
        for index,expense in enumerate(self.expenses, start=1):
            if keyword.lower() in expense.title.lower():
                print(f"{index}. {expense.title} - ${expense.amount} - {expense.category} - {expense.date}")
                found = True
        if not found:
                print("No matching expenses found. ")

