# File - word_freq.py
# Latest Version - Chapter 11


def by_freq(pair):
    return pair[1]


def main():
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


if __name__ == "__main__":
    main()
