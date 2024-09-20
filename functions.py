from tables import Users, Categories, Transactions, Budgets, Savings, Session
from datetime import datetime

######################################
# Adding new data functions

def add_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    
    with Session() as sesh:
        new_user = Users(name = name, email = email)
        sesh.add(new_user)
        sesh.commit()
        print(f"User '{name}' and '{email}'added successfully.")


def add_transaction():
    amount = input("Enter Transaction Amount: ")
    description = input("Enter Description: ")
    transaction_date = input("Enter Transaction Date (YYYY-MM-DD): ")
    transaction_type = input("Enter Transaction Type (Income/Expense): ")
    category_id = input("Enter Category ID: ")

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
        goal = str(goal)
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
def delete_user():
    user_id = int(input("Enter User ID to delete: "))

    with Session() as sesh:
        user = sesh.query(Users).filter_by(user_id=user_id.first())
        if user is not None:
            sesh.delete(user)
            sesh.commit()
            print(f"User with ID '{user_id}' has been successfully deleted")

def delete_transaction():
    transactions_id = int(input("Enter Transaction to delete: "))

    with Session() as sesh:
        transaction = sesh.query(Transactions).filter_by(transactions_id=transactions_id.first())
        if transaction is not None:
            sesh.delete(transaction)
            sesh.commit()
            print(f"Transaction with ID '{transactions_id}' has been successfully deleted")

def delete_Category():
    category_id = int(input("Enter Category to delete: "))

    with Session() as sesh:
        category = sesh.query(Categories).filter_by(category_id=category_id.first())
        if category is not None:
            sesh.delete(category)
            sesh.commit()
            print(f"Category with ID '{category_id}' has been successfully deleted")

def delete_budget():
    budget_id = int(input("Enter Budget to delete: "))

    with Session() as sesh:
        budget = sesh.query(Budgets).filter_by(budget_id=budget_id.first())
        if budget is not None:
            sesh.delete(budget)
            sesh.commit()
            print(f"Budget with ID '{budget_id}' has been successfully deleted")

def delete_saving():
    savings_id = int(input("Enter Saving to delete: "))

    with Session() as sesh:
        saving = sesh.query(Savings).filter_by(savings_id=savings_id.first())
        if saving is not None:
            sesh.delete(saving)
            sesh.commit()
            print(f"Saving with ID '{savings_id}' has been successfully deleted")


#######################################################################################

## Update functions 
def update_user():
    user_id = int(input("Enter User ID to update: "))
    new_name = input("Enter new name: ")
    new_email = input("Enter new email: ")

    with Session() as sesh:
        user = sesh.query(Users).filter_by(user_id=user_id).first()
        if user is not None:
            user.name = new_name
            user.email = new_email
            sesh.commit()
            print(f"User with ID '{user_id}' has been successfully updated")


def update_category():
    category_id = int(input("Enter Category ID to update: "))
    new_name = input("Enter new name: ")

    with Session() as sesh:
        category = sesh.query(Categories).filter_by(category_id=category_id).first()
        if category is not None:
            category.name = new_name
            sesh.commit()
            print(f"User with ID '{category_id}' has been successfully updated")

def update_transaction():
    transaction_id = int(input("Enter Transaction ID to update: "))
    new_amount = input("Enter new amount: ")
    new_description = input("Enter new description: ")
    new_transaction_date = input("Enter new transaction date (YYYY-MM-DD): ")
    new_transaction_type = input("Enter new transaction type (Income/Expense): ")
    new_category_id = input("Enter new category ID: ")

    try:
        new_amount = float(new_amount)
    except ValueError:
        print('Invalid input: Amount must be a number')
        return
    try:
        new_transaction_date = datetime.strptime(new_transaction_date, "%Y-%m-%d")
    except ValueError:
        print('Invalid input: Transaction Date must be in the format YYYY-MM-DD')
        return

    if not isinstance(new_description, str) or isinstance(new_transaction_type, str):
        print('Invalid input: Description and Transaction Type must be strings')

    try:
        new_category_id = int(new_category_id)
    except ValueError:
        print('Invalid input: Category ID must be an integer')
        return
    
    with Session() as sesh:
        transaction = sesh.query(Transactions).filter_by(transaction_id=transaction_id).first()
        if transaction is not None:
            transaction.amount = new_amount
            transaction.description = new_description
            transaction.transaction_date = new_transaction_date
            transaction.transaction_type = new_transaction_type
            transaction.category_id = new_category_id
            sesh.commit()
            print("Transaction has been successfully updated")

def update_budget():
    budget_id = int(input("Enter Budget ID to be updated: "))
    new_amount = input('Enter new amount: ')
    new_category_id = int(input('Enter new Category ID: '))
    new_month= input('Enter the new month: ')
    new_year = int(input('Enter the new year: '))

    months = ['January', 'February','March', 'April','May', 'June', 'July', 'August', 'September', 'October','November','December']
    try:
        new_amount = float(new_amount)
    except ValueError:
        print('Invalid input: Amount must be a number')
        return
    
    if not isinstance(new_category_id, int):
        print('Invalid input: Category ID must be an integer')

    if new_month not in months:
        print('Invalid input: Month must an existing month')
    
    if new_year < 0:
        print('Invalid input: Year must be greater than 0')

    with Session() as sesh:
        budget = sesh.query(Budgets).filter_by(budget_id=budget_id).first()
        if budget is not None:
            budget.amount = new_amount
            budget.category_id = new_category_id
            budget.month = new_month
            budget.year = new_year
            sesh.commit()
            print("Budget has been successfully updated")

def update_saving():
    saving_id = int(input("Enter Saving ID to update: "))
    new_amount = input("Enter new amount: ")
    new_goal = input("Enter new goal:")
    new_start_month = input("Enter the new start month: ")
    new_end_month = input("Enter the new end month: ")
    new_user_id = int(input("Enter the new user ID: "))

    months = ['January', 'February','March', 'April','May', 'June', 
              'July', 'August', 'September', 'October','November','December']

    try:
        new_amount = float(new_amount)
    except ValueError:
        print('Invalid input: Amount must be a number')
        return
    
    if not isinstance(new_goal, str):
        print("Invalid input: Goal must be a string")
        return
    
    if new_start_month and new_end_month not in months:
        print('Invalid input: Months must be existing months')
        return

    with Session() as sesh:
        saving = sesh.query(Savings).filter_by(saving_id=saving_id).first()
        if saving is not None:
            saving.amount = new_amount
            saving.goal = new_goal
            saving.start_month = new_start_month
            saving.end_month = new_end_month
            saving.user_id = new_user_id
        sesh.commit()
        print('Saving has been successfully updated')






    

    








    

