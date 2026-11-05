class Supplier():
    def __init__(self, supplier_id: str, name: str, contact_email: str):
            self.__supplier_id = supplier_id
            self.__name = name
            self.__contact_email = contact_email
            
    def display_information(self) -> None:  
        print(f"Supplier ID: {self.__supplier_id} | Name: {self.__name} | Contact Email: {self.__contact_email}")

    def supplier_id(self) -> str:
        return self.__supplier_id

    def name(self) -> str:
        return self.__name
    
    def contact_email(self) -> str:
        return self.__contact_email
    
    def to_dict(self) -> dict:
        return {
            "Supplier_ID": self.__supplier_id,
            "Name": self.__name,
            "Contact_Email": self.__contact_email
        }
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["Supplier_ID"],
            data["Name"],
            data["Contact_Email"]
        )   