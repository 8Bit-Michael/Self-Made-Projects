from colorama import init, Fore
from difflib import get_close_matches
def match_input(user_input, options, cutoff=0.6):
    return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)
init(autoreset=True)

class Shape:
    def area(self):
        raise NotImplementedError(Fore.RED + "This method should be overridden by subclasses.")
    
    def perimeter(self):
        raise NotImplementedError(Fore.RED + "This method should be overridden by subclasses.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.14159
        return pi * (self.radius ** 2)

    def perimeter(self):
        pi = 3.14159
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, side_length): 
        super().__init__(side_length, side_length)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base + 2 * self.height # This only works for isosceles triangles.
    
def main():
    while True:
        print("Welcome to my Geometric Shapes Calculator!")
        shape_type = input("What shape would you like to calculate? Please type 'circle', 'rectangle', 'square', 'triangle', or 'exit': ")
        refined_shape_type = match_input(shape_type, ['circle', 'rectangle', 'square', 'triangle', 'exit'])
        if refined_shape_type and refined_shape_type[0] == 'circle':
# This is the part you can just copy and paste to use for the other shapes------------------------------------------------------------------------
            input_radius = input("Please enter the radius of the circle: ")
            try:
                input_radius = float(input_radius)
                if input_radius <= 0:
                    print(Fore.RED + "The radius must be a positive number.")
                    continue
            except ValueError:
                print(Fore.RED + f"'{input_radius}' is not a valid number.")
                continue
            # This creates an instance of Circle with the given radius, 
            # so now circle_instance is equivalent to the Circle class.
            circle_instance = Circle(input_radius)
            print(Fore.GREEN + f"The area of your circle is: {circle_instance.area()}, and the perimeter is: {circle_instance.perimeter()}")
# ------------------------------------------------------------------------------------------------------------------------------------------------
        elif refined_shape_type and refined_shape_type[0] == 'rectangle':
                    input_rectangle_width = input("Please enter the width of the rectangle: ")
                    try:
                        input_rectangle_width = float(input_rectangle_width)
                        if input_rectangle_width <= 0:
                            print(Fore.RED + "The width must be a positive number.")
                            continue
                    except ValueError:
                        print(Fore.RED + f"'{input_rectangle_width}' is not a valid number.")
                        continue
                    input_rectangle_height = input("Please enter the height of the rectangle: ")
                    try:
                        input_rectangle_height = float(input_rectangle_height)
                        if input_rectangle_height <= 0:
                            print(Fore.RED + "The height must be a positive number.")
                            continue
                    except ValueError:
                        print(Fore.RED + f"'{input_rectangle_height}' is not a valid number.")
                        continue
                    rectangle_instance = Rectangle(input_rectangle_width, input_rectangle_height)
                    print(Fore.GREEN + f"The area of your rectangle is: {rectangle_instance.area()}, and the perimeter is: {rectangle_instance.perimeter()}")

        elif refined_shape_type and refined_shape_type[0] == 'square':
            input_side = input("Please enter the length of each side of the square: ")
            try:
                input_side = float(input_side)
                if input_side <= 0:
                    print(Fore.RED + "The length must be a positive number.")
                    continue
            except ValueError:
                print(Fore.RED + f"'{input_side}' is not a valid number.")
                continue
            square_instance = Square(input_side)
            print(Fore.GREEN + f"The area of your square is: {square_instance.area()}, and the perimeter is: {square_instance.perimeter()}")

        elif refined_shape_type and refined_shape_type[0] == 'triangle':
                    input_triangle_base = input("Please enter the base of the triangle: ")
                    try:
                        input_triangle_base = float(input_triangle_base)
                        if input_triangle_base <= 0:
                            print(Fore.RED + "The base must be a positive number.")
                            continue
                    except ValueError:
                        print(Fore.RED + f"'{input_triangle_base}' is not a valid number.")
                        continue
                    input_triangle_height = input("Please enter the height of the rectangle: ")
                    try:
                        input_triangle_height = float(input_triangle_height)
                        if input_triangle_height <= 0:
                            print(Fore.RED + "The height must be a positive number.")
                            continue
                    except ValueError:
                        print(Fore.RED + f"'{input_triangle_height}' is not a valid number.")
                        continue
                    triangle_instance = Triangle(input_triangle_base, input_triangle_height)
                    print(Fore.GREEN + f"The area of your triangle is: {triangle_instance.area()}, and the perimeter is: {triangle_instance.perimeter()}")
        
        elif refined_shape_type and refined_shape_type[0] == 'exit':
            print(Fore.GREEN + "Thank you for using my project, goodbye!")
            exit()

        else:
            print(Fore.RED + f"'{shape_type}' is not a valid shape type.")

if __name__ == "__main__":
    main()