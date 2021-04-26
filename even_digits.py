#Write a function that takes two integers as arguments and finds all numbers
#between them (both included) where each digit of the number is an even number.

#For example, for arguments 10 and 30, the function should give you numbers 20,
#22, 24, 26 and 28, as they're the only numbers between 10-30 where all digits are even.



#The numbers obtained should be returned as a comma-separated string on a single line.

#Examples:

#even_digits(10, 30) -> 20,22,24,26,28
#even_digits(1, 100) -> 2,4,6,8,20,22,24,26,28,40,42,44,46,48,60,62,64,66,68,80,82,84,86,88
#even_digits(200, 400) -> 200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,2


def even_digits(lower, upper):
    super_even = []
    for i in range(lower, upper):
        numeral = str(i)
        length = len(numeral)
        for index in range(length):
            if index == length - 1:
                if (int(numeral[index])%2) == 0:
                    super_even.append(str(i))
            else:
                digit = int(numeral[index])
                if digit%2 != 0:
                    break
                else:
                    continue
    return ", ".join(super_even)


lower = int(input("Enter lower bound: "))
upper = int(input("enter upper bound: "))

print(even_digits(lower, upper))
