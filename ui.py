
def display_banner():
    '''Display program name in a banner'''
    msg = 'Sales Program'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')


def display_sub_menu_title(title):
    '''Display the the option a user picked from the menu'''
    msg = 'Sales Program'
    dash = '-' * len(title)
    print('\n', dash, '\n', title, '\n', dash, '\n')


def display_menu():

    '''Display menu choices for user, return users selection'''

    print('''
        1. Merchandise
        2. Event
        3. Records
        4. Search
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def display_sub_menu():

    '''Display sub menu choices for user, return users selection'''

    print('''
        1. Display
        2. Add
        3. Edit
        4. Delete
        5. Back to Menu
        q. Quit
    ''')

    choice2 = input('Enter your selection: ')

    return choice2


def display_recored_menu():

    '''Display record menu choices for user, return users selection'''

    print('''
        1. Display Records
        2. Update Record
        3. Display Records (By Items Sold)
        4. Display Total for Merchandise by Event
        5. Display Total by Merchandise
        6. Display Total by Event
        7. Back to Menu
        q. Quit
    ''')

    choice3 = input('Enter your selection: ')

    return choice3


def display_search_menu():

    '''Display search menu choices for user, return users selection'''

    print('''
        1. Search By Event
        2. Search By Merchandise
        3. Back to Menu
        q. Quit
    ''')

    choice4 = input('Enter your selection: ')

    return choice4


def merch_input():

    '''Used for the add and edit function on the merchandise table'''

    name = input("Product name: ")
    cost = input("Product cost: $")
    data = [ name, cost ]
    return data


def event_input():

    '''Used for the add and edit function on the events table'''

    name = input("Event name: ")
    location = input("Event Location: ")
    date = input("Event date (mm/dd/yyyy): ")
    data = [ name, location, date ]
    return data


def id_input():

    '''Used by the edit and delete functions for the events and merchandise tables'''

    ID = input("Enter the id of the item to edit: ")

    return ID


def record_inputs():

    '''Uses event and merch variables to find a record with those ids and updates the sold variable'''

    event = input("Enter the name of the event: ")
    merch = input("Enter the product name: ")
    sold = input("Enter the number of products sold at the event: ")
    data = [ event, merch, sold ]
    return data


def search_input():

    '''Input used to query databse for similar data'''

    term = input("Enter search term: ")
    return term


def print_data(data_list):

    '''Print data from the events or merchandise table'''

    line = None
    for data in data_list:
        text = ' | '
        for d in data:
            text += str(d) + ' | '
        line = '-' * (len(text)-2)
        print(' ',line,'\n',text)
    if line != None:
        print(' ',line)
    else:
        message('\n  No data was Found')


def print_record(record_list):

    '''Prints results for inner joined querys that concatenate data to form analyses'''

    line = None
    for record in record_list:
        text = ' | '
        for r in record:
            text += str(r) + ' | '
        line = '-' * (len(text)-2)
        print(' ',line,'\n',text)
    if line != None:
        print(' ',line)
    else:
        message('\n  No record was Found')


def message(msg):

    '''Display a message to the user'''

    print(msg)
