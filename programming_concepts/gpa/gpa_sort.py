# gpa_sort.py
# Latest Version - Chapter 11
# A program to sort student information into GPA order.

from programming_concepts.gpa.gpa import Student, make_student


def read_students(filename):
    with open(filename, "r") as input_file:
        students = []
        for line in input_file:
            students.append(make_student(line))
    return students


def write_students(students, filename):
    with open(filename, "w") as output_file:
        for s in students:
            print(
                f"{s.get_name()}\t{s.get_hours()}\t{s.get_q_points()}", file=output_file
            )


def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = read_students(filename)
    data.sort(key=Student.gpa)
    filename = input("Enter a name for the output file: ")
    write_students(data, filename)
    print(f"The data has been written to {filename}")


if __name__ == "__main__":
    main()
