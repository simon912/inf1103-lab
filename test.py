
from typing import get_type_hints

from product import Product, CanBeShipped
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from order_line import OrderLine


# Used to demonstrate polymorphism through Product references
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_supplier_product_association() -> None:
    print("\n1. Supplier and Product Association")

    supplier = Supplier("S001", "Tech Supplies Inc.", "tech@gmail.com")

    physical = PhysicalProduct(
        "P001", "Laptop", 1500.0, 10, 2.5, supplier
    )

    digital = DigitalProduct(
        "P002", "E-Book", 20.0, 50, 15.0, supplier
    )

    # Product stores a reference to Supplier
    assert physical.get_supplier_info() is supplier
    assert digital.get_supplier_info() is supplier

    # Supplier can exist independently
    independent_supplier = Supplier(
        "S002", "Digital Solutions", "digital@gmail.com"
    )

    assert independent_supplier is not None

    print("PASS: Products reference their Supplier.")
    print("PASS: Supplier can exist independently.")


def test_inventory_aggregation() -> tuple[PhysicalProduct, DigitalProduct]:
    print("\n2. Inventory Aggregation")

    supplier = Supplier("S003", "General Supplies", "general@gmail.com")

    physical = PhysicalProduct(
        "P003", "Keyboard", 80.0, 12, 0.8, supplier
    )

    digital = DigitalProduct(
        "P004", "Online Course", 40.0, 30, 500.0, supplier
    )

    inventory1 = Inventory()
    inventory2 = Inventory()

    inventory1.add_product(physical, show_message=False)
    inventory1.add_product(digital, show_message=False)

    assert inventory1.search_product("P003") is physical
    assert inventory1.search_product("P004") is digital

    print("PASS: Inventory stores different Product subclasses.")

    # Transfer Product between inventories
    inventory1.remove_product("P003")
    inventory2.add_product(physical, show_message=False)

    assert inventory1.search_product("P003") is None
    assert inventory2.search_product("P003") is physical

    print("PASS: Product can be transferred between inventories.")
    print("PASS: Product remains usable after removal.")

    return physical, digital


def test_order_relationships(
    physical: PhysicalProduct,
    digital: DigitalProduct
) -> None:

    print("\n3. Order and OrderLine Relationships")

    order = Order("O001")

    order.add_order_line(physical, 2)
    order.add_order_line(digital, 3)

    order_lines = order.get_order_lines()

    assert len(order_lines) == 2

    print("PASS: Order creates and manages OrderLine objects.")

    # Check that OrderLine references the original Products
    assert order_lines[0].get_product() is physical
    assert order_lines[1].get_product() is digital

    print("PASS: OrderLine references Product objects.")

    # Calculate total
    expected_total = (
        physical.get_price() * 2
        + digital.get_price() * 3
    )

    assert order.calculate_total() == expected_total

    print(f"Expected total: ${expected_total:.2f}")
    print(f"Calculated total: ${order.calculate_total():.2f}")

    print("PASS: Order calculates its total correctly.")

    # Remove OrderLine without removing Product
    order.remove_order_line("P003")

    assert physical.get_product_id() == "P003"
    assert physical.get_name() == "Keyboard"

    print("PASS: OrderLine was removed successfully.")
    print("PASS: Original Product still exists after OrderLine removal.")


def test_lsp_and_polymorphism(
    physical: PhysicalProduct,
    digital: DigitalProduct
) -> None:

    print("\n4. LSP and Polymorphism")

    # Both objects are stored as Product references
    products: list[Product] = [physical, digital]

    for product in products:
        show_product_details(product)
        print("--------------------------------")

    # Both subclasses preserve inherited Product behaviour
    physical.update_stock(8)
    digital.update_stock(45)

    assert physical.get_fulfilment_info() == (
        "This product requires physical shipping."
    )

    assert digital.get_fulfilment_info() == (
        "This product is delivered digitally."
    )

    print("PASS: Both subclasses support Product operations.")
    print("PASS: Polymorphic calls invoke the correct methods.")

    # Check CanBeShipped implementation
    assert isinstance(physical, CanBeShipped)
    assert physical.calculate_shipping_cost() >= 0

    print("PASS: PhysicalProduct implements CanBeShipped.")


def test_type_hints() -> None:
    print("\n5. Type Hint Verification")

    checks = [
        (Product.update_stock, {"quantity": int, "return": type(None)}),
        (Product.get_product_id, {"return": str}),
        (Product.get_name, {"return": str}),
        (Product.get_price, {"return": float}),
        (Product.get_fulfilment_info, {"return": str}),
        (Inventory.add_product, {"product": Product, "return": type(None)}),
        (Inventory.get_products, {"return": list[Product]}),
        (Order.add_order_line, {
            "product": Product,
            "quantity": int,
            "return": type(None)
        }),
        (Order.calculate_total, {"return": float}),
        (OrderLine.calculate_total, {"return": float}),
        (OrderLine.get_product, {"return": Product})
    ]

    for method, expected in checks:
        hints = get_type_hints(method)

        for name, expected_type in expected.items():
            actual = (
                hints.get("return")
                if name == "return"
                else hints.get(name)
            )

            assert actual == expected_type, (
                f"Type hint mismatch in {method.__qualname__}: {name}"
            )

        print(f"PASS: {method.__qualname__}")


def main() -> None:
    print("TESTING AND REVIEW")
    print("========================================")

    test_supplier_product_association()

    physical, digital = test_inventory_aggregation()

    test_order_relationships(physical, digital)

    test_lsp_and_polymorphism(physical, digital)

    test_type_hints()

    print("\n========================================")
    print("ALL TESTS PASSED!")


if __name__ == "__main__":
    main()
