from functions import add_transaction, add_user, add_category, add_budgets, add_savings,update_category,update_saving,update_transaction,update_user,update_budget, delete_budget,delete_Category,delete_saving,delete_transaction,delete_user

################################################################################################
# The functions within this block are for the menus displayed when the users branches to Add, update or delete data in the main menu
def adding_data():
    Add = '''
    Please select an option from the following to add data:
    1 - Add a new user
    2 - Add a new transaction
    3 - Add a new category
    4 - Add a new budget
    5 - Add a new savings
    0 - Return to Main Menu
    '''
    while True:
        print(Add)
        userInput = int(input("Select an option: "))
        if userInput == 0:
            return
        elif userInput == 1:
            add_user()
        elif userInput == 2:
            add_transaction()
        elif userInput == 3:
            add_category()
        elif userInput == 4:
            add_budgets()
        elif userInput == 5:
            add_savings()
        else:
            print("Please select a valid option")

def updating_data():
    Update = '''
    Please select an option from the following to update data:
    1 - Update a user
    2 - Update a transaction
    3 - Update a category
    4 - Update a budget
    5 - Update a savings
    0 - Return to Main Menu
    '''
    while True:
        print(Update)
        userInput = int(input("Select an option: "))
        if userInput == 0:
            return
        if userInput == 1:
            update_user()
        elif userInput == 2:
            update_transaction()
        elif userInput == 3:
            update_category()
        elif userInput == 4:
            update_budget()
        elif userInput == 5:
            update_saving()
        else:
            print("Please select a valid option")

def deleting_data():
    Delete = '''
    Please select an option from the following to delete data:
    1 - Delete a user
    2 - Delete a transaction
    3 - Delete a category
    4 - Delete a budget
    5 - Delete a savings
    0 - Return to Main Menu
    '''
    while True:
        print(Delete)
        userInput = int(input("Select an option: "))
        if userInput == 0:
            return
        elif userInput == 1:
            delete_user()
        elif userInput == 2:
            delete_transaction()
        elif userInput == 3:
            delete_Category()
        elif userInput == 4:
            delete_budget()
        elif userInput == 5:
            delete_saving()
        else:
            print("Please select a valid option")
#############################################################################################
  

if __name__ == '__main__':
   # This is the output seen on the terminal on the file is initialized
      Hello = '''
      Welcome to MoneyWise, your reliable personal finance tracker.
      Please select an option from the following:
      0 - Exit the program
      1 - Add new data
      2 - Update existing data
      3 - Delete Data
      '''
      while True:
        print(Hello)
        userInput = int(input('Select an option: '))
        if userInput == 0:
            print('Thank you and have a nice day')
            exit()
        elif userInput == 1:
            adding_data()
        elif userInput == 2:
            updating_data()
        elif userInput == 3:
            deleting_data()
        else:
            print('Invalid choice')


