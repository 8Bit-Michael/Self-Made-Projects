from colorama import init, Fore
from difflib import get_close_matches
from datetime import datetime

init(autoreset=True)

# This is the parent class with the basic functions:
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(Fore.GREEN + f"${amount} have been deposited into your account.")
        else:
            print(Fore.RED + "Your input is invalid. You can't deposit a negative amount.")

        def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(Fore.RED + f"${amount} have been withdrawn from your account.")
                return True
            else:
                print(Fore.RED + f"${amount} cannot be withdrawn from your account.")
                return False

    def check_balance(self):
        print(Fore.GREEN + f"Your account's balance is: ${self.balance}")

class CheckingAccount(BankAccount):
    def overdrafts(self):
        # This code sends messages to the user if their account is overdrawn and some possible
        # options to fix it, like depositing more money.
        if self.balance < 0:
            raw_user_overdraft = input(Fore.RED + """Your account is overdrawn, would you like to deposit
some money to fix this? Type 'yes' or 'no': """).strip().lower()

            # There's no need to add .replace() multiple times here, the get_close_matches does that more cleanly.
            user_overdraft = get_close_matches(raw_user_overdraft, ["checking", "saving"], n=1, cutoff=0.6)

            if user_overdraft:
                if user_overdraft[0] == "yes":
                    amount = input("How much money would you like to deposit: ").strip()
                    try:
                        amount = int(amount)
                        if amount > 0:
                            self.deposit(amount)
                        else:
                            print(Fore.RED + "You can't deposit a negative amount.")
                    except ValueError:
                        print(Fore.RED + f"{amount} is not a valid amount. Please try again.")
                        return self.overdrafts()

                elif user_overdraft[0] == "no":
                    if self.balance < -1000:
                        print(Fore.RED + """Your account is overdrawn by more than $1000, you cannot keep withdrawing money,
                You must deposit money to fix this.""")
                        user_fix = input("How much would you like to deposit: ").strip()
                        if user_fix.isdigit():
                            user_fix = int(user_fix)
                            if user_fix > abs(self.balance):
                                self.deposit(user_fix)
                                print(Fore.GREEN + f"You have deposited ${user_fix} to your account.")
                            elif user_fix < abs(self.balance):
                                shortfall = abs(self.balance) - user_fix
                                print(Fore.RED + f"That is not enough money to fix your account, you need to deposit ${shortfall} more dollars to fix it.")
                            else:
                                print(Fore.GREEN + "You have deposited the exact amount needed to fix your account.")
                        else:
                            print(Fore.RED + f"{user_fix} is not a valid amount. Please try again.")
                            return self.overdrafts()
                    else:
                        print(Fore.RED + "Okay, your account will remain overdrawn.")
            else:
                print(Fore.RED + f"{raw_user_overdraft} is not a valid input. Please try again.")
                return self.overdrafts()

    # This function here is to add a fee to the account when the balance becomes negative,
    # making it more simple than the overdrafts function.
    def fee(self):
        if self.balance < 0:
            fee_amount = 35
            print(Fore.RED + f"Please note that a fee of ${fee_amount} will be charged to your account for being overdrawn.")
            self.balance -= fee_amount
            print(Fore.RED + f"Your new balance is ${self.balance}.")
        else:
            print(Fore.GREEN + "You're account isn't overdrawn, so you have no fees to pay.")
            

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.withdrawal_dates = []  

    def limit_with_drawals(self):
        now = datetime.now()
        withdrawals_this_month = [
            date for date in self.withdrawal_dates
            if date.year == now.year and date.month == now.month
        ]

        withdrawal_count = len(withdrawals_this_month)

        user_withdraw = input("Would you like to withdraw money? Please type 'yes' or 'no': ").strip().lower()
        matches = get_close_matches(user_withdraw, ['yes', 'no'], n=1, cutoff=0.6)
        
        if matches and matches[0] == 'yes':
            if withdrawal_count < 3:
                try:
                    amount = int(input("How much do you want to withdraw: ").strip())
                    if amount > 0:
                        if amount <= self.balance:
                            self.withdraw(amount) 
                            self.withdrawal_dates.append(now)  
                        else:
                            print(Fore.RED + "You do not have enough balance for this withdrawal.")
                    else:
                        print(Fore.RED + "You can't withdraw a negative amount or zero.")
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a valid number.")
                    return self.limit_with_drawals()
            else:
                print(Fore.RED + "You have already withdrawn money 3 times this month. No further withdrawals allowed.")
        elif matches and matches[0] == 'no':
            print("No withdrawal will be made.")
        else:
            print(Fore.RED + f"{user_withdraw} is not a valid input. Please try again.")
            return self.limit_with_drawals()

    def interest(self, rate):
        if rate > 0:
            interest_amount = self.balance * (rate / 100)
            self.balance += interest_amount
            print(Fore.GREEN + f"An interest of ${interest_amount:.2f} has been added to your account.")
        else:
            print(Fore.RED + "The interest rate must be a positive number.")
            return self.interest(float(input("Please enter a valid interest rate: ").strip()))

