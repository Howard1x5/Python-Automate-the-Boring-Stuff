import pyinputplus as pyip

# Prices for each ingredient
prices = {
    "bread": {"wheat": 1.50, "white": 1.00, "sourdough": 2.00},
    "protein": {"chicken": 3.00, "turkey": 3.50, "ham": 3.00, "tofu": 2.50},
    "cheese": {"cheddar": 1.00, "swiss": 1.25, "mozzarella": 1.50},
    "extras": {"mayo": 0.25, "mustard": 0.20, "lettuce": 0.50, "tomato": 0.75},
}

# Get user's sandwich order
print("\nWelcome to the Sandwich Maker!")

# Choose bread type
bread = pyip.inputMenu(["wheat", "white", "sourdough"], prompt="Choose your bread type:\n", numbered=True)

# Choose protein type
protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt="Choose your protein type:\n", numbered=True)

# Ask if they want cheese
want_cheese = pyip.inputYesNo("Do you want cheese? (yes/no)\n")

# If yes, choose cheese type
cheese = None
if want_cheese == "yes":
    cheese = pyip.inputMenu(["cheddar", "swiss", "mozzarella"], prompt="Choose your cheese type:\n", numbered=True)

# Ask about additional toppings
extras = []
for extra in ["mayo", "mustard", "lettuce", "tomato"]:
    if pyip.inputYesNo(f"Do you want {extra}? (yes/no)\n") == "yes":
        extras.append(extra)

# Ask how many sandwiches
num_sandwiches = pyip.inputInt("How many sandwiches would you like? (1 or more)\n", min=1)

# Calculate total price
total_price = (prices["bread"][bread] + prices["protein"][protein]) * num_sandwiches

# Add cheese price if chosen
if cheese:
    total_price += prices["cheese"][cheese] * num_sandwiches

# Add extra toppings price if chosen
for extra in extras:
    total_price += prices["extras"][extra] * num_sandwiches

# Display Order Summary
print("\nOrder Summary:")
print(f"Bread: {bread.capitalize()}")
print(f"Protein: {protein.capitalize()}")
if cheese:
    print(f"Cheese: {cheese.capitalize()}")
if extras:
    print(f"Extras: {', '.join([e.capitalize() for e in extras])}")
print(f"Quantity: {num_sandwiches}")
print(f"Total Price: ${total_price:.2f}")

print("\nThank you for your order! Enjoy your sandwich!")
