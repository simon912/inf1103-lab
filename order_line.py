from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    def calculate_total(self) -> float:
        return self.__product.get_price() * self.__quantity
    
    def display_information(self) -> None:
        print(f"Product: {self.__product.get_name()} | Quantity: {self.__quantity} | Total: ${self.calculate_total()}")