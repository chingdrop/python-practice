# File - happy.py
# Version 2
# Latest Version - Chapter 6
# Happy Birthday using value returning functions


def happy():
    return "Happy birthday to you!\n"


def verseFor(person):
    lyrics = happy() * 2 + "Happy birthday, dear " + person + ".\n" + happy()
    return lyrics


def main():
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verseFor(person))


main()
