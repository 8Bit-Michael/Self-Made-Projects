from colorama import init, Fore
init(autoreset=True)

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self, items):
        self.items = items
        self.order_list = []
        self.prices = []

    def print_items(self):
        try:
            user_choice = int(input("""Type in the number of the food you want to order:
1. Spaghetti - $12.99
2. Ravioli - $10.00
3. Pizza - $15.75
4. Fettucini Alfredo - $12.99
Choice: """))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            return self.print_items()

        if user_choice == 1:
            self.order_list.append("Spaghetti")
            self.prices.append(12.99)
        elif user_choice == 2:
            self.order_list.append("Ravioli")
            self.prices.append(10.00)
        elif user_choice == 3:
            self.order_list.append("Pizza")
            self.prices.append(15.75)
        elif user_choice == 4:
            self.order_list.append("Fettucini Alfredo")
            self.prices.append(12.99)
        else:
            print(Fore.RED + "Invalid choice.")
            return self.print_items()

        print(Fore.GREEN + f"{self.order_list[-1]} has been added to your order.")
        again = input("Add more items? Type yes or no: ").strip().lower()
        if again == 'yes':
            return self.print_items()
        elif again == 'no':
            print(Fore.YELLOW + "\nThank you for your order. Here is your receipt:")
            for item in self.order_list:
                print(f"- {item}")
            print(Fore.YELLOW + f"Total: ${sum(self.prices):.2f}")
        else:
            print(Fore.RED + "Invalid input.")
            return self.print_items()

class Restaurant:
    def __init__(self, menu):
        self.menu = menu

    def start(self):
        self.menu.print_items()

if __name__ == "__main__":
    items = [
        MenuItem("Spaghetti", 12.99),
        MenuItem("Ravioli", 10.00),
        MenuItem("Pizza", 15.75),
        MenuItem("Fettucini Alfredo", 12.99)
    ]
    menu = Menu(items)
    restaurant = Restaurant(menu)
    restaurant.start()