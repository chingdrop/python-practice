# average.py
# Version 7
# Latest Version - Chapter 8


def main():
    file_path = input("What file are the numbers in? ")
    with open(file_path, "r") as input_file:
        total = 0.0
        count = 0
        line = input_file.readline()
        while line != "":
            # update total and count for values in line
            for x_str in line.split(","):
                total = total + float(x_str)
                count = count + 1
            line = input_file.readline()
        print(f"\nThe average of the numbers is {total / count}")


if __name__ == "__main__":
    main()
