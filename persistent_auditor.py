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

def save_inventory(inventory_array):
        with open("inventory.txt", "w") as file:
                for item in inventory_array:
                        file.write(f"{item[0]},{item[1]},{item[2]}\n")
        print("Order successfully added to inventory.txt")
                        
def get_valid_input():
         print("Current Orders: ")
         current_inventory = load_inventory()
         stock = 0
         product_name = 0

         
         while True:
             product_name = input("Enter Product Name (type 'quit' to exit): ")
             if product_name == "quit":
                        save_inventory(current_inventory)
                        break
             stock = input("Enter Quantity (type 'quit' to exit): ")
             if stock == "quit":
                        save_inventory(current_inventory)
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
             save_inventory(current_inventory)
             print("New Order Added: ")
             
             print(f"{new_id}, {product_name}, {stock}")

# call function
get_valid_input()
