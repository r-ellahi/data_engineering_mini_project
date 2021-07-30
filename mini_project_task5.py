from mini_project_functions import whitespace, read_csv_file, print_csv_file, save_csv_file, append_dict, update_items
from csv import DictWriter, DictReader
from pprint import pprint

product = []
courier = []
orders = []

product = read_csv_file('product_list.csv', product)
courier = read_csv_file('courier_list.csv', courier)
orders = read_csv_file('orders.csv', orders)

order_status = ['Order Confirmed', 'Preparing', 'Quality Check', 'On Route', 'Delivered', 'Unable to Deliver']

def main_menu():
    print("""\033[33m\n\tMain Menu:\033[0m""")
    print("""
        [0] - To Exit 
        [1] - Product Options
        [2] - Courier Options
        [3] - Order Details
    """)
    
    option = int(input("""\033[33m\n\tEnter your choice here: \033[0m"""))
    
    if option == 0:
        save_csv_file('product_list.csv', product)
        save_csv_file('courier_list.csv', courier)
        save_csv_file('orders.csv', orders)
        whitespace()
        print('\tThanks for visiting!')
        whitespace()
        exit()
    
    elif option == 1:
        product_menu()   
        
    elif option == 2:
        courier_menu()
    
    elif option == 3:
        orders_details()
        
    else:
        print ('\tPlease enter a valid option')
        whitespace()
        main_menu()    


def product_menu():
    print("""\033[33m\n\tProduct Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - View Menu
        [2] - Create New Product
        [3] - Update Existing Product    
        [4] - Delete a Product''')
    whitespace()
    user_input = int(input("""\033[33m\n\tEnter your choice here: \033[0m"""))
        
        
    if user_input == 0:
        main_menu()
    
    # elif user_input == 1:
    # GET all products from products table
    # PRINT products
    
    # elif user_input == 2:
    # CREATE new product
    #  GET user input for product name
    #  GET user input for product price
    # INSERT product into products table   
        
    # elif user_input == 3:
    #  # STRETCH GOAL - UPDATE existing product
    # GET all products from products table
    # PRINT products with their IDs
    # GET user input for product ID
    # GET user input for product name
    # GET user input for product price
    # IF any inputs are empty, do not update them
    # UPDATE properties for product in product table    
            
    # elif user_input == 4:
    #      # STRETCH GOAL - DELETE product
    # GET all products from products table
    # PRINT products with their IDs
    # GET user input for product ID
    # DELETE product in products table


def courier_menu():
    print("""\033[33m\n\tCourier Options:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - Print Courier List
        [2] - Create New Courier
        [3] - Update Courier
        [4] - Delete Courier
                        ''')
    user_input = int(input("""\033[33m\n\tEnter your choice here:  \033[0m"""))

    if user_input == 0:    
        whitespace()
        print('Thanks for visiting!')
        whitespace()
        main_menu()
    
    # elif user_input = 1:
    # GET all couriers from couriers table
    # PRINT couriers
    
    # elif user_input = 2:
    # CREATE new courier
    # GET user input for courier name
    # GET user input for courier phone number
    # INSERT courier into couriers table  
    
    # elif user_input = 3:
    # STRETCH GOAL - UPDATE existing courier
    # GET all couriers from couriers table
    # PRINT couriers with their IDs
    # GET user input for courier ID
    # GET user input for courier name
    # GET user input for courier phone number
    # IF an input is empty, do not update its respective table property
    # UPDATE properties for courier in courier table
    
    # elif user_input = 4:
    # STRETCH GOAL - DELETE courier
    # GET all couriers from couriers table
    # PRINT courier with their IDs
    # GET user input for courier ID
    # DELETE courier in couriers table


def orders_details():
    print("""\033[33m\n\tOrder Details:\033[0m""")
    print('''
        [0] - Return to Main Menu
        [1] - View Order
        [2] - Enter Details
        [3] - Update Order Status  
        [4] - Update Existing Order
        [5] - Delete Order
        ''')
    user_input = int(input("""\033[33m\n\tEnter your choice here: \033[0m"""))
    
    
    if user_input == 0:
        main_menu()

    elif user_input == 1:
        whitespace()
        # for order in orders:
        #     print(order)
        pprint(orders)
        whitespace()
        orders_details()

    elif user_input == 2:
        customer_name = input("\tEnter your name: ")
        customer_address = input("\tEnter your address: ")
        customer_number = int(input("\tEnter your number: "))
        
        for value, index in enumerate(product):
            print(value, index)
        product_choice = input('Please select your products: ')
        
        for value, index in enumerate(courier):
            print(value, index)
        courier_choice = int(input('Who would you like to deliver your order:?  '))
        
        entry = {}
        entry['Customer Name'] = customer_name 
        entry ['Customer Address'] = customer_address
        entry ['Customer Phone Number'] = customer_number
        entry ['Courier'] = courier_choice
        entry['Status'] = order_status[1]
        entry['Products'] = product_choice
        
        titles = ['Customer Name', "Customer Address", 'Customer Phone Number','Courier', 'Status', "Products"]
        append_dict('orders.csv', entry, titles)
        
        print('Thank you for your order', entry)

    elif user_input == 3:
        for key, value in enumerate(orders):
            print(key, value)

        order_index = int(input("""\033[33m\nPlease select an order to update:   \033[0m"""))
        print('')

        for key, value in enumerate(order_status):
            print(key, value)

        status_input = int(
            input("""\033[33m\nChoose an order status to update on the order list:   \033[0m"""))
        order_to_update = orders[order_index]
        
        order_to_update['Status'] = order_status[status_input]
        print("""\033[33m\nOrder status has been updated\033[0m""")
        pprint(order_to_update)

    elif user_input == 4:
        for key, value in enumerate (orders):
            print(key, value)
        order_index = int(input(''' \033[33m\n\tSelect an order to update:    \033[0m'''))
        updated_order = orders[order_index] 
        old_order = updated_order.copy()
        for key, value in updated_order.items():
            print(key, value)
            chosen_order = input(f'\n{key} is currently {value}. Enter new details for {key}: ')
            if chosen_order == '':
                updated_order[key] = value
                print('\nNothing has been changed')
            else:
                updated_order[key] = chosen_order
        print(f'\n\tYour order has been updated from {old_order} to {updated_order}')
        orders_details()

    elif user_input == 5:
        for key, value in enumerate(orders):
            print(key, value)
        delete_order = int(input('''
        \033[33m\n\tSelect an order to delete:    \033[0m''')) 
        orders.pop(delete_order)
        print('''
                \033[33m\n\tOrder was deleted successfully.
                
        Remaining Orders: 
                \033[0m''')
        print(orders)
        whitespace()
        orders_details()
main_menu()