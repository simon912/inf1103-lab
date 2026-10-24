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

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        print("Product added successfully!")

    def search_product(self, product_id: str):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self) -> None:
        print("Current Inventory")
        print("---------------------------------------------------------")

        for product in self.__products:
            product.display_information()

        print("---------------------------------------------------------\n")

    def update_stock(self, product_id: str, quantity: int) -> None:
        product = self.search_product(product_id)

        if product is not None:
            product.update_stock(quantity)
            print("Stock updated successfully!")
        else:
            print("Product Not Found.")

    def get_products(self) -> list:
        return self.__products

def menu():
    print("========================================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================================")
    inventory = load_inventory(True)
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
            inventory.display_all()
        elif option == "2":
            print("")
            print("Add New Product")

            product_id = input("Product ID: ")
            product_name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))

            product = Product(product_id, product_name, price, stock)
            inventory.add_product(product)
        elif option == "3":
            print("")
            product_id = input("Enter Product ID: ")
            new_stock = int(input("New Stock Quantity: "))
            inventory.update_stock(product_id, new_stock)

        elif option == "4":
            print("")
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)

            if product is not None:
                print("Product Found:")
                print("---------------------------------------------------------")
                product.display_information()
                print("---------------------------------------------------------")
            else:
                print("Product Not Found.")
        elif option == "5":
            print("")
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("")
            print("Thank you for using Inventory Management.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")

def load_inventory(show_message=False):
    inventory = Inventory()
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)["Product"]   
        
        for item in data:
            product = Product(
                item["ID"], item["Name"], item["Price"], item["Stock"])
            inventory.add_product(product)
        
        if show_message:
            print("inventory.json found.")
            print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory.json not found.")
        
    return inventory
    
def display_all(inventory):
    print("Current Inventory")
    print("---------------------------------------------------------")
    for product in inventory:
        product.display_information()
    print("---------------------------------------------------------\n")

def add_product(inventory):
    print("Add New Product")
    
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    
    new_product = Product(product_id, product_name, price, stock)
    inventory.append(new_product)
    print("")
    print("Product added successfully!")
    
def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ")
    
    for product in inventory:
        if product.get_product_id() == product_id:
            product.display_information()

            new_stock = int(input("New Stock Quantity: "))
            product.update_stock(new_stock)

            print("Stock updated successfully!")
            return

    print("Product Not Found.") 

def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ")
    
    for product in inventory:
        if product.get_product_id() == product_id:
            print("Product Found:")
            print("---------------------------------------------------------")
            product.display_information()
            print("---------------------------------------------------------")
            return

    print("Product Not Found.")
    
def save_inventory(inventory):
    data = {
        "Product": [
            product.to_dict()
            for product in inventory.get_products()
        ]
    }

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

menu()