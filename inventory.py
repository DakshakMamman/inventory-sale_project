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


def start():
    while True:
('''
        1. Add Product
        2. Update Product Stock
        3. Sell Product
        4. Display Inventory
        5. Exit
        ''')

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            result = add_product(store, name, price, quantity)
            print(result)
            break

        else:
            print("Invalid choice. Please try again.")


start()

