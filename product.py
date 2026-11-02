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