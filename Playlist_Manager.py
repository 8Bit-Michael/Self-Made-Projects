from colorama import init, Fore
import random
import time
from difflib import get_close_matches

init(autoreset=True)

def match_input(user_input, options, cutoff=0.6):
    return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)

def proper_title(s):
    return ' '.join(word.capitalize() for word in s.split())

music_data = ["Song1", "Song2", "Song3"]

if __name__ == "__main__":
    while True:
        user_options = input("""Welcome to my Playlist Manager!

Please type:
- 'add' to add a song
- 'remove' to remove a song
- 'view' to view the playlist
- 'shuffle' to reorder the songs
- 'exit' to exit the program: """)
        
        refined_user_options = match_input(user_options, ['add', 'remove', 'view', 'shuffle', 'exit'])

        if refined_user_options and refined_user_options[0] == 'add':
            additional_song_label = input("Please enter the name of the song you would like to add: ")
            song_cap = proper_title(additional_song_label)
            if song_cap not in music_data:
                music_data.append(song_cap)
                print(Fore.GREEN + f"'{song_cap}' has been added to your playlist.")
                continue_or_exit = input("Would you like to continue using the Playlist Manager? Type 'yes' to continue or 'no' to exit: ")
                refined_continue_or_exit = match_input(continue_or_exit, ['yes', 'no'])
                if refined_continue_or_exit and refined_continue_or_exit[0] == 'yes':
                    print(Fore.GREEN + "Okay, let's continue...")
                    time.sleep(2)
                    continue
                elif refined_continue_or_exit and refined_continue_or_exit[0] == 'no':
                    print("Okay exiting program, goodbye!")
                    time.sleep(1.5)
                    exit()
            else:
                print(Fore.RED + f"'{song_cap}' is already in your playlist.")

        elif refined_user_options and refined_user_options[0] == 'remove':
            song_removal = input("Please enter the name of the song you would like to remove from your playlist: ")
            song_removal = proper_title(song_removal)
            if song_removal in music_data:
                music_data.remove(song_removal)
                print(Fore.GREEN + f"'{song_removal}' has been removed from your playlist.")
                continue_or_exit = input("Would you like to continue using the Playlist Manager? Type 'yes' to continue or 'no' to exit: ")
                refined_continue_or_exit = match_input(continue_or_exit, ['yes', 'no'])
                if refined_continue_or_exit and refined_continue_or_exit[0] == 'yes':
                    print(Fore.GREEN + "Okay, let's continue...")
                    time.sleep(2)
                    continue
                elif refined_continue_or_exit and refined_continue_or_exit[0] == 'no':
                    print("Okay exiting program, goodbye!")
                    time.sleep(1.5)
                    exit()
            else:
                print(Fore.RED + f"'{song_removal}' is not in your playlist, please try again.")
                continue

        elif refined_user_options and refined_user_options[0] == 'view':
            print(Fore.GREEN + f"Your current playlist includes the following songs: {', '.join(music_data)}")
            continue_or_exit = input("Would you like to continue using the Playlist Manager? Type 'yes' to continue or 'no' to exit: ")
            refined_continue_or_exit = match_input(continue_or_exit, ['yes', 'no'])
            if refined_continue_or_exit and refined_continue_or_exit[0] == 'yes':
                print(Fore.GREEN + "Okay, let's continue...")
                time.sleep(2)
                continue
            elif refined_continue_or_exit and refined_continue_or_exit[0] == 'no':
                print("Okay exiting program, goodbye!")
                time.sleep(1.5)
                exit()
            else:
                cap_continue_or_exit = continue_or_exit.title()
                print(Fore.RED + f"'{cap_continue_or_exit}' is not a valid option, please try again.")
                continue

        elif refined_user_options and refined_user_options[0] == 'shuffle':
            print(Fore.GREEN + "Shuffling your playlist...")
            time.sleep(2)
            random.shuffle(music_data)
            print(Fore.GREEN + f"Your new playlist is: {', '.join(music_data)}")

        elif refined_user_options and refined_user_options[0] == 'exit':
            print("Okay, thanks for trying out my project, goodbye!")
            exit()

        else:
            print(Fore.RED + f"Sorry, what you typed in was not a valid option, please try again.")
