from product import Product, CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["Type"] = "Physical"
        data["Weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data: dict) -> 'PhysicalProduct':
        return cls(
            data["ID"],
            data["Name"],
            data["Price"],
            data["Stock"],
            data["Weight"],
            Supplier.from_dict(data["Supplier"])
        )

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5.0