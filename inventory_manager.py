import json

def menu():
    print("========================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================================")
    load_inventory(True)
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
            display_all()
        elif option == "2":
            print("")
            add_product()
        elif option == "6":
            print("Saving inventory before exit...")
            #insert save inventory function
            print("")
            print("Thank you for using Inventory Management.")
            print("Program terminated.")
            break

def load_inventory(show_message=False):
    inventory_array = []
    try:
        with open("inventory.json", "r") as file:
            inventory_array = json.load(file)["Product"]
        if show_message:
            print("inventory.json found.")
            print("Inventory loaded successfully.")
    except FileNotFoundError:
        print("inventory.json not found.")
        return None
    return inventory_array
    
def display_all():
    inventory_array = load_inventory(False)
    print("Current Inventory")
    print("---------------------------------------------------------")
    for i in inventory_array:
        print(f"ID: {i['ID']} | Name: {i['Name']} | Price: ${i['Price']} | Stock: {i['Stock']}")
    print("---------------------------------------------------------\n")

    
def add_product():
    print("Add New Product")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price:"))
    stock = int(input("Stock Quantity: "))
    inventory_array = load_inventory(False)
    new_product = {
        "ID": product_id,
        "Name": product_name,
        "Price": price,
        "Stock": stock
    }
    inventory_array.append(new_product)
    with open("inventory.json", "w") as file:
        json.dump({"Product": inventory_array}, file)
    print("")
    print("Product added successfully!")
    
menu()