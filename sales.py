import db_store, db_manipulation, ui


def handle_menu_choice(choice):

    '''Main Menu'''

    quit = "q"
    choice2 = None

    if choice == '1':
        #TODO add function to set merchandise and call sub menu
        menu_to_sub_menu('merchandise')

    elif choice == '2':
        #TODO add function to set event and call sub menu
        menu_to_sub_menu('events')

    elif choice == '3':
        #TODO add function to set record and call sub menu
        menu_to_record_menu()

    elif choice == '4':
        #TODO add search function and call query menu
        menu_to_search_menu()

    elif choice == 'q':
        ui.message("Bye!")

    else:
        ui.message('Please enter a valid selection')


def menu_to_sub_menu(selection):

    '''Menu to the slected sub menu either events or merchandise'''

    quit = 'q'
    choice2 = None

    ui.display_sub_menu_title(selection)

    choice2 = ui.display_sub_menu()
    handle_sub_menu_choice(choice2, selection)


def menu_to_record_menu():

    '''Menu to the record menu'''

    quit = 'q'
    choice3 = None

    choice3 = ui.display_recored_menu()
    handle_record_menu_choice(choice3)


def menu_to_search_menu():

    '''Menu to Search menu'''

    quit = 'q'
    choice4 = None

    choice4 = ui.display_search_menu()
    handle_search_menu_choice(choice4)


def handle_sub_menu_choice(choice2, selection):

    '''Handles sub menu choice and specifies the events or merchandise table is selected'''

    if choice2 == '1':
        #TODO add function to display table
        data_list = db_store.db_get_data(selection)
        if data_list != None:
            ui.print_data(data_list)
        else:
            ui.message("\n  "+selection+" table contains zero data")
            pass
    elif choice2 == '2':
        #TODO add function to add data to table
        if selection == "merchandise":
            data = ui.merch_input()
        elif selection == "events":
            data = ui.event_input()
        boolean = db_manipulation.add(selection, data)
        if boolean:
            ui.message("\n  "+data[0]+" Added")
        elif boolean:
            ui.message("\n  Failed to Add "+data[0])
    elif choice2 == '3':
        #TODO add function to edit data in table
        data_list = db_store.db_get_data(selection)
        if data_list != None:
            ui.print_data(data_list)
            edit_id = ui.id_input()
            if selection == "merchandise":
                data = ui.merch_input()
            elif selection == "events":
                data = ui.event_input()
            boolean = db_manipulation.edit_update(selection, edit_id, data)
            if boolean:
                ui.message("\n  Update Succseeded")
                pass
            elif boolean:
                ui.message("\n  Failed to Update")
        else:
            ui.message("\n  "+selection+" table contains zero data")
            pass
    elif choice2 == '4':
        #TODO add function to delete data from table
        data_list = db_store.db_get_data(selection)
        if data_list != None:
            ui.print_data(data_list)
            delete_id = ui.id_input()
            boolean = db_manipulation.delete(selection, delete_id)
            if boolean:
                ui.message("\n  Delete Succseeded")
                pass
            elif boolean:
                ui.message("\n  Failed to Delete")
        else:
            ui.message("\n  "+selection+" table contains zero data")
    elif choice2 == '5':
        pass
    elif choice2 == 'q':
        ui.message("Bye!")
        main.choice = 'q'

    else:
        ui.message('Please enter a valid selection')


def handle_record_menu_choice(choice3):

    '''Handles users choice to display record analysis'''

    if choice3 == '1':
        record_list = db_store.db_get_records()
        if record_list != None:
            ui.print_record(record_list)
        else:
            ui.message("\n  No records currently exist")
            pass
    elif choice3 == '2':
        record_list = db_store.db_get_records()
        if record_list != None:
            ui.print_record(record_list)
            record = ui.record_inputs()
            boolean = db_manipulation.update_record(record)
            if boolean:
                ui.message("\n  Record Updated")
            elif boolean == False:
                ui.message("\n Record Failed to Update")
        else:
            ui.message("\n  No records currently exist")
            pass
    elif choice3 == '3':
        record_list = db_store.db_high_records()
        if record_list != None:
            ui.print_record(record_list)
        else:
            ui.message("\n  No records currently exist")
            pass
    elif choice3 == '4':
        record_list = db_store.db_total_sales_records()
        if record_list != None:
            ui.print_record(record_list)
        else:
            ui.message("\n  No records currently exist")
            pass
    elif choice3 == '5':
        record_list = db_store.db_total_merch_sales_records()
        if record_list != None:
            ui.print_record(record_list)
        else:
            ui.message("\n  No records currently exist")
            pass
    elif choice3 == '6':
        record_list = db_store.db_total_events_sales_records()
        if record_list != None:
            ui.print_record(record_list)
        else:
            ui.message("\n  No records currently exist")
            pass
    elif choice3 == '7':
        pass
    elif choice3 == 'q':
        ui.message("Bye!")
        main.choice = 'q'
    else:
        ui.message('Please enter a valid selection')


def handle_search_menu_choice(choice4):

    '''Handles choice from search menu and then finds and displays results'''

    if choice4 == '1':
        term = ui.search_input()
        data_list = db_store.db_get_event_search_data(term)
        if data_list != None:
            ui.print_data(data_list)
        else:
            ui.message('\n  Search for '+term+' has zero results')
    elif choice4 == '2':
        term = ui.search_input()
        data_list = db_store.db_get_merchandise_serch_data(term)
        if data_list != None:
            ui.print_data(data_list)
        else:
            ui.message('\n  Search for '+term+' has zero results')
    elif choice4 == '3':
        pass
    elif choice4 == 'q':
        ui.message("Bye!")
        main.choice = 'q'
    else:
        ui.message('Please enter a valid selection')


def main():

    db_store.db_setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu()
        handle_menu_choice(choice)


if __name__ == '__main__':
    main()
