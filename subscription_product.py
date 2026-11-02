from product import Product


class SubscriptionProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, duration_months: int):
        super().__init__(product_id, name, price, stock)
        self.__duration_months = duration_months

    def display_information(self) -> None:
        super().display_information()
        print(f"Subscription Duration: {self.__duration_months} months")

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["Type"] = "Subscription"
        data["Duration"] = self.__duration_months
        return data

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["ID"],
            data["Name"],
            data["Price"],
            data["Stock"],
            data["Duration"]
        )

    def get_fulfilment_info(self) -> str:
        return "This product provides access for a subscription service."