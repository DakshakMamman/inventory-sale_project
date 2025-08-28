Assignment: Online Store Inventory & Sales System
Create a Python program to manage an online store’s products, track inventory, process sales, and generate reports. 
Data structure(Sample)




Functions to Implement
add_product(store_dict, name, price, quantity)
Add a new product with the given price and quantity.
Return a success message if added, or a message if the product already exists.


update_stock(store_dict, name, quantity)
Update the stock of an existing product.
Return a success message if updated, or an error message if the product does not exist.


sell_product(store_dict, name, quantity)
Process a sale for the given product and quantity.
If enough stock exists, reduce the quantity and return the total sale price.
If stock is insufficient or product does not exist, return an appropriate error message.


display_inventory(store_dict)
Print all products with their prices and remaining quantity.
Return the total number of products displayed.


most_expensive_product(store_dict)
Find and return the product with the highest price along with its price.

total_potential_sales(store_dict)
Calculate the total value of all remaining stock  and return it.


