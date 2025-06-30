from colorama import init, Fore
from difflib import get_close_matches
import string
import time

init(autoreset=True)

def match_input(user_input, options, cutoff=0.6):
    return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)

class Player:
    def __init__(self, name, health, level, xp, inventory):
        self.name = name
        self.health = health
        self.level = level
        self.xp = xp
        self.inventory = inventory

    def attack(self, enemy, game):
        if enemy.is_alive():
            print(Fore.GREEN + f"You attack the {enemy.name}!")
            enemy.take_damage(5, self, game)
        else:
            print(Fore.RED + f"The {enemy.name} is already defeated.")
            game.player_actions(self)

    def heal(self, amount, game, player):
        while True:
            user_heal = input("Would you like to heal yourself? Type 'yes' or 'no': ")
            refined_user_heal = match_input(user_heal, ['yes', 'no'])
            if refined_user_heal and refined_user_heal[0] == 'yes':
                user_heal_amount = input("How many health points would you like to heal? Enter a number: ")
                try:
                    amount = int(user_heal_amount)
                    if self.health == 100:
                        print(Fore.RED + "You are already at full health!")
                        game.player_actions(self)
                    elif amount < 100:
                        self.health += amount
                        if self.health > 100:
                            self.health = 100
                        print(Fore.GREEN + f"You have healed. Your current health is now {self.health}.")
                        game.player_actions(self)
                    else:
                        print(Fore.RED + f"Sorry, you cannot heal by {user_heal_amount} points, as it exceeds your maximum health of 100.\n"
f"However, I will gladly heal you to full health, {player.name}!")
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a valid number.")
            elif refined_user_heal and refined_user_heal[0] == 'no':
                print(Fore.YELLOW + f"You chose not to heal. You have {self.health} HP left.")
                game.player_actions(self)
            else:
                print(Fore.RED + "Invalid input. Try again.")

class Enemy:
    def __init__(self, name, health, attack_power, xp_reward):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.xp_reward = xp_reward

    def attack(self, player, game):
        if player.health > 0:
            player.health -= self.attack_power
            print(Fore.RED + f"The {self.name} struck back! You lost {self.attack_power} HP.")
            game.player_actions(player)
            if player.health <= 0:
                print(Fore.RED + "You have been defeated. Game over!")
                exit()
        else:
            print(Fore.RED + f"It looks like you are too weak to continue, {player.name}, goodbye.")
            exit()

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage, player, game):
        self.health -= damage
        print(Fore.YELLOW + f"You dealt {damage} damage to the {self.name}.")
        if self.health <= 0:
            print(Fore.GREEN + f"You defeated the {self.name} and gained {self.xp_reward} XP!")
            player.xp += self.xp_reward
            game.player_actions(player)
        else:
            self.attack(player, game)

class Zombie(Enemy):
    def __init__(self, name="Zombie", health=15, attack_power=5, xp_reward=10):
        super().__init__(name, health, attack_power, xp_reward)

class Skeleton(Enemy):
    def __init__(self, name="Skeleton", health=10, attack_power=3, xp_reward=5):
        super().__init__(name, health, attack_power, xp_reward)

class Game:
    def start(self):
        start_choice = input("Would you like to start Runia? Type 'yes' or 'no': ")
        refined_start_choice = match_input(start_choice, ['yes', 'no'])

        if refined_start_choice and refined_start_choice[0] == 'yes':
            print(Fore.GREEN + "Starting Runia...")
            time.sleep(1)
            self.player_creation()
        elif refined_start_choice and refined_start_choice[0] == 'no':
            print(Fore.RED + "Thanks for checking out Runia!")
            exit()
        else:
            print(Fore.RED + f"'{start_choice}' is not valid.")
            self.start()

    def player_creation(self):
        while True:
            player_name = input("What is your name, hero? ")
            if player_name.isalpha():
                self.player = Player(name=player_name.capitalize(), health=100, level=1, xp=0, inventory=[])
                self.zombie = Zombie()
                self.skeleton = Skeleton()
                print(Fore.GREEN + f"Hmm... a wise name {self.player.name} is. Welcome to Runia!")
                self.player_actions(self.player)
                break
            else:
                print(Fore.RED + f"'{player_name}' is not a valid name.")

    def player_actions(self, player):
        choice = input(f"What would you like to do, {player.name}? 'attack', 'heal', or 'exit': ")
        refined_choice = match_input(choice, ['attack', 'heal', 'exit'])

        if refined_choice and refined_choice[0] == 'attack':
            enemy_choice = input("Which enemy would you like to attack? Type 'Zombie', 'Skeleton', or exit: ")
            refined_enemy = match_input(enemy_choice, ['zombie', 'skeleton'])
            if refined_enemy and refined_enemy[0] == 'zombie':
                player.attack(self.zombie, self)
            elif refined_enemy and refined_enemy[0] == 'skeleton':
                player.attack(self.skeleton, self)
            elif enemy_choice.lower() == 'exit':
                print("Exiting the game. Thanks for playing!")
                time.sleep(2)
                exit()
            else:
                print(Fore.RED + f"'{enemy_choice}' is not a valid enemy.")
                self.player_actions(player)

        elif refined_choice and refined_choice[0] == 'heal':
            player.heal(10, self, player)

        elif refined_choice and refined_choice[0] == 'exit':
            print(Fore.GREEN + "Thanks for playing Runia!")
            exit()
        else:
            print(Fore.RED + "Invalid choice.")
            self.player_actions(player)

if __name__ == '__main__':
    game = Game()
    game.start()
