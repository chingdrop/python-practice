#This class was provided in the Assignment 1 help.
#add_Grades() module collects all grade input from the user.
#Method is called after the main() module prompts the user for the studentName, studentID.
def add_grades():
    
    #Prompts user for assignment scores.
    assignments = eval(input("Enter assignment scores separated by a comma: "))
    #Sums assignment scores by delimiting the input by comma.
    assignSum = sum(assignments)
    
    #Prompts user for exam scores.
    exams = eval(input("Enter exam scores separated by a comma: "))
    #Sums exam scores by delimiting the input by comma.
    examSum = sum(exams)
    
    #Prompts user for participation score.
    participation = eval(input("Enter participation score: "))
    
    #Passes the sum of all scores back to the main() module. 
    return (assignSum + examSum + participation)

#This is the main() module, it drives and conducts all other modules.
def main():
    
    #This print segment informs the user of the program's nature.
    #It also informs the user how to exit the program.
    print("This program collects student names, student IDs, and their final grades.")
    print("After collecting all the data, the program will print the information in rows.")
    print("When finished entering students, please hit enter.")
    
    #Creates two lists to hold student names and grades.
    gradeList = []
    nameList = []
    
    #This loop provides the program to work for an undecided amount of students, including 15. 
    while True:
        
        #Prompts user for studentname and studentID
        studentNameID = input("Enter studentName, student ID separated by commas: ")
        
        #This decision will end the loop when the user inputs a null string ("").
        #This is how the program ends its cycle and moves onto the print stage. 
        if studentNameID == "":
            break

        #This will append all student names from the user into a list.
        nameList.append(studentNameID)

        #After storing the name input into a list, the main module calls the add_grades() module.
        #This is placed after the loop in case the user quits. 
        finalGrades = add_grades()
        #This will append all student grades into a list. 
        gradeList.append(finalGrades)

    #This loop iterates through the student name list and prints all information stored in the lists.
    totalStudents = len(nameList)
    #I had to use range because the "for in" statement would not work with how I printed the data.
    for n in range(totalStudents):

        #prints data stored in the lists, delimited by a comma.
        #The n used in the iterative loop had to be defined as a integer instead of an object.
        #The elements in the lists had to be converted to strings so I could concantenate the print statement.
        print(str(nameList[n])+", "+str(gradeList[n]))

#main() module is called on program start.
main()
