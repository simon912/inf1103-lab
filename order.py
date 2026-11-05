from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.__order_lines:
            total += order_line.calculate_total()
        return total

    def remove_order_line(self, product_id: str) -> None:
        for order_line in self.__order_lines:
            if order_line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                print("Order line removed successfully!")
                return
        print("Order line not found.")

    def display_information(self) -> None:
        print(f"Order ID: {self.__order_id}")
        print("-------------------------------:")
        for order_line in self.__order_lines:
            order_line.display_information()
            print("-------------------------------:")
        print(f"Total Order Cost: ${self.calculate_total():.2f}")
        
    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines