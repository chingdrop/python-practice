# File - maxn.py
# Latest Version - Chapter 7
# Finds the maximum of a series of numbers


def main():
    n = int(input("How many numbers are there? "))

    # Set max to be the first value
    maxn = float(input("Enter a number: "))

    # Now compare the n-1 successive values
    for i in range(n - 1):
        x = float(input("Enter a number: "))
        if x > maxn:
            maxn = x

    print(f"The largest value is {maxn}")


if __name__ == "__main__":
    main()
