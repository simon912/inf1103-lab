

def process_delivery(current_total, new_value):
        current_total += new_value
        print("Stock Quantity Added:", new_value)
        print("Current Inventory:", current_total)
        return current_total

def calculate_tax(amount):
        tax_rate = 10/100
        amount = amount + (amount * tax_rate)
        return amount

def generate_report(total_units, failed_attempts):
        print("Total Units Processed: ", total_units)
        print("Number of Rejected Entries:", failed_attempts)
        print("Total Units Processed after Tax: ", calculate_tax(total_units))

def get_valid_input():
         fail_entry = 0
         inventory = 0
         stock = 0
         while True:
             stock = input("Enter stock quantity (type 'quit' to exit): ")
             if stock == "quit":
                                  generate_report(inventory, fail_entry)
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
             
             if inventory + stock > 500:
                print("Inventory limit reached, cannot add more stock.")
                break
        
             inventory = process_delivery(inventory, stock)




# call function
get_valid_input()
