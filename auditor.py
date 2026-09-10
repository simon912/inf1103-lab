inventory = 0
stock = 0
while True:
    stock = input("Enter stock quantity (type 'quit' to exit): ")
    if stock == "quit":
        print("Exiting...")
        break
    if not stock.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    stock = int(stock)

    if stock < 0:
        print("Stock quantity cannot be negative, please enter a valid number.")
        continue

    inventory += stock

    print("Stock Quantity Added:", stock)
    print("Current Inventory:", inventory)
    