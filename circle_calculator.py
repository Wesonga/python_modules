# Circle Calculator with Math

import math


# Calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2


# Calculate the circumference of a circle
def circle_circumference(radius):
    return 2 * math.pi * radius


# Calculate the volume of a sphere
def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


# Get input from the user
try:
    radius = float(input("Enter the radius of the circle: "))

    if radius < 0:
        print("Error: Radius cannot be negative.")
    else:
        area = circle_area(radius)
        circumference = circle_circumference(radius)
        volume = sphere_volume(radius)

        print(f"Radius: {radius}")
        print(f"Area: {area}")
        print(f"Circumference: {circumference}")
        print(f"Volume of sphere: {volume}")

except ValueError:
    print("Invalid input! Please enter a numeric radius.")
