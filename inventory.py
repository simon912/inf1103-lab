import json

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct

PRODUCT_TYPES = {
    "Physical": PhysicalProduct,
    "Digital": DigitalProduct,
    "Subscription": SubscriptionProduct
}


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product, show_message=True) -> None:
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
            product.display_supplier_information()

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


def load_inventory(show_message=False):
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)["Product"]

        for item in data:
            product_class = PRODUCT_TYPES[item["Type"]]
            product = product_class.from_dict(item)
            inventory.add_product(product, show_message=False)

        if show_message:
            print("inventory.json found.")
            print("Inventory loaded successfully.")

    except FileNotFoundError:
        if show_message:
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