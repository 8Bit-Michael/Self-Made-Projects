from colorama import init, Fore
from difflib import get_close_matches
import string

init(autoreset=True)

def match_input(user_input, options, cutoff=0.6):
    return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)

class Inventory:
    def __init__(self):
        self.products = {}

    def list_products(self):
        for product in self.products.values():
            print(Fore.GREEN + f"Product: {product.name} Price: ${product.price} Stock: {product.stock}")

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, product):
        self.products.pop(product.name, None)
        return Fore.RED + f"The product {product.name} has been removed."

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product: {self.name} Price: ${self.price} Stock: {self.stock}"

    def change_stock(self, amount):
        self.stock += amount

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        if product.stock > 0:
            self.items.append(product)
            product.change_stock(-1)
        else:
            print(Fore.RED + f"{product.name} is out of stock.")

    def remove_from_cart(self, product_name):
        for i, item in enumerate(self.items):
            if item.name == product_name:
                self.items.pop(i)
                item.change_stock(1)
                return
        raise ValueError(Fore.RED + f"{product_name} is not in your cart.")

    def view_cart(self):
        if not self.items:
            return "Cart is empty."
        word_count = len(self.items)
        return Fore.GREEN + f"The {word_count} items in your cart include the following:\n" + "\n".join(str(item) for item in self.items)

    def calculate_total(self):
        total = sum(p.price for p in self.items)
        return Fore.GREEN + f"Total: ${total:.2f}"

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

class Store:
    def __init__(self, inventory, users):
        self.inventory = inventory
        self.users = users

    def start(self):
        while True:
            user_role = input("Welcome to Tom's grocery store, are you an admin or a customer? (type 'exit' to quit) ").lower()
            if user_role == 'exit':
                print(Fore.YELLOW + "Thanks for visiting Tom's grocery store!")
                break

            role_match = match_input(user_role, ['admin', 'customer'])
            if role_match:
                role = role_match[0]
                if role == 'admin':
                    self.admin_actions()
                elif role == 'customer':
                    self.customer_actions()
            else:
                print(Fore.RED + f"Sorry, the role '{user_role}' wasn't recognized.")

    def admin_actions(self):
        admin_name = input("What is your name: ")
        name = admin_name.capitalize()
        admin_choice = input(f"""What would you like to do as an admin, {name}? 
Please type 'quantity' to set product amounts, 'product name' to rename items, or 'inventory' to change stock levels:\n""")
        action = match_input(admin_choice, ['quantity', 'product name', 'inventory'])

        if action and action[0] == 'quantity':
            product_input = input("Which product's quantity would you like to change: ")
            product_match = match_input(product_input, list(self.inventory.products.keys()))
            if product_match:
                product = self.inventory.products[product_match[0]]
                user_amount = input("How much would you like to add or remove? Type a number, like 8 or -19: ")
                try:
                    amount = int(user_amount)
                    product.change_stock(amount)
                    print(Fore.GREEN + f"Your update was successful! You now have {product.stock} of '{product.name}' in stock.")
                except ValueError:
                    print(Fore.RED + f"{user_amount} is not a valid number. You must type in a number, like 12.")
            else:
                print(Fore.RED + f"'{product_input}' isn't a valid option.")
        elif action and action[0] == 'product name':
            user_choice = input("What product do you want to rename? ")
            product_match = match_input(user_choice, list(self.inventory.products.keys()))
            if product_match:
                product = self.inventory.products[product_match[0]]
                new_name = input(f"What would you like to rename '{product.name}' to? ")
                if new_name.isdigit():
                    grammatic_new_name = string.capwords(new_name)
                    print(Fore.RED + f"Your new name for the product cannot be a digit. '{grammatic_new_name}' is invalid.")
                elif new_name in self.inventory.products:
                    print(Fore.RED + f"A product named '{new_name}' already exists.")
                else:
                    self.inventory.products.pop(product.name)
                    product.name = string.capwords(new_name)
                    self.inventory.products[product.name] = product
                    print(Fore.GREEN + f"You have now rebranded the product to '{product.name}'!")
            else:
                print(Fore.RED + f"The product '{user_choice}' doesn't seem to be in the grocery store, please try again.")
        elif action and action[0] == 'inventory':
            self.inventory.list_products()
        else:
            print(Fore.RED + f"'{admin_choice}' is an invalid choice.")

    def customer_actions(self):
        customer_name = input("What is your name: ")
        name = customer_name.capitalize()
        user = User(name)
        self.users.append(user)

        customer_choice = input(f"Would you like to add an item to your cart, {name}? Type yes or no: ")
        refined_customer_choice = match_input(customer_choice, ['yes', 'no'])

        if refined_customer_choice and refined_customer_choice[0] == 'yes':
            item_addition = input("What item would you like to add: ")
            refined_item_addition = match_input(item_addition, list(self.inventory.products.keys()))
            if refined_item_addition:
                product = self.inventory.products[refined_item_addition[0]]
                user.cart.add_to_cart(product)
                print(Fore.GREEN + f"{refined_item_addition[0]} has been added to your cart!")
            else:
                punctuated_item_addition = item_addition.capitalize()
                print(Fore.RED + f"'{punctuated_item_addition}' is not a valid option.")
                print(Fore.YELLOW + "Please try again.\n")
        elif refined_customer_choice and refined_customer_choice[0] == 'no':
            print(Fore.GREEN + "Okay! Let us know if you need anything.")
        else:
            print(Fore.RED + f"'{customer_choice}' is an invalid choice.")

if __name__ == '__main__':
    inventory = Inventory()
    prod_obj = Product("Frank's Sweet And Spicy Pizza", 1.00, 8)
    inventory.add_product(prod_obj)
    inventory.list_products()

    store = Store(inventory, [])
    store.start()
