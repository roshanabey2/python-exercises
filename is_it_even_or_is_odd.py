#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?

#Stretch goals:
#- If the number is a multiple of 4, print out a different message.
#- Ask the user for two numbers: one number to check (call it num)
# and one number to divide by (check). If check divides evenly into num,
# -tell that to the user. If not, print a different appropriate message.

import math

userNum = int(input("Please enter a Number dude: "))

if userNum%2 == 0:
    if userNum%4 == 0:
        print("It's even and divisible by 4 well done")
    else:
        print("At least it's even")
else:
    print("An odd number. Better luck next time")

print("\n Another silly number Game then.")
num = int(input("\nEnter a new num: "))
check = int(input("\nAnd another: "))

if num%check == 0:
    print("Well done. You have guessed what this program is checking for." +
          " The former is divisible but the latter")
else:
    print("Common man it was obviously going to divide the two")
