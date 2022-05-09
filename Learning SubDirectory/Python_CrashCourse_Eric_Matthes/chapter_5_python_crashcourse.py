#               CHAPTER 5: IF STATEMENTS

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
mammal = 'whale'
print('Is mammal == "whale"? i predict True.')
print(mammal == 'whale')
print(mammal == 'chicken')
# •	 Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# •	 Create at least ten tests. Have at least five tests evaluate to True and
# another five tests evaluate to False.
girl_name = 'Bella'
print(girl_name == 'Mike')

boy_name = 'Tunde'
print(boy_name == 'Tunde')

# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# •	 Tests for equality and inequality with strings
girl_name = 'Bella'
print(girl_name == 'Mike')

boy_name = 'Tunde'
print(boy_name != 'Bayo')

# •	 Tests using the lower() method
boy_name = 'Tunde'
print(boy_name.lower() == 'tunde')
print(boy_name.upper() != 'TUNDE')

# •	 Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
test_1 = 50
print(test_1 > 100)

# •	 Tests using the and keyword and the or keyword
test_1 = 50
print(test_1 > 100 and test_1 < 80)


# •	 Test whether an item is in a list
lista = ['cat', 'dog']
print('dog' in lista)
if 'goat' not in lista:
    print('\noops')

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
alien_color = ['green', 'yellow', 'red']

# •	 Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('you just earned 5 XP')

# •	 Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
alien_color = ['green', 'yellow', 'red']
if 'yellow' in alien_color:
    print('you just earned 5 XP')
if 'purple' in alien_color:
    print("hey")

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.
alien_color = ['brown']
if 'brown' in alien_color:
    print(f'its colour is {alien_color[0]}')
else:
    print('the alien is colorless')

# •	 If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
alien_color = ['green']
if 'green' in alien_color:
    print('Player 1 just earned 5 XP')

# •	 If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
alien_color = ['blue']
if 'green' in alien_color:
    print('Player 1 just earned 5 XP')
if 'green' not in alien_color:
    print('Player 1 just earned 10 points')

# •	 Write one version of this program that runs the if block and another that
# runs the else block.
alien_color = ['blue']
if 'green' in alien_color:
    print('Player 1 just earned 5 XP')
if 'green' not in alien_color:
    print('Player 1 just earned 10 points')
    ###
alien_color = ['blue']
if 'green' in alien_color:
    print('Player 1 just earned 5 XP')
else:
    print('Player 1 just earned 10 points')

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed
# for the appropriate color alien.
alien_color = 'turqouise'
if alien_color == 'green':
    print('the player earned 5 points')
elif alien_color == 'yellow':
    print('the player earned 10 points.')
elif alien_color == 'red':
    print('the player earned 15 points')
else:
    print('nada')

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# •	 If the person is less than 2 years old, print a message that the person is
# a baby.
# •	 If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
# •	 If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# •	 If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# •	 If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# •	 If the person is age 65 or older, print a message that the person is an
# elder.
Joshua_age = 22
if Joshua_age < 2:
    print('Josh is such a baby')
elif Joshua_age >= 2 and Joshua_age < 4:
    print('Joshua is a toddler')
elif Joshua_age >= 4 and Joshua_age < 13:
    print('Joshua is still a kid')
elif Joshua_age >= 13 and Joshua_age < 20:
    print('Joshua is still a teenager')
elif Joshua_age >= 20 and Joshua_age < 65:
    print('Joshua is an adult')
else:
    print('Joshua is an elder')

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# •	 Make a list of your three favorite fruits and call it favorite_fruits.
# •	 Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!
fav_fruits = []
fav_fruits.append('Oranges')
fav_fruits.append('Bananas')
fav_fruits.append('Mangoes')
fav_fruits.append('grapes')

if 'kiwis' in fav_fruits:
    print('You must really like kiwis!')
if 'Bananas' in fav_fruits:
    print('You seem to like Bananas')

# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.
usernames = ['Bayo', 'Taiwo', 'Nacho', 'admin']
if 'admin' in usernames:
    print('Hello admin, would you like to see a status report?')
if 'Bayo' in usernames:
    print('\nHello Bayo, thank you for logging in again!')
if 'Taiwo' in usernames:
    print('Hello Taiwo, thank you for logging in again!')
if 'Nacho' in usernames:
    print('Hello Nacho, thank you for logging in again!')

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# •	 If the list is empty, print the message We need to find some users!
# •	 Remove all of the usernames from your list, and make sure the correct
# message is printed.
usernames = []
if usernames == []:
    print('We need to  find some users!')

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# •	 Make a list of five or more usernames called current_users.
current_users = ['Bayo', 'Taiwo', 'Nacho', 'Tyler', 'Kenny']

# •	 Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
new_users = ['Adam', 'Bayo', 'Kenny', 'Cassie', 'Nate']

# •	 Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
current_users = ['Bayo', 'Taiwo', 'Nacho', 'Tyler', 'Kenny']
new_users = ['Adam', 'Bayo', 'Kenny', 'Cassie', 'Nate']
for users in new_users:
    if users in current_users:
        print(f'{users}, you need to enter a new username')
    else:
        print(f'{users}, username is available')


# •	 Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)
current_users = ['Bayo', 'Taiwo', 'Nacho', 'Tyler', 'Kenny']
ucurrent_users = ['BAYO', 'TAIWO', 'NACHO', 'TYLER', 'KENNY']

new_users = ['Adam', 'Bayo', 'KENNY', 'Cassie', 'Nate']
for users in new_users:
    if users in current_users or users in ucurrent_users:
        print(f'{users}, you need to enter a new username')
    else:
        print(f'{users}, username is available')

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •	 Store the numbers 1 through 9 in a list.
numbers = list(range(1, 10))
print(numbers)

# •	 Loop through the list.
numbers = list(range(1, 10))
for number in numbers:
    print(number)

# •	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line
numbers = list(range(1, 10))
for num in numbers:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')
