import os
import platform

def clear_console():
    if platform.system() == "Windows":
         os.system('cls')
    else:
         os.system('clear')
# This function calculates the next available ID for a new item based on existing items.
# If the items_list is empty, it returns 1 as the starting ID.
# If items exist, it finds the highest ID in the list, adds 1, and returns the next ID.
def get_next_id(items_list):
    if not items_list:
        return 1
    # Create a list of all the IDs from existing items and find the maximum ID.
    ids = [int(item['id']) for item in items_list]
    return max(ids) + 1

# This function displays a list of items with their index numbers.
# It also pauses execution until the user presses Enter to continue.
def list_items(items):
    clear_console()
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")
    

# This function is used to add a new item of a specific item_type (e.g., "product" or "courier").
# It collects information for each field in the item and assigns a unique ID.
# The new item is returned as a dictionary.
def add_item(item_type, fields, items_list):
    item = {}
    for field in fields:
        item[field] = input(f"Enter {item_type} {field}: ")
    item_id = get_next_id(items_list)
    item = {"id": str(item_id), **item}
    clear_console()
    return item

# This function allows updating the values of an item, except for the ID field.
# It displays the current values and prompts the user to enter new values.
def update_item(item, products, couriers, order_statuses):
    print("Update Item")
    for key, value in item.items():
        if key == 'id':  # Skip updating the ID field
            continue
        elif key == 'status':
            new_value = order_status(order_statuses)
            item[key] = new_value
            continue
        elif key == 'products':
            new_value = get_prod(products)
            item[key] = new_value
            continue
        elif key == 'courier':
            new_value = get_couriers(couriers)
            item[key] = new_value
            continue
        new_value = input(f"{key} ({value}): ")
        if new_value:
            item[key] = new_value
    clear_console()
        

# This function deletes an item from the items list based on its index.
# It checks if the provided index is within a valid range and removes the item.
def delete_item(items, index):
    if 0 <= index < len(items):
        items.pop(index)
        print("Item deleted successfully")
    else:
        print("Invalid index.")
    input("Press Enter to continue...")

def get_couriers(couriers):
    list_items(couriers)
    courier_index = int(input("Enter courier index: ")) - 1
    if 0 <= courier_index < len(couriers):
        
            courier_id = couriers[courier_index]['id']
            return courier_id
    else:
        print("Invalid courier index. ")
        # Exit the function to avoid adding an order with an invalid courier

def order_status(order_statuses):
    list_items(order_statuses)
    order_index = int(input("Enter order status index: ")) - 1
    if 0 <= order_index < len(order_statuses):

        #order_id = order_statuses[order_index]
        status = order_statuses[order_index]
        
        return status
    else:
        print("invalid courier index")

def get_prod(products):
    list_items(products)
    product_indexes = input("Enter indexes of products (for multiple products include comma): ")
    product_ids = [products[int(index) - 1]['id'] for index in product_indexes.split(',')]
    products_string = ",".join(product_ids)
    clear_console()
    return products_string



#index = int(input("Select the index value of the order status you'd like to update it to: "))
               # for i, status in enumerate(order_statuses, start=1):
               #         print(f"{i}. {status}")
                #status_index = int(input("Enter new status index: ")) - 1
                # if 0 <= status_index < len(order_statuses):
                #     orders[index]["status"] = order_statuses[status_index] # Update the status of the selected order in the order log
                   
                # else:
                #     print("Invalid index.")