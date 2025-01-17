'''
COMP 3270 Intro to Algorithms Homework 0: Introduction to Python
install python (google it) and make sure you have python version 3.6+ 
'''

# this is a single line comment just so you knowsl 

'''
This is a multi
line comment just fyi
'''

#Problem 1: print the string hello world to standard out
print("hello world")


'''
Problem 2: declare variables with the types int, float, boolean, Nonetype and print their values and types
then perform operations additions, subtraction, multiplication, division, and power on the float and integer division and modulo on the int
'''
some_int = 420
some_float = 13.37
some_bool = True
some_none = None
print(type(some_int), some_int)
print(type(some_float), some_float)
print(type(some_bool), some_bool)
print(type(some_none), some_none)
print(some_float + 1)
print(some_float - 2)
print(some_float * 3)
print(some_float / 4)
print(some_float ** 5)
print(some_int // 69)
print(some_int % 69)


'''
Problem 3: declare two strings and concatenate them
then print out the 2nd character to the last character without knowing the length of the string. 
'''
s1 = "algo"
s2 = "rithms"
s1_2 = s1 + s2
print(s1_2[2:])



#Problem 4: Write a function that takes in a string name and prints out Hello, <name>!
#your code here
def hello(name):
	print(f"Hello {name}")
hello("World")


'''
Problem 5: Write a function that takes in a number x and you compute and print out x! 
'''
def factorial(x):
	if x <= 1:
		return 1
	total = 1
	temp = x
	while x > 1:
		total *= x
		x -= 1
	print(f"{temp}! = {total}")
factorial(5)

'''
Problem 6: Write if statements to check if a number is postive, negative, or 0 and print a statement to that effect
'''
num = 69
if num > 0:
	print("positive")
elif num < 0:
	print("negative")
else:
	print("zero")


'''
Problem 7: Write a function that takes in a number x and prints out x^2
'''
def square(x):
	print(x * x)
square(13)

'''
Problem 8: Make a list of the squares of the numbers 0 to 9
add 100 to the end of that list
create another list with the square of the values 11 to 15 and concatenate those lists (show me 2 ways to do this)
check if the number 25 is in that list and print if it is
do the same with a list-comprehension to generate the list
create a dictionary where the keys are the numbers 0 to 9 and the values are the square of those numbers
create a set of the unique characters in a string
'''
squares = []
for i in range(10):
	squares.append(i ** 2)
print(squares)
# list comp
squares = [x ** 2 for x in range(10)]
print(squares)

squares.append(100)
print(squares)

squares2 = []
for i in range(11, 16):
	squares2.append(i ** 2)
print(squares2)
# list comp
squares2 = [x ** 2 for x in range(11, 16)]
print(squares2)

# method one {
all_squares = squares + squares2
print(all_squares)

# method two
all_squares = list(squares)
for x in squares2:
	all_squares.append(x)
print(all_squares)

if 25 in all_squares:
	print("25 is in squares")

a_dict = dict([(x, x ** 2) for x in range(10)])
print(a_dict)

a_set = set("Hello, World!")
print(a_set)

'''
Problem 9: FizzBuzz
Write a function that takes in a list of numbers, loops over it and prints out Fizz if the number is a multiple
of 3, Buzz if it is multiple of 5, and FizzBuzz if it is a multiple of 3 and 5, otherwise print out the number
'''
def fizz_buzz(l):
	for x in l:
		m3 = x % 3 == 0
		m5 = x % 5 == 0
		if m3:
			print("Fizz", end="")
		if m5:
			print("Buzz", end="")
		if not m3 and not m5:
			print(x, end="")
		print()
fizz_buzz(list(range(1, 31)))


'''
Problem 10: Make a class called Person with attributes age and name
Make a method for that class called introduce which prints out an introduction with its name and age
Make an instance of that class and call its introduce method
'''
class Person:
	def __init__(self, age, name):
		self.age = age
		self.name = name

	def introduce(self):
		print(f"My name is {self.name}, and I am {self.age} years old")

Person(42, "Some Body").introduce()

'''
Problem 11: install numpy, import it here and get the mean of a list of numbers and print it out
'''
import numpy as np

print(np.mean(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))

