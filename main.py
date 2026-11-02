from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from subscription_product import SubscriptionProduct

from inventory import Inventory, load_inventory, save_inventory


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
        option = input("Enter option: ")

        if option == "1":
            print("")
            inventory.display_all()

        elif option == "2":
            print("")
            print("Add New Product")
            print("1. Physical Product")
            print("2. Digital Product")
            print("3. Subscription Product")

            product_type = input("Enter product type (1, 2, or 3): ")

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

            elif product_type == "3":
                duration_months = int(input("Subscription Duration (months): "))
                product = SubscriptionProduct(product_id, product_name, price, stock, duration_months)

            else:
                print("Invalid product type. Product not added.")
                continue

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


if __name__ == "__main__":
    menu()