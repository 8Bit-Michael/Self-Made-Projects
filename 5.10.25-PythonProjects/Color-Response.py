# The dictionary:
Colors = {
'Red':'Blue',
'Orange':'Bright Blue',
'Yellow':'Indigo',
'Green':'Violet',
'Blue':'Red',
'Bright Blue':'Orange',
'Indigo':'Yellow',
'Violet':'Green',
}
print('Welcome to my Python color wheel project! Enter in a color and I will tell you the opposite of it!')
# The code:
ColorGiven = input('Enter a color: ')
ColorGiven = ColorGiven.capitalize()

if ColorGiven not in Colors:
    print('Please enter a valid color next time.')
else:
    print('The opposite of', ColorGiven, 'is', Colors[ColorGiven])


