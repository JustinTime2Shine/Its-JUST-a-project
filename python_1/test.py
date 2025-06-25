"""
Simple Shopping Cart System
---------------------------
This Python script simulates a basic shopping cart for a fruit store. Users can:
- View available items and prices
- Add items to their cart
- View the contents of their cart
- Checkout and see the total cost

It demonstrates use of variables, lists, dictionaries, functions, loops, conditionals, and documentation.
"""

# List of available items in the store
store_items = ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]

# Prices for each item (dictionary)
item_prices = {
    "Apple": 1,
    "Banana": 0.5,
    "Orange": 0.75,
    "Grapes": 2,
    "Watermelon": 3
}

# User's shopping cart (list)
cart = []

def display_cart(cart_list):
    """
    Prints the current contents of the shopping cart.
    
    Parameters:
        cart_list (list): A list of items currently in the user's shopping cart.
        
    Returns:
        None
    """
    if not cart_list:
        print("Your shopping cart is currently empty.")
    else:
        print("\nItems in your cart:")
        for item in cart_list:
            print(f"- {item}")
    print()  # blank line for readability


# Greet the user and display store items
print("Welcome to the Fruit Store!")
print("Here are the available items:")

# Show available items with prices
for item in store_items:
    print(f"{item}: ${item_prices[item]}")

# Begin main loop for shopping interaction
while True:
    print("\nWhat would you like to do?")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Checkout and quit")

    # Get user's input
    choice = input("Enter 1, 2, or 3: ")

    # Handle user input using decision structures
    if choice == "1":
        item_to_add = input("Enter the name of the item to add: ").title()
        if item_to_add in store_items:
            cart.append(item_to_add)
            print(f"{item_to_add} has been added to your cart.")
        else:
            print("Sorry, that item is not available.")
    elif choice == "2":
        display_cart(cart)
    elif choice == "3":
        print("\nChecking out...")
        display_cart(cart)

        total = 0
        for item in cart:
            total += item_prices[item]
        
        print(f"Total amount due: ${total:.2f}")
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please try again.")
