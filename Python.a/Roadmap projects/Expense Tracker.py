import time
expenses = dict()
expense_id = 0
etime = 0
def add_expense(amount, description):
    global expense_id
    expenses[expense_id] = [f"{time.localtime()[0]}.{time.localtime()[1]}.{time.localtime()[2]}", round(float(amount), 1), description]
    expense_id += 1

def del_expense(id):
    global expense_id
    expenses.pop(id)
    expense_id -= 1 # not enough, needs to update ids
    for i in range(len(expenses)):
        if i >= id:
            expenses[i] = expenses[i + 1]
            expenses.pop(i + 1)
    
def view_expenses():
    global expense_id
    print("ID   Date       Amount(€)   Description")
    for i in range(len(expenses)):
        id = str(i).ljust(4)
        date = expenses[i][0]
        amount = str(round(expenses[i][1], 1)).ljust(10)
        desc = str(expenses[i][2]).ljust(25)
        print(f"{id} | {date} | {amount}| {desc}")
    print("========================================")
    print(f"Total expenses: {sum(expense[1] for expense in expenses.values())}€")

def spec_month_expenses(month):
    global expense_id
    print("ID   Date       Amount(€)   Description")
    for i in range(len(expenses)):
        if expenses[i][0].split('.')[1] == str(month):
            # Only show expenses from the specified month
            id = str(i).ljust(4)
            date = expenses[i][0]
            amount = str(expenses[i][1]).ljust(10)
            desc = str(expenses[i][2]).ljust(25)
            print(f"{id} | {date} | {amount}| {desc}")
    print("========================================")
    print(f"Total expenses: {sum(expense[1] for expense in expenses.values())}€")

def update_expense(id, amount, description):
    global expense_id
    if id in expenses.keys():
        expenses[id] = [expenses[id][0], amount, description]
    else:
        print("Expense ID not found.")
                        
for i in range(5):
    add_expense(float(input("Expense amount (decimal):\n" )), input("Expense description: "))
