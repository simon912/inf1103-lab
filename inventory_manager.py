import json
from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

class Product(ABC):
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
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")
        
    def to_dict(self) -> dict: 
        data = super().to_dict()
        data["Type"] = "Physical"
        data["Weight"] = self.__weight
        return data

    def get_fulfilment_info(self) -> str:
            return "This product requires physical shipping."
        
    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5.0 # $5 per kg

CanBeShipped.register(PhysicalProduct)
    
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, size: float):
        super().__init__(product_id, name, price, stock)
        self.__size = size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__size} MB")
        
    def to_dict(self) -> dict: 
        data = super().to_dict()
        data["Type"] = "Digital"
        data["Download_Size"] = self.__size
        return data
    
    def get_fulfilment_info(self) -> str:
            return "This product is delivered digitally"
        
        
class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product, show_message=True) -> None:
        self.__products.append(product)
        if show_message:
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
            print("1. Physical Product")
            print("2. Digital Product")
            product_type = input("Enter product type (1 or 2): ")
            product_id = input("Product ID: ")
            product_name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock Quantity: "))
            if product_type == "1":
                weight = float(input("Weight (kg): "))
                product = PhysicalProduct(product_id, product_name, price, stock, weight)
            elif product_type == "2":
                download_size = float(input("Download Size (MB): "))
                product = DigitalProduct(product_id, product_name, price, stock, download_size)
            else:
                print("Invalid product type. Product not added.")
                continue
            inventory.add_product(product, show_message=True)
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
            if "Weight" in item:
                product = PhysicalProduct(
                    item["ID"], item["Name"], item["Price"], item["Stock"], item["Weight"])
            elif "Download_Size" in item:
                product = DigitalProduct(
                    item["ID"], item["Name"], item["Price"], item["Stock"], item["Download_Size"])
            inventory.add_product(product, show_message=False)
        
        if show_message:
            print("inventory.json found.")
            print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("inventory.json not found.")
    return inventory
    

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
