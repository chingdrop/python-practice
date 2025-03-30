# Version 2
# Latest Version - Chapter 6
# Happy Birthday using value returning functions


def happy():
    return "Happy birthday to you!\n"


def verse_for(person):
    lyrics = f"{happy() * 2} Happy birthday, dear {person}.\n{happy()}"
    return lyrics


def happy_birthday():
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verse_for(person))


# Version 2
# Latest Version - Chapter 5
# A program to print the month abbreviation, given its number.


def month():
    # months is a list used as a lookup table
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    n = int(input("Enter a month number (1-12): "))
    print(f"The month abbreviation is {months[n - 1]}.")


# Latest Version - Chapter 5
# Simple string processing program to generate usernames.


def username():
    print("This program generates computer usernames.\n")

    # get user's first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]

    # output the username
    print(f"Your username is: {uname}")


# Latest Version - Chapter 5
# Program to create a file of usernames in batch mode.


def username_from_file():
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


# Latest Version - Chapter 5
# Prints a file to the screen.


def print_from_file():
    fname = input("Enter filename: ")
    with open(fname, "r") as file:
        data = file.read()
        print(data)


# Latest Version - Chapter 11


def by_freq(pair):
    return pair[1]


def word_freq():
    print(
        "This program analyzes word frequency in a file and prints a report on the n most frequent words.\n"
    )

    # get the sequence of words from the file
    fname = input("File to analyze: ")
    with open(fname, "r").read() as text:
        text = text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = text.replace(ch, " ")
        words = text.split()

    # construct a dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # output analysis of n most frequent words.
    n = int(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key=by_freq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print(f"{word:<15}{count:>5}")
