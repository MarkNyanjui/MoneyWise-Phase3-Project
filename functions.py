from tables import Users, Categories, Transactions, Budgets, Savings, Session
from datetime import datetime

######################################
# Adding new data functions

def add_user():
    name = input("Enter name:")
    email = input("Enter email:")
    
    with Session() as sesh:
        new_user = Users(name = name, email = email)
        sesh.add(new_user)
        sesh.commit()
        print(f"User '{name}' and '{email}'added successfully.")


def add_transaction():
    amount = input("Enter Transaction Amount:")
    description = input("Enter Description:")
    transaction_date = input("Enter Transaction Date (YYYY-MM-DD):")
    transaction_type = input("Enter Transaction Type (Income/Expense):")
    category_id = input("Enter Category ID:")

    try:
        amount = float(amount)
    except ValueError:
        print('Invalid input: Amount must be a number')
        return
    try:
        transaction_date = datetime.strptime(transaction_date, "%Y-%m-%d")
    except ValueError:
        print('Invalid input: Transaction Date must be in the format YYYY-MM-DD')
        return

    if not isinstance(description, str) or isinstance(transaction_type, str):
        print('Invalid input: Description and Transaction Type must be strings')

    try:
        category_id = int(category_id)
    except ValueError:
        print('Invalid input: Category ID must be an integer')
        return
    
    with Session() as sesh:
        new_transaction = Transactions(
            amount = amount,
            description = description,
            transaction_date = transaction_date,
            transaction_type = transaction_type,
            category_id = category_id,
        )
        sesh.add(new_transaction)
        sesh.commit()
        print("Transaction has been added successfully.")

def add_category():
    name = input('Enter name: ')

    if not isinstance(name, str):
        print('Invalid input: Name must be a string')

    
    with Session() as sesh:
        new_category = Categories(
            name = name
        )
        sesh.add(new_category)
        sesh.commit()
        print('Category has been added successfully')


def add_budgets():
    amount = input('Enter amount: ')
    category_id = int(input('Enter Category ID: '))
    month= input('Enter the month: ')
    year = int(input('Enter the year: '))

    months = ['January', 'February','March', 'April','May', 'June', 'July', 'August', 'September', 'October','November','December']
    try:
        amount = float(amount)
    except ValueError:
        print('Invalid input: Amount must be a number')
        return
    
    if not isinstance(category_id, int):
        print('Invalid input: Category ID must be an integer')

    if month not in months:
        print('Invalid input: Month must an existing month')
    
    if year < 0:
        print('Invalid input: Year must be greater than 0')

    with Session() as sesh:
        new_budget = Budgets(
            amount = amount,
            category_id = category_id,
            month = month,
            year = year
        )
        sesh.add(new_budget)
        sesh.commit()
        print('Budget has been added successfully')


def add_savings():
    amount = input('Enter amount: ')
    goal = input('Enter goal: ')
    start_month = input('Enter Start Month: ')
    end_month = input('Enter End Month: ')
    user_id = int(input('Enter User ID: '))

    months = ['January', 'February','March', 'April','May', 'June', 'July', 'August', 'September', 'October','November','December']

    try:
        amount = float(amount)
    except ValueError:
        print('Invalid input: Amount must be a number')
        return
    try:
        goal = float(goal)
    except ValueError:
        print('Invalid input: Goal must be a number')
        return
    if start_month and end_month not in months:
        print('Invalid input: Months must be existing months')

    with Session() as sesh:
        new_saving = Savings(
            amount = amount,
            goal = goal,
            start_month = start_month,
            end_month = end_month,
            user_id = user_id
        )
        sesh.add(new_saving)
        sesh.commit()
        print('Saving has been added successfully')

###########################################################################
# Delete functions






    

