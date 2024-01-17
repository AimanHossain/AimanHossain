def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    try:
        # Get the lengths of the sides from the user
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        side3 = float(input("Enter the length of the third side: "))

        # Check if the sides form a valid triangle using the triangle inequality
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            print("The sides form a valid triangle.")

            # Classify the type of triangle
            triangle_type = classify_triangle(side1, side2, side3)
            print(f"The triangle is {triangle_type}.")

        else:
            print("The sides do not form a valid triangle.")

    except ValueError:
        print("Please enter valid numerical values for the side lengths.")

if __name__ == "__main__":
    main()
