#Create a new python file. In that file create a program that works out a grade
# based on marks with the use of functions.
#The program should take the students name:
# Homework(/25) score,
#Assessment(/50) score,
# Final Exam(/100) score as inputs,
#output their name and final ICT grade as a percentage.
#Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def final_ICTGrade(Homework,Assessment, finalExam) :
  totalMark = int(Homework) + int(Assessment) + int(finalExam)
  percentage = totalMark/2
  if percentage >= 75:
    grade = "A"
  elif percentage >= 65:
    grade = "B"
  elif percentage >= 55:
    grade = "C"
  else:
    grade = "Fail"
  return percentage, grade

def student_input():
    student = input("Student Name: ")
    hw = input("Homework Mark: ")
    asses = input("Assessment Mark: ")
    fe = input("Final Exam: ")
    return student, hw, asses, fe

def print_grade():
    (student, hw, asses, fe) = student_input()
    (percentage, grade) = final_ICTGrade(hw, asses, fe)
    print(f"{student} has a percentage of {percentage} with grade {grade}")


print_grade()
