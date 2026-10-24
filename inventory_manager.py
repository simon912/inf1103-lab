import json

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    def display_information(self) -> None:
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")
        
    def get_product_id(self) -> str:
        return self.__product_id
    
    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price
    
    def to_dict(self) -> dict:
        return {
        "ID": self.__product_id,
        "Name": self.__name,
        "Price": self.__price,
        "Stock": self.__stock
    }

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
            data = json.load(file)["Product"]
        inventory_array = []    
        
        for item in data:
            product = Product(
                item["ID"], item["Name"], item["Price"], item["Stock"])
            inventory_array.append(product)
        
        if show_message:
            print("inventory.json found.")
            print("Inventory loaded successfully.")
        
        return inventory_array

    except FileNotFoundError:
        print("inventory.json not found.")
        return None
    
def display_all(inventory_array):
    print("Current Inventory")
    print("---------------------------------------------------------")
    for product in inventory_array:
        product.display_information()
    print("---------------------------------------------------------\n")

def add_product(inventory_array):
    print("Add New Product")
    
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    
    new_product = Product(product_id, product_name, price, stock)
    inventory_array.append(new_product)
    print("")
    print("Product added successfully!")
    
def update_stock(inventory_array):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    
    for product in inventory_array:
        if product.get_product_id() == product_id:
            product.display_information()

            new_stock = int(input("New Stock Quantity: "))
            product.update_stock(new_stock)

            print("Stock updated successfully!")
            return

    print("Product Not Found.") 

def search_product(inventory_array):
    print("Search Product")
    product_id = input("Enter Product ID: ")
    
    for product in inventory_array:
        if product.get_product_id() == product_id:
            print("Product Found:")
            print("---------------------------------------------------------")
            product.display_information()
            print("---------------------------------------------------------")
            return

    print("Product Not Found.")
    
def save_inventory(inventory_array):
    data = {
        "Product": [product.to_dict() for product in inventory_array]
    }

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)
        
menu()