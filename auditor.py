inventory = 0
stock = 0
while True:
    stock = input("Enter stock quantity (type 'quit' to exit): ")
    if stock == "quit":
        print("Exiting...")
        break
    stock = int(stock)
    print("Stock Quantity:", stock)
    