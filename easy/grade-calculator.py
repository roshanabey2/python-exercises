import emoji

print("Welcome to the Grade Calculator")
mathGrade = input("Please enter your Maths mark: ")
chemistryGrade = input("Please enter your Chemistry mark: ")
physicsGrade = input("Please enter your Physics mark: ")

averageScore = (int(mathGrade) + int(chemistryGrade) + int(physicsGrade))/3

if (averageScore >= 70) :
    print("You got a grade of  A")
elif (averageScore >=60):
    print("You got a grade of  B")
elif (averageScore >=50):
    print("You got a grade of  C")
else:
    print(emoji.emojize(You Failed Bro :sob:))
