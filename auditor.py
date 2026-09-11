inventory = 0
stock = 0
fail_entry = 0

while True:

    if inventory > 500:
            print("Inventory limit reached, cannot add more stock.")
            break
    
    stock = input("Enter stock quantity (type 'quit' to exit): ")
    
    if stock == "quit":
        print("Total Units Processed: ", inventory)
        print("Number of Rejected Entries:", fail_entry)
        break

    if not stock.isdigit():
        print("Invalid input. Please enter a valid number.")
        fail_entry += 1
        continue

    stock = int(stock)

    if stock < 0:
        print("Stock quantity cannot be negative, please enter a valid number.")
        fail_entry += 1
        continue

    inventory += stock
    
    print("Stock Quantity Added:", stock)
    print("Current Inventory:", inventory)
    