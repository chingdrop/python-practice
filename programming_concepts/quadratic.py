# quadratic.py
# Version 6
# Latest Version - Chapter 7
import math


def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        disc_root = math.sqrt((b * b) - (4 * a * c))
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print(f"\nThe solutions are: {root1}, {root2}")
    except ValueError as e:
        if str(e) == "math domain error":
            print("No Real Roots")
        else:
            print("Invalid coefficient given")
    except:
        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()
