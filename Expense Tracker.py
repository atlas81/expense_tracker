import time
expenses = dict()
expense_id = 0
etime = 0
def add_expense(amount, description):
    global expense_id
    expenses[expense_id] = [f"{time.localtime()[0]}.{time.localtime()[1]}.{time.localtime()[2]}", amount, description]
    expense_id += 1

def del_expense(id):
    global expense_id
    expenses.pop(id)
    expense_id -= 1 # not enough, needs to update ids
    
def view_expenses():
    global expense_id
    print("ID   Date       Amount      Description")
    for i in range(len(expenses)):
        id = str(i).ljust(4)
        date = expenses[i][0]
        amount = str(expenses[i][1]).ljust(10)
        desc = str(expenses[i][2]).ljust(25)
        print(f"{id} | {date} | {amount}| {desc}")

add_expense(float(input("Expense amount (decimal):\n" )), input("Expense description: "))
add_expense(float(input("Expense amount (decimal):\n" )), input("Expense description: "))
view_expenses()
del_expense(0)
print(expenses)
view_expenses()