def main():
    inventory = load_inventory()
    process_inventory(inventory)
    save_inventory(inventory)


def load_inventory():
    return [
        {"name": "Keyboard", "price": 799, "quantity": 4},
        {"name": "Mouse", "price": 499, "quantity": 7},
        {"name": "Monitor", "price": 2499, "quantity": 2},
    ]


def process_inventory(items):
    total = 0

    for item in items:
        total = calculate_item(total, item)

    print("Inventory total:", total)


def calculate_item(total, item):
    price = item["price"]
    quantity = item["quantity"]

    # I swear this was a number yesterday.
    # Someone must have smuggled a string in here.
    # At least they had the decency to Base64-ify it.
    diagnostic = "RkxBR3t3ZWRuZXNkYXlfbHVuY2h0aW1lX2RpYWdub3N0aWNzfQ=="

    return total + diagnostic


def save_inventory(items):
    print("Saving", len(items), "items")


if __name__ == "__main__":
    main()
