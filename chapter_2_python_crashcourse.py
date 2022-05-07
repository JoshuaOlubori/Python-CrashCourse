
#               CHAPTER 2: VARIABLES AND SIMPLE DATA TYPES

# 2-1. Simple Message: Assign a message to a variable, and then print that
# message.
name = 'Bayo'
print(name)

# 2-2. Simple Messages: Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print the new
# message.
name = 'Austin'
print(name)

name = "Bayo"
print(name)

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case
name = 'Bayo'
print(name.title())
print(name.upper())
print(name.lower())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a
# mistake never tried anything new.”
print("Bertrand Russell wrote (paraphrased): '...Be a licensed lunatic'")

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
# famous person’s name using a variable called famous_person. Then compose
# your message and represent it with a new variable called message. Print your
# message
famous_person = "Bertrand Russell wrote (paraphrased): '...Be a licensed lunatic'"
print(famous_person)

# 2-7. Stripping Names: Use a variable to represent a person’s name, and include
# some whitespace characters at the beginning and end of the name. Make sure
# you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().
message = ' Bayo \t Kayode '
print(message)
print(message.lstrip())
print(message.rstrip())
print(message.strip())

#underscores in numbers
# used to make large groups of numbers more readable without affecting their value
universe_age = 14_000_000_000
print(universe_age)

# multiple assignment
# You can assign values to more than one variable using just a single line.
# This can help shorten your programs and make them easier to read; you’ll
# use this technique most often when initializing a set of numbers.
# For example, here’s how you can initialize the variables x, y, and z
# to zero:
x, y, z = 0, 0, 0
print(x)
print(y)
print(x, y)

# Constants
# A constant is like a variable whose value stays the same throughout the life
# of a program. Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a
# constant and never be changed:
MAX_ATTENDANCE = 1000

# 2-8. Number Eight: Write addition, subtraction, multiplication, and division
# operations that each result in the number 8.
print(4+4)
print(10-2)
print(4*2)
print(16/2)

# 2-9. Favorite Number: Use a variable to represent your favorite number. Then,
# using that variable, create a message that reveals your favorite number. Print
# that message
favourite_num = 2000
print(f"my fav. number is {favourite_num}")
