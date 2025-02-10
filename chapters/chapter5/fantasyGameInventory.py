# Fantasy Game Inventory

# You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

# Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

# Hint: You can use a for loop to loop through all the keys in a dictionary.

# # inventory.py
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         # FILL THIS PART IN
#     print("Total number of items: " + str(item_total))

# displayInventory(stuff)

## PseudoCode
# DEFINE function displayInventory(inventory):
#     PRINT "Inventory:"  # Print header

#     SET item_total to 0  # Initialize a counter for total items

#     FOR each key-value pair (item, count) in inventory:
#         PRINT count and item name  # Print quantity followed by item name
#         ADD count to item_total  # Update total count

#     PRINT "Total number of items: " + item_total  # Print total count


# Inventory dictionary
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Function to display inventory
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0  # Initialize total count
    
    for item, count in inventory.items():  # Loop through dictionary
        print(f"{count} {item}")  # Print quantity + item name
        item_total += count  # Add count to total

    print(f"Total number of items: {item_total}")  # Print total count

# Call the function with the inventory dictionary
displayInventory(stuff)
