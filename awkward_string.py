#Given a string of odd length greater than 7, return a new string made of the
#middle three characters of the given string

#Stretch goal: return the original string with only the middle
#three characters in upper-case, and the rest in lower-case.

string = input("Write some gibberish brother: ")
stringlength = len(string)

if stringlength%2 == 1:
    if stringlength == 3:
        print(string)
    else:
        outersegmentlength = (stringlength - 3)/2
        firstsegment = int(0 + outersegmentlength)
        print(firstsegment)
        secondsegment = int((stringlength -outersegmentlength))
        print(secondsegment)
        print(string[firstsegment:secondsegment])
        upperMiddle = string[firstsegment:secondsegment]
        print(upperMiddle.upper())
        print(string)
else:
    print("hint: the length should be odd....")
