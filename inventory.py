store = {
    "laptop": {"price": 1200, "quantity": 5},
    "Headphones": {"price": 150, "quantity": 10},
    "mouse": {"price": 40, "quantity": 20}
}

print("Initial store:")
print(store)

def add_product(store_dict, name, price, quantity):
    if name in store_dict:
        return "Product already exists."
    else:
        store_dict[name] = {"price": price, "quantity": quantity}
        return "Product added successfully."

def update_stock(store_dict, name, quantity):
    if name in store_dict:
        store_dict[name]["quantity"] = quantity
        return "Stock for updated."
    else:
        return "Product does not exist in the store."

def sell_product(store_dict, name, quantity):
    if name not in store_dict:
        return "Product does not exist."

    current_stock = store_dict[name]["quantity"]
    price = store_dict[name]["price"]

    if quantity > current_stock:
        return "Not enough stock"
    else:
        store_dict[name]["quantity"] -= quantity
        total_price = price * quantity
        return f"Sold {quantity} '{name}' for N{total_price:.2f}."

def display_inventory(store_dict):
    print("Current Inventory:")
    for name, details in store_dict.items():
        print(f"{name}: Price = N{details['price']}, Quantity = {details['quantity']}")

def sum_product(store):
    total = 0
    for product in store.values():
        total += product["price"] * product["quantity"]
    return total

   

def start():
    while True:
        print('''
        1. Add Product
        2. Update Product Stock
        3. Sell Product
        4. Display Inventory
	5. sum of product
        6. Exit
        ''')

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            result = add_product(store, name, price, quantity)
            print(result)

        elif user_choice == 2:
            name = input("Enter product name to update: ")
            quantity = int(input("Enter new quantity: "))
            result = update_stock(store, name, quantity)
            print(result)

        elif user_choice == 3:
            name = input("Enter product name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            result = sell_product(store, name, quantity)
            print(result)

        elif user_choice == 4:
            display_inventory(store)

        elif user_choice == 5:
            print(sum_product(store))

        elif user_choice == 6:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

start()

