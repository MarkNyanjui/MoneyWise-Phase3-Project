from functions import add_transaction, add_user, add_category, add_budgets, add_savings

if __name__ == '__main__':
    pass

    Hello = '''
    0 - Exit the program
    1 - Add a new user
    2 - Add a new transaction
    3 - Add a new category
    4 - Add a new budget
    5 - Add a new saving
    '''
    while True:
        print(Hello)
        userInput = int(input('Select an option: '))
        if userInput == 0:
            print('Thank you and have a nice day')
            exit()
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
            print('Invalid choice')


