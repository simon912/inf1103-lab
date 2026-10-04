import json

def menu():
    print("========================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================================")
    inventory_array = load_inventory(True)
    print("------------------------- MENU -------------------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------------------------------\n")
    while True:
        option = input ("Enter option: ")
        if option == "1":
            print("")
            display_all(inventory_array)
        elif option == "2":
            print("")
            add_product(inventory_array)
        elif option == "3":
            print("")
            update_stock(inventory_array)
        elif option == "4":
            print("")
            search_product(inventory_array)
        elif option == "5":
            print("")
            print("Saving inventory...")
            save_inventory(inventory_array)
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory_array)
            print("")
            print("Thank you for using Inventory Management.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")

def load_inventory(show_message=False):
    try:
        with open("inventory.json", "r") as file:
            inventory_array = json.load(file)["Product"]
        if show_message:
            print("inventory.json found.")
            print("Inventory loaded successfully.")
        return inventory_array
    except FileNotFoundError:
        print("inventory.json not found.")
        return None
    return inventory_array
    
def display_all(inventory_array):
    print("Current Inventory")
    print("---------------------------------------------------------")
    for i in inventory_array:
        print(f"ID: {i['ID']} | Name: {i['Name']} | Price: ${i['Price']} | Stock: {i['Stock']}")
    print("---------------------------------------------------------\n")

def add_product(inventory_array):
    print("Add New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    new_product = {
        "ID": product_id,
        "Name": product_name,
        "Price": price,
        "Stock": stock
    }
    inventory_array.append(new_product)
    print("")
    print("Product added successfully!")
    
def update_stock(inventory_array):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    for product in inventory_array:
        if product["ID"] == product_id:
            print("Product Found:")
            print(f"Name: {product['Name']}")
            print(f"Current Stock: {product['Stock']}")
            new_stock = int(input("New Stock Quantity: "))
            product["Stock"] = new_stock
            print("Stock updated successfully!")
            return
    print("Product Not Found.") 

def search_product(inventory_array):
    print("Search Product")
    product_id = input("Enter Product ID: ")
    for product in inventory_array:
        if product["ID"] == product_id:
            print("Product Found:")
            print("---------------------------------------------------------")
            print(f"Name: {product['Name']}")
            print(f"Price: ${product['Price']}")
            print(f"Stock: {product['Stock']}")
            print("---------------------------------------------------------")
            return
    print("Product Not Found.")
    
def save_inventory(inventory_array):
    with open("inventory.json", "w") as file: 
        json.dump( {"Product": inventory_array}, file, indent=4 ) 
        print("Inventory saved successfully to inventory.json.")

menu()