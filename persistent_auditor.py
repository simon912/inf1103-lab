from hashlib import new

def get_next_id(inventory_array):
    highest_id = 1000
    for item in inventory_array:
            item_id = int(item[0])
            if item_id > highest_id:
                highest_id = item_id

    return highest_id + 1

def load_inventory():
        inventory_array = []
        with open("inventory.txt", "r") as file:
                for line in file:
                        if line.strip() == "":
                                continue
                        data = line.strip().split(",")
                        data = [item.strip() for item in data]
                        inventory_array.append(data)
        for item in inventory_array:
                print(f"{item[0]}, {item[1]}, {item[2]}")
        return inventory_array



#def process_delivery(current_total, new_value):
 #       current_total += new_value
 #       print("New Order Added:")
 #       print("Stock Quantity Added:", new_value)
 #       print("Current Inventory:", current_total)
 #       return current_total

#def calculate_tax(amount):
#        tax_rate = 10/100
#        amount = amount + (amount * tax_rate)
#        return amount

#def generate_report(total_units, failed_attempts):
#        print("Current Order:")
#        load_inventory()

def get_valid_input():
         print("Current Orders: ")
         current_inventory = load_inventory()
         stock = 0
         product_name = 0

         
         while True:
             product_name = input("Enter Product Name (type 'quit' to exit): ")
             if product_name == "quit":
                        break
             stock = input("Enter Quantity (type 'quit' to exit): ")
             if stock == "quit":
                        break
             if not stock.isdigit():
                                  print("Invalid input. Please enter a valid number.")
                                  continue
             stock = int(stock)
             if stock < 0:
                     print("Stock quantity cannot be negative, please enter a valid number.")
                     continue
             new_id = get_next_id(current_inventory)
             new_item = [int(new_id), product_name, str(stock)]
             current_inventory.append(new_item)
             print("New Order Added: ")
             
             print(f"{new_id}, {product_name}, {stock}")
        
             #inventory = process_delivery(inventory, stock)


# call function
get_valid_input()
