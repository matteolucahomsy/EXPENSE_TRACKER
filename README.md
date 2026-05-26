# 💰 Expense Tracker (Flask + SQLite)

A modern personal finance tracker built with **Flask**, **SQLite**, **Bootstrap**, and **Chart.js**.

This web application allows users to manage expenses, track budgets, and visualize spending using interactive charts and a clean dashboard UI.

---

## 🚀 Features

✔ Add, edit, delete expenses  
✔ Budget tracking system  
✔ Live remaining balance calculation  
✔ Progress bar (visual budget usage)  
✔ Budget alerts (warning & danger levels)  
✔ Category-based statistics  
✔ Interactive charts (bar & pie)  
✔ Clean Bootstrap dashboard UI  

### 📌 Expense Management
- ➕ Add expenses
- ✏️ Edit expenses
- ❌ Delete expenses
- 📋 View all expenses

---

### 💰 Budget System
- Set a global budget
- Track:
  - Total spent
  - Remaining balance
  - Percentage used
- Dynamic progress bar

---

### ⚠️ Budget Alerts
- 🟢 Green → safe
- 🟠 Orange → budget almost reached (>80%)
- 🔴 Red → budget exceeded (>100%)

Real-time alert messages are displayed on the dashboard.

---

### 📊 Statistics & Analytics
Interactive charts using **Chart.js**:
- 📈 Bar chart
- 🥧 Pie chart

Expenses are grouped by category for better visualization.

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- SQLite 🗄️
- HTML / CSS 🎨
- Bootstrap 5
- Jinja2
- Chart.js 📊

---

## 📂 Project Structure

```txt
expense-tracker/
│
├── main.py
├── database.py
├── expense_manager.py
├── models/
│   ├── expense.py
│   └── user.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── stats.html
│   └── edit.html
│
├── static/
│   └── style.css
│
├── expenses.db
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```
### 2.Install Flask
```bash
pip install flask
```
### 3.Run the application
```bash 
python main.py
```
### 4.Open in browser
http://127.0.0.1:5000

### Installation
```bash
pip install -r requirements.txt
```
## 📸 Application Features

### 🏠 Dashboard
- Budget overview cards
- Progress bar
- Expense list

### 📊 Statistics Page
- Expense analytics
- Interactive visual charts

### ✏️ Edit Page
- Update expense title
- Update amount
- Update category


## 🧠 What I Learned

This project helped me practice:

- Flask routing
- CRUD operations
- SQLite database management
- Jinja2 templating
- Bootstrap UI development
- Chart.js integration
- Backend + frontend integration
- Dashboard design principles


## 🚀 Future Improvements

Possible future upgrades:

- 👤 User authentication
- 📅 Monthly reports
- 🔍 Advanced filtering
- ☁️ Cloud deployment
- 📱 Mobile responsive improvements
- 📤 Export to PDF/Excel

## Author 
Matteo Luca Homsy
