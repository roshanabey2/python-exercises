#Take a list, for example my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
 #Write a program that prints out all the elements of the list that are less than 5.

#Stretch goals:
#- Instead of printing the elements one by one, make a new list that has all the
# elements less than 5 from this list in it and print out this new list.
#- Write this in just one line of Python using list comprehension.
#- Ask the user for a number and return a list that contains only elements from
#the original list that are smaller than the given number.

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
wtf = []

for num in my_list:
	if num < 5:
		new_list.append(num)

print(new_list)

newlist = [num for num in my_list if num < 5]
print(new_list)

usernum = int(input("Enter a number buddy: "))
poop = [num for num in my_list if num < usernum]
print(poop)


#Write a Python program which iterates the integers from 1 to 50.
#For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five
#Write a Python program w print "FizzBuzz".
Fizzybuzzy = []
for i in range(1, 51):
	if i%3 == 0 and i%5 == 0:
		Fizzybuzzy.append("FizzBuzz")
	elif i%3 == 0:
		Fizzybuzzy.append("Fizz")
	elif i%5 == 0:
		Fizzybuzzy.append("buzz")
	else:
		Fizzybuzzy.append(i)

print(Fizzybuzzy)

#Let’s say I give you a list:
# my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Write one line of Python that takes this list and makes a new list
#that has only the even elements of this list in it.

third_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([num for num in third_list if num%2 == 0])
