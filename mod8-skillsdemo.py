'''
Module 8

import the shop module. Write function calls to demonstrate the following:

Viewing the shop's inventory.
Buying at least 2 different items.
Restocking an item.
Viewing the updated shop's inventory.
While writing your function calls:

Trace the function calls back to the module, and describe how each function in the module works, emphasizing when dictionaries are being used to organize & retrieve data.
Test your code to demonstrate that it is functional.

Funcs: view_inventory(), buy_item(item_name, quantity), restock_item(item_name, quantity)
'''
import shop # bring the shop in view

shop.view_inventory() # Show shop inventory
shop.buy_item("Tomato Seeds", 7) # Buy tomato
shop.buy_item("Cabbage Seeds", 3) # Buy Cabbage

shop.restock_item("Tomato Seeds", 5) # Restock tomato
shop.view_inventory()# Update view of shop inventory
