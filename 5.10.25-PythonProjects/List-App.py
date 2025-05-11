import time

print("""
List-App

Hello, this is a simple list app in which you can add up to 3 things to do in a list, which 
is pretty helpful for keeping track of your tasks.
""")

time.sleep(2)

# Initialize an empty list to hold the items.
todo_list = []

# The first item.
first_item = input('What would you like to add to your list?: ')
if first_item != 'Nothing':
    time.sleep(1)
    todo_list.append(first_item)
    print(f'{first_item} has been added to your list of things to do.')

    # Ask if the user wants to keep adding more items.
    add_more = input('Do you want to keep adding items? Type "Yes" or "No": ')
    if add_more == 'Yes':
        print('Okay, please wait.')
        time.sleep(1)

        # The second item.
        item2 = input('Enter the next item: ')
        todo_list.append(item2)
        print(f'{item2} has been added to your list of things to do.')

        # Ask again if the user wants to add more items.
        add_more = input('Do you want to keep adding items? Type "Yes" or "No": ')
        if add_more == 'Yes':
            print('Okay, please wait.')
            time.sleep(1)

            # Third item.
            item3 = input('Enter the next item: ')
            todo_list.append(item3)
            print(f'{item3} has been added to your list of things to do.')

    elif add_more == 'No':
        print('Okay, nothing more will be added to your list.')

else:
    print('Okay, nothing will be added to your list.')

# Print the final list.
if len(todo_list) > 0:
    print(f'Your list of things to do is {", ".join(todo_list)}')
else:
    print('No items were added to your list.')
