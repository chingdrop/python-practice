# File - gpa.py
# Latest Version - Chapter 11
# Program to find student with highest GPA


class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def get_name(self):
        return self.name

    def get_hours(self):
        return self.hours

    def get_q_points(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours


def make_student(info_str):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = info_str.split("\t")
    return Student(name, hours, qpoints)


def main():
    # open the input file for reading
    filename = input("Enter name the grade file: ")
    with open(filename, "r") as input_file:

        # set best to the record for the first student in the file
        best = make_student(input_file.readline())

        # process subsequent lines of the file
        for line in input_file:
            # turn the line into a student record
            s = make_student(line)
            # if this student is best so far, remember it.
            if s.gpa() > best.gpa():
                best = s

    # print information about the best student
    print(
        f"The best student is: {best.get_name()} hours: {best.get_hours()} GPA: {best.gpa()}"
    )


if __name__ == "__main__":
    main()
