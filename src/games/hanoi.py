# File - hanoi.py
# Latest Version - Chapter 13
# Recursive solution to Towers of Hanoi problem.


def move_tower(n, source, dest, temp):
    if n == 1:
        print(f"Move disk from {source} to {dest}.")
    else:
        move_tower(n - 1, source, temp, dest)
        move_tower(1, source, dest, temp)
        move_tower(n - 1, temp, dest, source)


def hanoi(n):
    move_tower(n, "A", "C", "B")


def main():
    print("Towers of Hanoi")
    n = int(input("How many disks? "))
    move_tower(n, "A", "C", "B")


if __name__ == "__main__":
    main()
