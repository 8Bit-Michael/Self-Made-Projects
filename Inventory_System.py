from colorama import init, Fore
init(autoreset=True)

max = 4
inventory = ['Sword', 'Shield', 'Potion', 'Bag']

def add_item(item):
    global inventory
    if len(inventory) == max:
        new_capacity = max * 2
        updated_inventory = []

        for old_item in inventory:
            updated_inventory.append(old_item)

        updated_inventory.append(item)
        inventory = updated_inventory

        print(Fore.GREEN + f"{item} has been added successfully! Your new inventory includes: {', '.join(inventory)}")

add_item('Coins')
