from colorama import init, Fore
from difflib import get_close_matches
import time

init(autoreset=True)

def match_input(user_input, options, cutoff=0.6):
    return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)

class User:
    def __init__(self, login, past_orders, personal_information):
        self.login = login
        self.past_orders = past_orders
        self.personal_information = personal_information

class Product:
    def __init__(self, name, description, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description

    def change_stock(self, amount, name):
        user_change = input("What would you like to add or subtract to your stock? Type a number like 10 or -3: ")
        try:
            user_change = int(user_change)
            new_balance = amount + user_change
            if new_balance > 0:
                print(Fore.GREEN + f"You now have a stock of {new_balance} {name}s!")
            else:
                print(Fore.RED + "Sorry, you cannot get rid of more items than you have in your stock.")
        except ValueError:
            print(Fore.RED + f"{user_change} is not a valid stock, you must type in a number.")

class CartItem:
    def __init__(self, quantity, product):
        self.product = product
        self.quantity = quantity

    def update_quantity(self, product, quantity):
        change_option = input(f"Would you like to add or subtract {product.name}s to your cart? Type 'add' or 'subtract': ")
        refined_change_option = match_input(change_option, ['add', 'subtract'])

        if refined_change_option and refined_change_option[0] == 'add':
            addition_amount = input("How much would you like to add to your stock? Please type a number like 12 or 4: ")
            try:
                addition_amount = int(addition_amount)
                if addition_amount <= 0:
                    print(Fore.RED + f"Sorry, your number must be above zero, {addition_amount} is invalid.")
                    self.update_quantity(product, quantity)
                elif quantity + addition_amount <= 0:
                    self.handle_invalid_add(product, quantity)
                else:
                    print(Fore.GREEN + f"{addition_amount} {product.name}s added!")
            except ValueError:
                print(Fore.RED + f"Sorry, '{addition_amount}' isn't valid. Restarting function...")
                time.sleep(2)
                self.update_quantity(product, quantity)

        elif refined_change_option and refined_change_option[0] == 'subtract':
            subtraction_amount = input(f"How many {product.name}s would you like to get rid of? Please type a number like -12 or -4: ")
            try:
                subtraction_amount = int(subtraction_amount)
                if subtraction_amount >= 0:
                    print(Fore.RED + "Sorry your number needs to be negative, please try again.")
                    self.update_quantity(product, quantity)
                elif quantity + subtraction_amount >= 0:
                    print(Fore.GREEN + f"{-subtraction_amount} {product.name}s removed!")
                else:
                    print(Fore.RED + f"Sorry, not enough {product.name}s in stock to remove that many.")
                    self.update_quantity(product, quantity)
            except ValueError:
                print(Fore.RED + f"Sorry, '{subtraction_amount}' isn't valid. Restarting function...")
                time.sleep(2)
                self.update_quantity(product, quantity)
        else:
            print(Fore.RED + f"Sorry, '{change_option}' is not a valid input.")

    def handle_invalid_add(self, product, quantity):
        response = input(Fore.RED + f"That would make the stock of {product.name}s negative. Would you like to switch to subtracting instead? Type 'yes' or 'no': ")
        refined = match_input(response, ['yes', 'no'])
        if refined and refined[0] == 'yes':
            self.update_quantity(product, quantity)
        else:
            print("Okay, restarting.")
            time.sleep(1)
            self.update_quantity(product, quantity)

class Cart:
    def __init__(self, cart_items=None):
        self.cart_items = cart_items if cart_items else []

    def add_item(self, product, quantity):
        if product is None:
            new_item_name = input("Enter a product name to add: ")
            new_item_amount = input(f"How many {new_item_name}s? ")
            try:
                amount = int(new_item_amount)
                if amount > 0:
                    new_product = Product(new_item_name, "", 0.0, amount)
                    self.cart_items.append(CartItem(amount, new_product))
                    print(Fore.GREEN + f"Added {amount} {new_item_name}s to cart.")
                else:
                    print(Fore.RED + "Amount must be positive.")
            except ValueError:
                print(Fore.RED + f"{new_item_amount} is not valid.")
        else:
            if product.stock > 0:
                self.cart_items.append(CartItem(quantity, product))
                product.stock -= quantity
                print(Fore.GREEN + f"Added {quantity} {product.name}s to your cart.")
            else:
                print(Fore.RED + f"Sorry, {product.name}s are out of stock.")

    def remove_item(self, product):
        item = next((ci for ci in self.cart_items if ci.product == product), None)
        if not item:
            print(Fore.RED + f"{product.name} not found in your cart.")
        else:
            self.cart_items.remove(item)
            product.stock += item.quantity
            print(Fore.GREEN + f"Removed {product.name} from cart.")

    def calculate_total(self):
        total = sum(item.quantity * item.product.price for item in self.cart_items)
        print(Fore.GREEN + f"Total: ${total:.2f}")

class Order:
    def __init__(self, snapshot, total, status):
        self.snapshot = snapshot
        self.total = total
        self.status = status
