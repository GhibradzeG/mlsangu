import math

def main():
    # Input radius
    radius = float(input("Enter the radius of the circle: "))

    # Calculate area
    area = math.pi * radius ** 2

    # Print the result
    print("The area of the circle with radius", radius, "is:", area)

if __name__ == "__main__":
    main()
