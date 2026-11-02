from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, size: float):
        super().__init__(product_id, name, price, stock)
        self.__size = size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.__size} MB")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["Type"] = "Digital"
        data["Download_Size"] = self.__size
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["ID"],
            data["Name"],
            data["Price"],
            data["Stock"],
            data["Download_Size"]
        )

    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."