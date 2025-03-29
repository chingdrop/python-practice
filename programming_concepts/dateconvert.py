# File - dateconvert.py
# Version 2
# Latest Version - Chapter 5
# Converts day month and year numbers into two date formats


def main():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    date1 = f"{str(month)} / {str(day) / {str(year)}}"

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    month_str = months[month - 1]
    date2 = f"{month_str} {str(day)}, {str(year)}"

    print(f"The date is: {date1} or {date2}.")


if __name__ == "__main__":
    main()
