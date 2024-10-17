#!/usr/bin/env python
# coding: utf-8

# Function 1: Area of a Rectangle
def area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# Function 2: Area of a Circle
import math

def area_circle(radius):
    """Calculate the area of a circle."""
    return math.pi * (radius ** 2)

# Function 3: Area of a Triangle
def area_triangle(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

# Function 4: Volume of a Cube
def volume_cube(side):
    """Calculate the volume of a cube."""
    return side ** 3

# Function 5: Volume of a Cylinder
def volume_cylinder(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * (radius ** 2) * height

# Menu display
def display_menu():
    print("\nA/V Calculator Menu")
    print("Q/q: Quit")
    print("V/v: Change View (Show Equation)")
    print("D/d: Default View (Show Result Only)")
    print("1: Area of a Rectangle")
    print("2: Area of a Circle")
    print("3: Area of a Triangle")
    print("4: Volume of a Cube")
    print("5: Volume of a Cylinder")

# Function to handle invalid input
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Please enter a positive number.")
            return value
        except ValueError as e:
            print(e)

# Function to display results based on view mode
def display_result(view_mode, equation, result):
    if view_mode == 'V':
        print(f"{equation} = {result}")
    else:
        print(f"Result = {result}")

# Main calculator logic
def main():
    view_mode = 'D'  # Default view (just calculation)
    
    while True:
        display_menu()
        choice = input("Choose an option: ").lower()
        
        if choice == 'q':
            print("Quitting program...")
            break
        elif choice == 'v':
            view_mode = 'V'
        elif choice == 'd':
            view_mode = 'D'
        elif choice == '1':
            length = get_positive_float("Enter length: ")
            width = get_positive_float("Enter width: ")
            result = area_rectangle(length, width)
            display_result(view_mode, f"{length} * {width}", result)
        elif choice == '2':
            radius = get_positive_float("Enter radius: ")
            result = area_circle(radius)
            display_result(view_mode, f"{math.pi} * {radius}^2", result)
        elif choice == '3':
            base = get_positive_float("Enter base: ")
            height = get_positive_float("Enter height: ")
            result = area_triangle(base, height)
            display_result(view_mode, f"0.5 * {base} * {height}", result)
        elif choice == '4':
            side = get_positive_float("Enter side length: ")
            result = volume_cube(side)
            display_result(view_mode, f"{side}^3", result)
        elif choice == '5':
            radius = get_positive_float("Enter radius: ")
            height = get_positive_float("Enter height: ")
            result = volume_cylinder(radius, height)
            display_result(view_mode, f"{math.pi} * {radius}^2 * {height}", result)
        else:
            print("Invalid choice, try again.")

# Guard clause to prevent the script from executing when imported
if __name__ == "__main__":
    main()




