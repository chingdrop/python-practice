# File - user_file.py
# Latest Version - Chapter 5
# Program to create a file of usernames in batch mode.


def main():
    print("This program creates a file of usernames from a file of names.")

    # get the file names
    input_file_path = input("What file are the names in? ")
    output_file_path = input("What file should the usernames go in? ")

    # process each line of the input file
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            # get the first and last names from line
            first, last = line.split()
            # create the username
            uname = (first[0] + last[:7]).lower()
            # write it to the output file
            with open(output_file_path, "w") as output_file:
                print(uname, file=output_file)

    # close both files
    input_file.close()
    output_file.close()

    print(f"Usernames have been written to {output_file_path}")


if __name__ == "__main__":
    main()
