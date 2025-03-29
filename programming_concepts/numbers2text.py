# File - numbers2text.py
# Version 2
# Latest Version - Chapter 5
# A program to convert a sequence of Unicode numbers into a string of text.
# Efficient version using a list accumulator.


def main():
    print(
        "This program converts a sequence of Unicode numbers into the string of text that it represents.\n"
    )

    # Get the message to encode
    input_str = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    chars = []
    for num_str in input_str.split():
        code_num = int(num_str)  # convert digits to a number
        chars.append(chr(code_num))  # accumulate new character

    message = "".join(chars)
    print(f"\nThe decoded message is: {message}")


if __name__ == "__main__":
    main()
