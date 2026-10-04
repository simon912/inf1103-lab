import json

def load_inventory():
    inventory_array = []
    with open("inventory.json", "r") as file:
        print("Current Inventory")
        print("---------------------------")
        inventory_array = json.load(file)["Product"]
        for i in inventory_array:
            print(f"ID: {i['ID']} | Name: {i['Name']} | Price: ${i['Price']} | Stock: {i['Stock']}")
        print("---------------------------")
        return inventory_array
    
load_inventory()