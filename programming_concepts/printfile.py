# File - printfile.py
# Latest Version - Chapter 5
# Prints a file to the screen.


def main():
    fname = input("Enter filename: ")
    with open(fname, "r") as file:
        data = file.read()
        print(data)


if __name__ == "__main__":
    main()
