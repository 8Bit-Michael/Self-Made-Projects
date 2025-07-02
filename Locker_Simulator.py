locker_names = ['Alice', 'Ben', 'Charlotte', 'Daniel', 'Ella', 'Finn', 'Grace']
new_name = 'Chris' 

for index, name in enumerate(locker_names):
    if new_name < name:
        if name:
            locker_names.insert(index, new_name)
            break
    else:
        locker_names.append(new_name)

print(locker_names)