account_selection = input("""
Welcome to my bank simulation! Would you like to create a Checking or Savings account? Type 'Checking' or 'Savings': """).strip().lower()
refined_selection = get_close_matches(account_selection, ['checking', 'savings'], n=1, cutoff=0.6)
# This is what happens if the user chooses a checking account:
if refined_selection and refined_selection[0] == 'checking':
    account_number = input("Please enter your account number: ").strip()
    owner_name = input("Please enter your name: ").strip()
    
    if not owner_name or owner_name.isdigit():
        print(Fore.RED + "Your name must include letters and cannot be a number. Please try again.")
        exit()
    else:
        print(Fore.GREEN + f"Welcome {owner_name}, your account number is {account_number}.")
    checking_account = CheckingAccount(account_number, owner_name)
    
    while True:
        checking_choice = input("What would you like to do on your account? You can enter 'deposit', 'withdraw', 'check balance', 'overdrafts', 'pay fees', or 'exit': ")
        checking_choice = checking_choice.replace(" ", "").lower()
        
        match = get_close_matches(checking_choice, ['deposit', 'withdraw', 'checkbalance', 'overdrafts', 'payfees', 'exit'], n=1, cutoff=0.6)

        if match:
            if match[0] == 'deposit':
                amount = input("How much would you like to deposit: ").strip()
                if amount.isdigit():
                    checking_account.deposit(int(amount))
                else:
                    print(Fore.RED + f"{amount} is not a valid amount. Please try again.")
            elif match[0] == 'withdraw':
                amount = input("How much would you like to withdraw: ").strip()
                if amount.isdigit():
                    success = checking_account.withdraw(int(amount))
                    if success:
                        checking_account.fee()
                else:
                    print(Fore.RED + f"{amount} is not a valid amount. Please try again.")
            elif match[0] == 'checkbalance':
                checking_account.check_balance()
            elif match[0] == 'overdrafts':
                checking_account.overdrafts()
            elif match[0] == 'payfees':
                checking_account.fee()
            elif match[0] == 'exit':
                print("Thanks for using my bank simulation, bye!")
                break
        else:
            print(Fore.RED + f"'{checking_choice}' is an invalid choice, please try again.")
# This is what happens if the user chooses a savings account:
elif refined_selection and refined_selection[0] == 'savings':
    account_number = input("Please enter your account number: ").strip()
    owner_name = input("Please enter your name: ").strip()
    if not owner_name or owner_name.isdigit():
        print(Fore.RED + "Your name must include letters and cannot be a number. Please try again.")
        exit()
    else:
        print(Fore.GREEN + f"Welcome {owner_name}, your account number is {account_number}.")
    savings_account = SavingsAccount(account_number, owner_name)
    
    while True:
        savings_choice = input("""What would you like to do on your account? Keep in mind you can type in 
'deposit', 'withdraw', 'check balance', 'interest', 'limit withdrawals', 
and 'exit' once your done with the program: """).strip().lower()
        refined_savings_choice = get_close_matches(savings_choice, ['deposit', 'withdraw', 'checkbalance', 'limitwithdrawls', 'interest', 'exit'], n=1, cutoff=0.6)
        # Everything here is just used to handle what the user wants to do with their savings.
        if refined_savings_choice:
            choice = refined_savings_choice[0]
            if choice == 'deposit':
                amount = input("How much would you like to deposit? ").strip()
                if amount.isdigit():
                    savings_account.deposit(int(amount))
            elif choice == 'withdraw':
                savings_account.limit_with_drawals()
            elif choice == 'checkbalance':
                savings_account.check_balance()
            elif refined_savings_choice == 'limitwithdrawls':
                savings_account.limit_with_drawals()
            elif choice == 'interest':
                rate = input("Please enter the interest rate you would like to add: ").strip()
                try:
                    savings_account.interest(float(rate))
                except ValueError:
                    print(Fore.RED + f"{rate} is an invalid interest rate, please try again.")
            elif choice == 'exit':
                print("Thanks for using my bank simulation, bye!")
                break
        # This is what happens if the user enters something that doesn't match any of the options:
        else:
            print(Fore.RED + f"{savings_choice} is an invalid choice, please try again.")
            
# This is what happens if the user enters an invalid input:
else:
    print(Fore.RED + f"{account_selection} is an invalid input, please try again.")
    exit()