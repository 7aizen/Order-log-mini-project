import csv #imports the csv files
import os #imports os so i dont have to type a long directory 
import myfunc #imports my function
import platform



# This function loads data from a CSV file named 'file_name'.
# If the file doesn't exist, it returns None.
# If the file exists, it reads the data and returns it as a list of dictionaries.
def load_csv(file_name):
    if not os.path.exists(file_name):
        return None
    with open (file_name, newline= '', mode='r' ) as f:
        return list(csv.DictReader(f))
    

# This function saves data to a CSV file named 'file_name'.
# It checks if there's data to save, and if so, it writes the data to the file.
# It uses the keys of the first dictionary in the 'data' list as field names in the CSV.
def save_csv(file_name, data):
    if data:
        with open(file_name, newline='', mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer .writeheader() # Writes the header row with field names
            writer.writerows(data) #writes the data as rows in the CSV
    

#

product_path = 'data\products.csv'
orders_path = 'data\orders.csv'
couriers_path = 'data\couriers.csv'

products = load_csv('data\products.csv')
couriers = load_csv('data\couriers.csv')
orders = load_csv('data\orders.csv')
order_statuses = ["Preparing", "Out for delivery", "Delivered"]




while True:
    print("Main Menu:")
    print("0. Exit App")
    print("1. Products Menu")
    print("2. Courier Menu")
    print("3. Orders menu")

    user_input = (input("Enter your selection: "))

    if user_input == "0":
        print("See you later!")
        save_csv(product_path, products)
        save_csv(couriers_path, couriers)
        save_csv(orders_path, orders)

         # EXIT app
        
        break
#PRODUCTS MENU  - LISTS
    elif user_input == "1":
        while True:
            print("Product Menu Options:")
            print("0. Return to main menu")
            print("1. Product menu")
            print("2. Add new product")
            print("3. Update existing product")
            print("4. Delete product")

            prod_input = input("Enter your selection: ")

            if prod_input == "0":
                    break
            elif prod_input == "1":
                    print('Products List: ')
                    myfunc.list_items(products)
                    

            elif prod_input == "2":
                    products.append(myfunc.add_item("product", ["name", "price"], products))
                    print('Updated Products List: ')
                    myfunc.list_items(products)

            elif prod_input == "3":
                myfunc.list_items(products)
                index = int(input("Enter product index to update: ")) - 1
                if 0 <= index < len(products):
                    myfunc.update_item(products, couriers, order_statuses, index)
                

            elif prod_input == "4":
                myfunc.list_items(products)
                index = int(input("Enter product index to delete: ")) - 1
                myfunc.delete_item(products, index)
                

    elif user_input == "2": 
        
        while True:
            print("Courier Menu")
            print("0. Return to main menu")
            print("1. Courier list")
            print("2. Add new courier")
            print("3. Update existing courier")
            print("4. Delete courier")

            # Ask the user to choose an option
            courier_input = input("Please enter a selection: ")

            if courier_input == "0":
                break
                    # If the user selects "0", exit the courier menu and return to the main menu
            elif courier_input == "1":
                print("Courier List: ") # Display the list of couriers
                myfunc.list_items(couriers) # Print the list of couriers
                

            elif courier_input == "2":
                print("Enter the courier you want to add: ") # Prompt user to enter a new courier
                couriers.append(myfunc.add_item("courier", ["name", "phone"], couriers)) # The new courier is now on the list
                print("The new courier has been added to the list.")
               

            elif courier_input == "3":
                myfunc.list_items(couriers)

                index = int(input("Enter courier index to update: ")) - 1

                if 0 <= index < len(couriers):
                            myfunc.update_item(couriers[index])
                print('the courier has been implemented into the list.')
                input("Press Enter to continue...")
                

            elif courier_input == "4":
                myfunc.list_items(couriers)
                index = int(input("Enter courier index to delete: ")) - 1
                myfunc.delete_item(couriers, index)
                print('the courier as been removed from the list.')
                

            else:
                print('Invalid option, will now return to the main menu.')


#PRINT ORDERS MENU
    elif user_input == "3": # If user selects the "Orders menu" option from the main menu
        while True:  # Enter into a loop for the orders menu
            #this displays the options in the orders menu
            print("Orders Menu:")
            print("0 - Return to main menu")
            print("1 - Print Order Dictionary")
            print("2 - Create new order")
            print("3 - Update existing order status")
            print("4 - Update existing order")
            print("5 - Delete order")

            # This Asks the user to choose an option within the orders menus
            order_input = input("Enter your option for the order menu:")


            if order_input == "0":  # If the user selects "0," inform them that they will return to the main menu
                print("Returning to main menu")
            # If user selects "0", exit the orders menu and return to the main menu 
                break

            elif order_input == "1":
                  # If the user selects "1," print the current order log

                # Iterate through each order in the order log and print its details
                myfunc.list_items(orders)
            
            elif order_input == "2": # If the user selects "2," create a new order

                # Prompt the user to enter the customer's name, address, and phone number
                customer_name = input("Enter customer name: ")
                customer_address = input("Enter customer address: ")
                customer_phone = input("Enter customer phone number: ")

                # Generate a unique order number by counting the existing orders and adding 1
                myfunc.list_items(products)
                product_indexes = input("Enter indexes of products (for multiple products include comma): ")
                product_ids = [products[int(index) - 1]['id'] for index in product_indexes.split(',')]
                products_string = ",".join(product_ids)

                # Add the new order to the order log with a "PREPARING" status
                myfunc.list_items(couriers)
                courier_index = int(input("Enter courier index: ")) - 1
                if 0 <= courier_index < len(couriers):
                        courier_id = couriers[courier_index]['id']
                        
                else:
                    print("Invalid courier index.")
                    # Exit the function to avoid adding an order with an invalid courier

                order = {
                        "customer_name": customer_name,
                        "customer_address": customer_address,
                        "customer_phone": customer_phone,
                        "courier": courier_id,
                        "status": order_statuses,
                        "products": products_string
                    }
                 # Add the new order to the order log and Informs the user that their order has been placed
                print("Your order has been placed")
                orders.append(order)
                

            elif order_input == "3":#Update existing order status

                # Iterate through each order in the order log and print its details
                myfunc.list_items(orders)
                # Prompt the user to select the index (order number) of the order they want to update
                index = int(input("Select the index value of the order number you'd like to update: ")) - 1


                # Prompt the user to enter the updated status for the selected order
                if 0 <= index < len(orders):
                    for i, status in enumerate(order_statuses, start=1):
                        print(f"{i}. {status}")
                    status_index = int(input("Enter new status index: ")) - 1
                    if 0 <= status_index < len(order_statuses):
                        orders[index]["status"] = order_statuses[status_index] # Update the status of the selected order in the order log
                        print("Order status updated successfully.")  # Inform the user that the order status has been updated
                        
                    else:
                        print("Invalid index.")
                else:
                    print("Invalid order index.")
                    input("Press Enter to continue...")


            elif order_input == "4":   # Update existing order details (name, address, phone number)
                myfunc.list_items(orders)

                 #Prompt the user to select the index (order number) of the order they want to update
                index = int(input("Select the index value of the order number you'd like to update: "))
                if 0 <= index < len(orders):
                    myfunc.update_item(orders[index],products ,couriers, order_statuses)
                    
            
                    
                print('Order has been updated!')  # Inform the user that the selected order has been updated

            
            elif order_input == "5":# If the user selects "5," delete an order

                # Iterate through each order in the order log and print its details
                myfunc.list_items(orders)
                index = int(input("Enter order index to delete: ")) - 1
                myfunc.delete_item(orders, index)
                

                # Remove the selected order from the order log

                print('Order has been deleted') # Inform the user that the selected order has been delete
            
            else: 
                # If the user enters an invalid option, inform them and break to return to the main menu
                print("Invalid selection returning to Main Menu")
                break

    # Define a function to handle the courier menu

