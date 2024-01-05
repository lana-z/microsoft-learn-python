from datetime import date
import sys

print('Hello World')

print("show this in the console")

sum = 1 + 2
product = sum * 2
print(product)

print(date.today())
print("Today's date is: " + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

# print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1])

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

# print("calculator program")
# first_number = input("first number: ")
# second_number = input("second number: ")
# print(first_number + second_number)
# input 3 and 4 prints 34 instead of 7, fixed below

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(int(first_number) + int(second_number))


parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = parsecs * 3.26
print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")