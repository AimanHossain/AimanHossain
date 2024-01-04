def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"
def main():
    try:
        a = float(input("Enter the length of the first side: "))
        b = float(input("Enter the length of the second side: "))
        c = float(input("Enter the length of the third side: "))
        if a <= 0 or b <= 0 or c <= 0:
            print("Side lengths must be positive values.")
        elif is_triangle(a, b, c):
            triangle_type = classify_triangle(a, b, c)
            print(f"These side lengths make sense, you can form a triangle of the {triangle_type} type!")
        else:
            print("These side lengths cannot form a triangle, as the sum of the side lengths doesn't make sense.")
    except ValueError:
        print("Please enter valid numeric values for the side lengths.")
