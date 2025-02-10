# This function adds items from a list to an existing inventory dictionary.

#     Input:
#         inventory: A dictionary where keys are item names and values are item counts.
#         addedItems: A list of loot items that need to be merged into the inventory.

#     Output:
#         A modified dictionary with the updated item counts.
#         If an item from addedItems already exists in inventory, increase its count.
#         If an item does not exist, add it with an initial count.

## Pseudocode

# DEFINE function addToInventory(inventory, addedItems):
#     FOR each item in addedItems:
#         IF item exists in inventory:
#             INCREMENT inventory[item] by 1
#         ELSE:
#             ADD item to inventory with count 1
#     RETURN updated inventory

def addToInventory(inventory, addedItems):
    for item in addedItems:  # Loop through the loot list
        if item in inventory:
            inventory[item] += 1  # If item exists, increment count
        else:
            inventory[item] = 1  # If new item, set count to 1
    return inventory  # Return updated inventory dictionary

# Example usage:
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)  # Update inventory

# Display the inventory using the function from the previous exercise
displayInventory(inv)

