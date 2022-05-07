#               CHAPTER 4: WORKING WITH LISTS

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
for each_pizza in pizza:
    print(each_pizza)

# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
for each_pizza in pizza:
    print(f'As much as I hate {each_pizza}, I\'ll still take it today\n')

# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
for each_pizza in pizza:
    print(f'As much as I hate {each_pizza}, I\'ll still take it today\n')
print(f'I haven\'t even had a pizza in my entire life!')

# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
reptilians = ['lizards', 'crocodiles', 'gharials']
for reptile in reptilians:
    print(reptile)

# •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
reptilians = ['lizards', 'crocodiles', 'gharials']
for reptile in reptilians:
    print(f'Well, {reptile} would definitely not make great pets!')

# •	 Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!
reptilians = ['lizards', 'crocodiles', 'gharials']
for reptile in reptilians:
    print(f'Well, {reptile} would definitely not make great pets!')
print(f'Please stop buying these animals as pets!')


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
integ = range(1, 21)
for numbers in integ:
    print(numbers)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
integ = range(1, 1_000_001)
for numbers in integ:
    print(numbers)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
for numbers in range(1, 1_000_001):
    print(numbers)
print(max(range(1, 1_000_001)))
print(min(range(1, 1_000_001)))
print(sum(range(1, 1_000_001)))
# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.

for numbers in range(1, 21, 2):
    print(numbers)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
multiples_of_3 = range(3, 301, 3)
hi = list(multiples_of_3)
print(hi)

for numbers in range(3, 301, 3):
    print(numbers)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
cubes = []
for number in range(1, 11):
    cubes.append(number**3)
print(cubes)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
cubes = [number**3 for number in range(1, 11)]
print(cubes)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
print(f'The first three items in the list are {pizza[:3]}')

# •	 Print the message Two items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
print(f'Two items from the middle of the list are {pizza[1:3]}')

# •	 Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
print(f'The last three items from the list are {pizza[1:3]}')

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
friend_pizza = pizza[:]
print(friend_pizza)

# •	 Add a new pizza to the original list.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
pizza.append('chocolate')
print(pizza)

# •	 Add a different pizza to the list friend_pizzas.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
friend_pizza = pizza[:]
print(friend_pizza)
friend_pizza.append('vanilla')
print(friend_pizza)

# •	 Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
print('My favorite pizzas are:\n')
for pizzae in pizza:
    print(pizzae)

pizza = ['Pepperoni', 'Amala', 'Eba', 'Ewedu']
friend_pizza = pizza[:]
print('My friend\'s favorite pizzas are:\n')
for pizzae in friend_pizza:
    print(pizzae)

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(food)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
foods = ('salad', 'cake', 'coleslaw', 'spinach', 'asparagus')

# •	 Use a for loop to print each food the restaurant offers.
foods = ('salad', 'cake', 'coleslaw', 'spinach', 'asparagus')
for food in foods:
    print(food)

# •	 Try to modify one of the items, and make sure that Python rejects the
# change.
foods = ('salad', 'cake', 'coleslaw', 'spinach', 'asparagus')
foods.append('mango')

# •	 The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
foods = ('salad', 'cake', 'coleslaw', 'spinach', 'asparagus')
foods = ('salad', 'macaroni', 'coleslaw', 'kale', 'asparagus')
for food in foods:
    print(food)
